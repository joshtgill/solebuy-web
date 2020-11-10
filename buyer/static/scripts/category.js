var productPopup = document.getElementById('productPopup');


function displayProductPopup(productId) {
    product = JSON.parse(document.getElementById(productId).textContent);

    // Load general product data
    document.getElementById('name').innerText = product['name'];
    document.getElementById('price').innerText = `$${product['price'].toFixed(2)}`;
    document.getElementById('image').src = `/static/images/smartphone/products/${product['imageFileName']}`;
    document.getElementById('prosSummary').innerText = product['prosSummary'];
    document.getElementById('consSummary').innerText = product['consSummary'];

    // Get alternative products div and remove any existing children
    alternativeProductsDiv = document.getElementById('alternative-products');
    alternativeProductsDiv.querySelectorAll('*').forEach(n => n.remove());

    // For each alternative product, create a div containing alternative product name
    alternativeProducts = product['alternativeProducts'];
    for (i = 0; i < alternativeProducts.length; i++) {
        var alternativeProductDiv = document.createElement('div');
        alternativeProductDiv.className = 'alternative-product';

        var alternativeProductH1 = document.createElement('h1');
        alternativeProductH1.innerHTML = alternativeProducts[i];

        alternativeProductDiv.appendChild(alternativeProductH1);
        alternativeProductsDiv.appendChild(alternativeProductDiv);
    }

    // Show product popup
    productPopup.style.display = "block";
}


function hideProductPopup() {
    productPopup.style.display = 'none';
}


document.getElementsByClassName('close')[0].onclick = function() {
     hideProductPopup();
}


window.onclick = function(event) {
    if (event.target == productPopup)
        hideProductPopup()
}
