// Display Order History
function displayOrderHistory() {
  const historyContainer = document.getElementById("history-container");

  // Fetch order history from localStorage
  const orderHistory = JSON.parse(localStorage.getItem("orderHistory")) || [];

  if (orderHistory.length === 0) {
    historyContainer.innerHTML = "<p>No orders found.</p>";
    return;
  }

  // Create order cards
  orderHistory.forEach((order, index) => {
    const orderCard = document.createElement("div");
    orderCard.classList.add("order-card");

    orderCard.innerHTML = `
      <h2>Order #${index + 1}</h2>
      <p><strong>Date:</strong> ${order.date}</p>
      <p><strong>Total:</strong> $${order.total.toFixed(2)}</p>
      <h3>Items:</h3>
      <ul>
        ${order.items.map(item => `<li>${item.quantity}x ${item.name} - $${item.price}</li>`).join("")}
      </ul>
      <h3>Shipping Details:</h3>
      <p>${order.shipping.name}, ${order.shipping.address}</p>
    `;

    historyContainer.appendChild(orderCard);
  });
}

// Initialize page
displayOrderHistory();


// Toggle the visibility of the menu on small screens
function toggleMenu() {
  const navRight = document.querySelector(".nav-right");
  navRight.classList.toggle("active");
}