topNav = document.getElementById('topNav');
categoryBar = document.getElementById('categoryBar');


function toggleCategoryBar() {
    if (!categoryBar.style.display || categoryBar.style.display == 'none')
        displayCategoryBar();
    else
        hideCategoryBar()
}


function displayCategoryBar(homePageStyle) {
    if (homePageStyle) {
        document.getElementById('categoriesClickable').style.display = 'none';
        categoryBar.style.backgroundColor = 'rgb(242, 242, 242)';
        document.getElementById('categoryBarItemLabel').style.color = 'rgb(17, 17, 17)';
    }

    topNav.style.minHeight = '155px';
    categoryBar.style.display = 'flex';
}


function hideCategoryBar() {
    topNav.style.minHeight = '55px';
    categoryBar.style.display = 'none';
}
