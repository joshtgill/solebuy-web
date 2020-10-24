var productPopup = document.getElementById('productPopup');

function openProductPopup(product) {
    document.getElementById('name').innerText = product['name'];
    document.getElementById('price').innerText = `$${product['price']}`;
    document.getElementById('image').src = `/static/images/products/${product['imagePath']}`;
    productPopup.style.display = "block";
}

function closeProductPopup() {
    productPopup.style.display = 'none';
}

document.getElementsByClassName('close')[0].onclick = function() {
    closeProductPopup();
}

window.onclick = function(event) {
    if (event.target == productPopup)
        closeProductPopup()
}
