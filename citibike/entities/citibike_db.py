import sqlite3
from sqlite3 import OperationalError

class CitibikeDb():

    def __init__(self):
        self.connection = sqlite3.connect('/home/matt/code/citibike/citibike/db/citibike.db')

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