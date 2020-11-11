var productPopup = document.getElementById('productPopup');


function displayProductPopup(productId) {
    product = JSON.parse(document.getElementById(productId).textContent);

    // Load and display general product data
    document.getElementById('name').innerText = product['name'];
    document.getElementById('price').innerText = `Starting at $${product['price'].toFixed(2)}`;
    document.getElementById('image').src = `/static/images/smartphone/products/${product['imageFileName']}`;
    document.getElementById('prosSummary').innerText = product['prosSummary'];
    document.getElementById('consSummary').innerText = product['consSummary'];

    // Clear alternatives for fresh load
    var alternativesDiv = document.getElementById('alternatives');
    alternativesDiv.querySelectorAll('*').forEach(e => e.remove());

    // Load and display product's alternatives
    var alternativeProducts = product['alternativeProducts'];
    if (alternativeProducts.length > 0) {
        // Create label for alternatives and add to parent
        var alternativesLabel = document.createElement('h1');
        alternativesLabel.innerHTML = 'Similar products: ';
        alternativesDiv.appendChild(alternativesLabel);

        // Create alternative products div
        var alternativeProductsDiv = document.createElement('div');
        alternativeProductsDiv.className = 'alternative-products';
        alternativesDiv.appendChild(alternativeProductsDiv);

        // For each alternative product, create a div containing alternative product name
        for (i = 0; i < alternativeProducts.length; i++) {
            var alternativeProductDiv = document.createElement('div');
            alternativeProductDiv.className = 'alternative-product';

            var alternativeProductH1 = document.createElement('h1');
            alternativeProductH1.innerHTML = alternativeProducts[i];
            alternativeProductDiv.appendChild(alternativeProductH1);

            alternativeProductsDiv.appendChild(alternativeProductDiv);
        }
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
