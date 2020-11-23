var productPopup = document.getElementById('productPopupContainer');


function displayProductPopup(productId) {
    product = JSON.parse(document.getElementById(productId).textContent);

    // Initialize and clear details for fresh popup
    var detailsDiv = document.getElementById('details');
    detailsDiv.querySelectorAll('*').forEach(cn => cn.remove());

    // Load and display general product data
    document.getElementById('name').innerText = product['name'];
    document.getElementById('image').src = `/static/images/smartphone/products/${product['imageFileName']}`;
    document.getElementById('prosSummary').innerText = product['prosSummary'];
    document.getElementById('consSummary').innerText = product['consSummary'];
    addDetail(detailsDiv, 'Starting price', `$${product['price'].toFixed(2)}`);
    addDetail(detailsDiv, 'Starting capacity', `${product['entryCapacity']} GB`);
    addDetail(detailsDiv, 'Display', `${product['displayDescription']}`);
    addDetail(detailsDiv, 'Camera', `${product['cameraDescription']}`);
    addDetail(detailsDiv, 'Battery life', `${product['batteryDescription']}`);

    // Show product popup
    productPopup.style.display = "block";
}

function addDetail(detailsDiv, label, value) {
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

function hideProductPopup() {
    productPopup.style.display = 'none';
}


document.getElementsByClassName('close')[0].onclick = function() {
     hideProductPopup();
}


window.onclick = function(event) {
    if (event.target == productPopup)
        hideProductPopup();
    else if (categoryBar.style.display == 'flex' &&
             event.target.id != 'topNavLeftH1')
        categoryBar.style.display = 'none';
}

document.getElementById('categoryContent').onscroll = function(event) {
    categoryBar.style.display = 'none';
}
