import inspect
import sqlite3
from sqlite3 import OperationalError


def update_object_from_dictionary_representation(dictionary, instance):
    """Given a dictionary and an object instance, will set all object attributes equal to the dictionary's keys and
    values. Assumes dictionary does not have any keys for which object does not have attributes

    @type dictionary: dict
    @param dictionary: Dictionary representation of the object
    @param instance: Object instance to populate
    @return: None
    """
    for key, value in dictionary.items():
        if hasattr(instance, key):
            setattr(instance, key, value)

    return instance


def get_object_from_dictionary_representation(dictionary, class_type):
    """Instantiates a new class (that takes no init params) and populates its attributes with a dictionary

    @type dictionary: dict
    @param dictionary: Dictionary representation of the object
    @param class_type: type
    @return: None
    """
    assert inspect.isclass(class_type), 'Cannot instantiate an object that is not a class'
    instance = class_type()
    update_object_from_dictionary_representation(dictionary, instance)

    return instance

class CitibikeDb():

    def __init__(self):
        def dict_factory(cursor, row):
            d = {}
            for idx, col in enumerate(cursor.description):
                d[col[0]] = row[idx]
            return d
        self.connection = sqlite3.connect('/home/matt/code/citibike/citibike/db/citibike.db')
        self.connection.row_factory = dict_factory

    def __del__(self):
        self.connection.close()

    def execute(self, *args, **kwargs):
        """Executes the sql statement, but does not commit. Returns the cursor to commit

        @return: DB and cursor instance following sql execution
        """

        # Execute the query
        cursor = self.connection.cursor()
        try:
            cursor.execute(*args, **kwargs)
        except OperationalError as e:
            raise OperationalError('{} when executing: {}'.format(e.args, args[0]))

        return cursor

    def execute_and_commit(self, *args, **kwargs):
        """Executes and commits the sql statement

        @return: None
        """
        cursor = self.execute(*args, **kwargs)
        self.connection.commit()
        return cursor

    def insert(self, sql, *args, **kwargs):
        """Inserts and commits with an insert sql statement, returns the record, but with a small chance of a race
        condition

        @param sql: sql to execute
        @return: The last row inserted
        """

        assert "insert into" in sql.lower(), 'This function requires an insert statement, provided: {}'.format(sql)
        cursor = self.execute_and_commit(sql, *args, **kwargs)

        # now get that id
        last_row_id = cursor.lastrowid
        cursor.close()

        return last_row_id

    def get_single_record(self, *args, **kwargs):
        cursor = self.execute(*args, **kwargs)
        result = cursor.fetchone()
        cursor.close()

        return result

    def get_single_instance(self, sql, class_type, *args, **kwargs):
        """Returns an instance of class_type populated with attributes from the DB record; throws an error if no
        records are found

        @param sql: Sql statement to execute
        @param class_type: The type of class to instantiate and populate with DB record
        @return: Return an instance with attributes set to values from DB
        """
        record = self.get_single_record(sql, *args, **kwargs)
        try:
            instance = get_object_from_dictionary_representation(dictionary=record, class_type=class_type)
        except AttributeError:
            raise RuntimeError('No records found for {class_type} with sql: \n {sql}'.format(
                sql=sql,
                class_type=class_type
            ))
        return instance