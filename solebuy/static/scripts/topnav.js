categoryBar = document.getElementById('categoryBar');
topNav = document.getElementById('topNav');


function toggleCategoryBar() {
    if (!categoryBar.style.display ||
        categoryBar.style.display == 'none') {
            categoryBar.style.backgroundColor = 'rgb(17, 17, 17)';
            document.getElementById('categoryBarItemH1').style.color = 'rgb(255, 255, 255)';
            displayCategoryBar();
        }
    else
        hideCategoryBar()
}

function displayCategoryBar() {
    topNav.style.minHeight = '155px';
    categoryBar.style.display = 'flex';
}

function hideCategoryBar() {
    topNav.style.minHeight = '55px';
    categoryBar.style.display = 'none';
}
