function sortTable(index) {
    var table, rows, switching, i, x, y, shouldSwitch;
    table = document.getElementById("bikeList");
    switching = true;
    var sortUp = true;

    // Determine to sort Up or Down
    sortHeader = document.getElementsByTagName("TH")[index];
    if(sortHeader.classList.length > 0) {
        if (sortHeader.classList.contains("up")) {
            sortUp = false;
        }
    }

    // sort
    while (switching) {
      switching = false;
      rows = table.rows;
      for (i = 1; i < (rows.length - 1); i++) {
        shouldSwitch = false;
        x = rows[i].getElementsByTagName("TD")[index];
        y = rows[i + 1].getElementsByTagName("TD")[index];
        if (sortUp) {
            if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                shouldSwitch = true;
                break;
            }
        }
        else {
            if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                shouldSwitch = true;
                break;
            }
        }
      }
      if (shouldSwitch) {
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
      }
    }

    // add class
    sortHeader.classList.remove("up");
    sortHeader.classList.remove("down");
    if(sortUp) {
        sortHeader.classList.add("up");
    }
    else {
        sortHeader.classList.add("down");
    }
}