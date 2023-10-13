const itemsPerPage = 15;
let page = 0;
const table = document.getElementsByClassName("dataframe");

function show_page (index) {
    const rows = table[0].tBodies[0].rows;
    if (index < 0) {
        show_page(0);
    } else if (index > rows.length){
        show_page(index - itemsPerPage);
    } else {
        page = index;
    }
      
    for (let i = 0; i < rows.length; i++) {
        if (i >= page && i < page + itemsPerPage) {
          rows[i].style.display = 'table-row';
        }
        else {
          rows[i].style.display = 'none';
        }
    }
}