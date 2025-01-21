let cart = [];

// Load cart from localStorage
function loadCart() {
  const savedCart = JSON.parse(localStorage.getItem("cart"));
  cart = savedCart || [];
  renderOrderSummary();
}

// Render order summary
function renderOrderSummary() {
  const summaryContainer = document.getElementById("summary-container");
  const subtotalElement = document.getElementById("subtotal");
  const totalElement = document.getElementById("total");

  summaryContainer.innerHTML = "";

  if (cart.length === 0) {
    summaryContainer.innerHTML = "<p>Your cart is empty!</p>";
    subtotalElement.textContent = "$0";
    totalElement.textContent = "$5";
    return;
  }

  let subtotal = 0;

  cart.forEach(item => {
    subtotal += item.quantity * parseFloat(item.price.slice(1)); // Remove $ sign

    const summaryItem = document.createElement("div");
    summaryItem.className = "summary-item";
    summaryItem.innerHTML = `
      <p>${item.name} x ${item.quantity} - ${item.price}</p>
    `;
    summaryContainer.appendChild(summaryItem);
  });

  const deliveryFee = 5;
  const total = subtotal + deliveryFee;

  subtotalElement.textContent = `$${subtotal.toFixed(2)}`;
  totalElement.textContent = `$${total.toFixed(2)}`;
}

// Place order function
function placeOrder() {
  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const address = document.getElementById("address").value.trim();
  const phone = document.getElementById("phone").value.trim();

  if (!name || !email || !address || !phone) {
    alert("Please fill out all shipping details.");
    return;
  }

  // Clear cart and localStorage
  cart = [];
  localStorage.removeItem("cart");

  // Display confirmation message (for simplicity)
  alert("Order placed successfully! Thank you for shopping with us.");

  // Redirect to home or order confirmation page
  window.location.href = "index.html";
}

// Initialize
loadCart();




// for the payment page

function placeOrder() {
  const name = document.getElementById("name").value.trim();
  const email = document.getElementById("email").value.trim();
  const address = document.getElementById("address").value.trim();
  const phone = document.getElementById("phone").value.trim();

  if (!name || !email || !address || !phone) {
    alert("Please fill out all shipping details.");
    return;
  }

  const total = parseFloat(document.getElementById("total").textContent.slice(1)); // Remove $ sign
  localStorage.setItem("paymentTotal", JSON.stringify(total)); // Pass total to payment page

  window.location.href = "payment.html"; // Redirect to payment page
}


// Toggle the visibility of the menu on small screens
function toggleMenu() {
  const navRight = document.querySelector(".nav-right");
  navRight.classList.toggle("active");
}