// Sample status data (for demonstration)
const orderStatuses = {
  "Processing": "Your order has been received and is currently being processed.",
  "Shipped": "Your order has been shipped and is on its way.",
  "Delivered": "Your order has been delivered. Enjoy!",
  "Returned": "Your return request has been processed."
};

// Function to track order status
function trackOrder() {
  const orderNumber = document.getElementById("tracking-id").value.trim();
  const orderHistory = JSON.parse(localStorage.getItem("orderHistory")) || [];
  const returnRequests = JSON.parse(localStorage.getItem("returnRequests")) || [];
  const trackingResult = document.getElementById("tracking-result");

  // Clear previous results
  trackingResult.innerHTML = "";

  if (!orderNumber) {
    trackingResult.textContent = "Please enter a valid order number.";
    return;
  }

  // Find order in order history
  const orderIndex = parseInt(orderNumber) - 1; // Adjust for index (order numbers start at 1)
  const order = orderHistory[orderIndex];

  if (order) {
    // Generate tracking details for the found order
    const statusMessage = orderStatuses[order.status] || "Status not available.";
    trackingResult.innerHTML = `
      <p><strong>Order Number:</strong> #${orderNumber}</p>
      <p><strong>Status:</strong> ${order.status}</p>
      <p>${statusMessage}</p>
      <p><strong>Items:</strong></p>
      <ul>
        ${order.items.map(item => `<li>${item.quantity}x ${item.name}</li>`).join("")}
      </ul>
    `;
    return;
  }

  // Find in return requests
  const returnIndex = returnRequests.findIndex(req => req.orderNumber === orderNumber);
  if (returnIndex !== -1) {
    trackingResult.innerHTML = `
      <p><strong>Order Number:</strong> #${orderNumber}</p>
      <p><strong>Status:</strong> Returned</p>
      <p>${orderStatuses["Returned"]}</p>
    `;
    return;
  }

  // If no match found
  trackingResult.textContent = "Order not found. Please check the order number and try again.";
}


// Toggle the visibility of the menu on small screens
function toggleMenu() {
  const navRight = document.querySelector(".nav-right");
  navRight.classList.toggle("active"); // Toggle the 'active' class to show/hide the menu
}