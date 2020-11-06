var productPopup = document.getElementById('productPopup');


function displayProductPopup(productId) {
    product = JSON.parse(document.getElementById(productId).textContent);

    document.getElementById('name').innerText = product['name'];
    document.getElementById('price').innerText = `$${product['price'].toFixed(2)}`;
    document.getElementById('image').src = `/static/images/smartphone/products/${product['imageFileName']}`;
    document.getElementById('prosSummary').innerText = product['prosSummary'];
    document.getElementById('consSummary').innerText = product['consSummary'];

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
