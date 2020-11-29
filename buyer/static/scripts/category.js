var productPopupContainer = document.getElementById('productPopupContainer');
var assisterHelpPopupContainer = document.getElementById('assisterHelpPopupContainer');


function displayProductPopup(productIndexedId) {
    product = JSON.parse(document.getElementById(productIndexedId).textContent);

    // Initialize and clear details for fresh popup
    var detailsDiv = document.getElementById('details');
    detailsDiv.querySelectorAll('*').forEach(cn => cn.remove());

    // Load and display general product data
    document.getElementById('name').innerText = product['name'];
    document.getElementById('image').src = `/static/images/smartphone/products/${product['imageFileName']}`;
    document.getElementById('prosSummary').innerText = product['prosSummary'];
    document.getElementById('consSummary').innerText = product['consSummary'];
    addProductDetail(detailsDiv, 'Starting price', `$${product['price'].toFixed(2)}`);
    addProductDetail(detailsDiv, 'Starting capacity', `${product['entryCapacity']} GB`);
    addProductDetail(detailsDiv, 'Display', `${product['displayDescription']}`);
    addProductDetail(detailsDiv, 'Camera', `${product['cameraDescription']}`);
    addProductDetail(detailsDiv, 'Battery life', `${product['batteryDescription']}`);

    // Show popup at top
    productPopupContainer.style.display = 'block'
    document.getElementById('productPopup').scrollTop = 0;
}


function addProductDetail(detailsDiv, label, value) {
    var detailDiv = document.createElement('div');
    detailDiv.className = 'detail';

    var labelDiv = document.createElement('div');
    labelDiv.className = 'label';
    var labelH1 = document.createElement('h1');
    labelH1.innerHTML = label;
    labelDiv.appendChild(labelH1);
    detailDiv.appendChild(labelDiv);

    var valueDiv = document.createElement('div');
    valueDiv.className = 'value';
    var valueH1 = document.createElement('h1');
    valueH1.innerHTML = value;
    valueDiv.appendChild(valueH1);
    detailDiv.appendChild(valueDiv);

    detailsDiv.appendChild(detailDiv);
}


productPopupContainer.onclick = function(event) {
    productPopupContainer.style.display = 'none';
}


function displayAssisterPopup(assisterIndexedId) {
    assisterData = JSON.parse(document.getElementById(assisterIndexedId).textContent);

    // Initialize and clear filter helps
    assisterHelpPopup = document.getElementById('assisterHelpPopup');
    assisterHelpPopup.querySelectorAll('*').forEach(cn => cn.remove());

    // File assister popup with its filters and descriptions
    for (contents in assisterData['filtersData'])
        addFilterHelp(assisterHelpPopup, contents, assisterData['filtersData'][contents]);

    // Shop popup at top
    assisterHelpPopupContainer.style.display = 'block';
    assisterHelpPopup.scrollTop = 0;
}


function addFilterHelp(assisterHelpPopup, contents, explanation) {
    var filterHelp = document.createElement('div');
    filterHelp.className = 'filter-help';

    var filterContents = document.createElement('h1');
    filterContents.innerHTML = contents;
    filterHelp.appendChild(filterContents);

    filterHelp.appendChild(document.createElement('hr'));

    var filterExplanation = document.createElement('p');
    filterExplanation.innerHTML = explanation;
    filterHelp.appendChild(filterExplanation);

    assisterHelpPopup.appendChild(filterHelp);
}


assisterHelpPopupContainer.onclick = function() {
    assisterHelpPopupContainer.style.display = 'none';
}


window.onclick = function(event) {
    if (categoryBar.style.display == 'flex' && event.target.id != 'categoriesClickable' &&
        event.target.id != 'categoryBar')
            hideCategoryBar();
}


document.getElementById('categoryContent').onscroll = function() {
    hideCategoryBar();
}
