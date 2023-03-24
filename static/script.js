/**
 * Displays a text area for the user to input a custom manufacter name when
 * 'Other' is selected from the dropdown menu in 'upload.html'.
 * @param {String} val The value of the selected option from the dropdown menu
 */
function CheckManufacturer(val){
  var element=document.getElementById('manufacturer');
  if(val==='other')
    element.style.display='block';
  else  
    element.style.display='none';
  }

/**
 * Displays only the rows that match the user input in the search bar in 
 * 'collection.html'.
 */
function search() {
  // Declare variables
  var input, filter, table, tr, td, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[1];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }
  }
}

/**
 * Sorts and reorders the rows of the collection in 'collection.html'.
 * @param {Integer} columnIndex The column to sort by.
 * @param {Boolean} asc Whether to sort in ascending or descending order.
 */
function sortTable(columnIndex, asc) {
  const table = document.getElementById("myTable");
  const rows = Array.from(table.rows).slice(1); // slice to remove header row

  rows.sort((rowA, rowB) => {
    const cellA = rowA.cells[columnIndex].textContent.toLowerCase();
    const cellB = rowB.cells[columnIndex].textContent.toLowerCase();
    
    if (!isNaN(cellA) && !isNaN(cellB)) {
      return asc ? Number(cellA) - Number(cellB) : Number(cellB) - Number(cellA);
    } else {
      return asc ? cellA.localeCompare(cellB) : cellB.localeCompare(cellA);
    }
  });

  rows.forEach(row => {
    table.tBodies[0].appendChild(row); // re-append sorted rows
  });
}