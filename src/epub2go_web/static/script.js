// needs to be included at bottom to get document references    
const params = new URLSearchParams(window.location.search);
const searchInput = document.getElementById('searchInput');
const table = document.getElementById('table');
const table_r = Array.from(table.getElementsByTagName('tr'));

// allow search from url parameter
let searchParam = params.get('s');
if (searchParam){
    searchInput.value = searchParam;
    search(searchParam);
}

function submitSearch(event){
    event.preventDefault();
    search();
}
function search(searchStr = searchInput.value){
    function showMatch(tr){
        // match search with list
        let searchSuccess = Array.from(tr.getElementsByClassName('table-data')).map(e => e.textContent)
            .join(' ')
            .indexOf(searchStr) > -1;
        if (searchSuccess) tr.style.display = "";
        else tr.style.display = "none";
    }
    table_r.map(showMatch, table_r);
}
