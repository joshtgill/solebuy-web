var productPopup = document.getElementById("productPopup");

function openProductPopup(product) {
    productName = product['name'];
    console.log(productName);
	productPopup.style.display = "block";
}

function closeProductPopup() {
	productPopup.style.display = "none";
}

document.getElementsByClassName("close")[0].onclick = function() {
    closeProductPopup();
}

window.onclick = function(event) {
    if (event.target == productPopup)
        closeProductPopup()
}
