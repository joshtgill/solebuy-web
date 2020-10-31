var productPopup = document.getElementById('productPopup');
var productInput = document.getElementById('productInput');
var productForm = document.getElementById('productForm');


function submitProductForm(productId) {
    productInput.value = productId;
    productForm.submit();
}


function closeProductPopup() {
    productInput.value = null;
    productForm.submit();
}


document.getElementsByClassName('close')[0].onclick = function() {
    closeProductPopup();
}


window.onclick = function(event) {
    if (event.target == productPopup)
        closeProductPopup()
}
