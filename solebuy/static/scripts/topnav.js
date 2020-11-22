categoryBar = document.getElementById('categoryBar');


function toggleCategoryBar() {
    if (!categoryBar.style.display
        || categoryBar.style.display == 'none') {
            categoryBar.style.backgroundColor = 'rgb(17, 17, 17)';
            document.getElementById('categoryH1').style.color = 'white';
            displayCategoryBar()
        }
    else
        hideCategoryBar()
}

function displayCategoryBar() {
    categoryBar.style.display = 'flex';
}

function hideCategoryBar() {
    categoryBar.style.display = 'none';
}
