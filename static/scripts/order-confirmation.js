// Load Order Confirmation Details
function loadOrderDetails() {
  // Retrieve order data from localStorage
  const cart = JSON.parse(localStorage.getItem("cart")) || [];
  const total = JSON.parse(localStorage.getItem("paymentTotal")) || 0;
  const shipping = JSON.parse(localStorage.getItem("shippingDetails")) || {};

  const orderSummary = document.getElementById("order-summary");
  const orderTotal = document.getElementById("order-total");
  const shippingDetails = document.getElementById("shipping-details");

  // Display Order Items
  cart.forEach(item => {
    const itemDiv = document.createElement("div");
    itemDiv.textContent = `${item.quantity}x ${item.name} - $${item.price}`;
    orderSummary.appendChild(itemDiv);
  });

  // Display Total
  orderTotal.textContent = `$${total.toFixed(2)}`;

  // Display Shipping Details
  shippingDetails.innerHTML = `
    <p><strong>Name:</strong> ${shipping.name}</p>
    <p><strong>Email:</strong> ${shipping.email}</p>
    <p><strong>Address:</strong> ${shipping.address}</p>
    <p><strong>Phone:</strong> ${shipping.phone}</p>
  `;

  // Clear localStorage after loading order details
  localStorage.clear();
}

// Redirect to Homepage
function goToHome() {
  window.location.href = "onlineshop.html";
}

// Initialize the page
loadOrderDetails();



// Order history

function loadOrderDetails() {
  // Retrieve order data from localStorage
  const cart = JSON.parse(localStorage.getItem("cart")) || [];
  const total = JSON.parse(localStorage.getItem("paymentTotal")) || 0;
  const shipping = JSON.parse(localStorage.getItem("shippingDetails")) || {};

  const orderSummary = document.getElementById("order-summary");
  const orderTotal = document.getElementById("order-total");
  const shippingDetails = document.getElementById("shipping-details");

  // Display Order Items
  cart.forEach(item => {
    const itemDiv = document.createElement("div");
    itemDiv.textContent = `${item.quantity}x ${item.name} - $${item.price}`;
    orderSummary.appendChild(itemDiv);
  });

  // Display Total
  orderTotal.textContent = `$${total.toFixed(2)}`;

  // Display Shipping Details
  shippingDetails.innerHTML = `
    <p><strong>Name:</strong> ${shipping.name}</p>
    <p><strong>Email:</strong> ${shipping.email}</p>
    <p><strong>Address:</strong> ${shipping.address}</p>
    <p><strong>Phone:</strong> ${shipping.phone}</p>
  `;

  // Save to order history
  saveOrderHistory(cart, total, shipping);

  // Clear localStorage
  localStorage.removeItem("cart");
  localStorage.removeItem("paymentTotal");
  localStorage.removeItem("shippingDetails");
}

// Save Order to Order History
function saveOrderHistory(cart, total, shipping) {
  const orderHistory = JSON.parse(localStorage.getItem("orderHistory")) || [];
  
  const newOrder = {
    date: new Date().toLocaleString(),
    items: cart,
    total: total,
    shipping: shipping
  };

  orderHistory.push(newOrder);
  localStorage.setItem("orderHistory", JSON.stringify(orderHistory));
}


// Toggle the visibility of the menu on small screens
function toggleMenu() {
  const navRight = document.querySelector(".nav-right");
  navRight.classList.toggle("active");
}