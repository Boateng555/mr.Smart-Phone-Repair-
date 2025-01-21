// Load Orders into Dropdown
function loadOrders() {
  const orderHistory = JSON.parse(localStorage.getItem("orderHistory")) || [];
  const orderSelect = document.getElementById("order-select");

  if (orderHistory.length === 0) {
    orderSelect.innerHTML = "<option value=''>No orders found</option>";
    return;
  }

  // Populate dropdown with orders
  orderHistory.forEach((order, index) => {
    const option = document.createElement("option");
    option.value = index; // Store order index
    option.textContent = `Order #${index + 1} - ${order.date}`;
    orderSelect.appendChild(option);
  });
}

// Load Items for Selected Order
function loadOrderItems() {
  const orderHistory = JSON.parse(localStorage.getItem("orderHistory")) || [];
  const orderSelect = document.getElementById("order-select");
  const itemsContainer = document.getElementById("items-container");
  const submitButton = document.getElementById("submit-return");

  itemsContainer.innerHTML = ""; // Clear previous items
  submitButton.disabled = true; // Disable button by default

  const selectedOrderIndex = orderSelect.value;
  if (selectedOrderIndex === "") return; // No order selected

  const selectedOrder = orderHistory[selectedOrderIndex];

  // Display items as checkboxes
  selectedOrder.items.forEach((item, index) => {
    const itemDiv = document.createElement("div");
    itemDiv.classList.add("return-item");
    itemDiv.innerHTML = `
      <input type="checkbox" id="item-${index}" data-item='${JSON.stringify(item)}'>
      <label for="item-${index}">${item.quantity}x ${item.name} - $${item.price}</label>
    `;
    itemsContainer.appendChild(itemDiv);
  });

  submitButton.disabled = false; // Enable button once items are loaded
}

// Submit Return Request
function submitReturn() {
  const orderSelect = document.getElementById("order-select");
  const selectedOrderIndex = orderSelect.value;
  const itemsContainer = document.getElementById("items-container");
  const returnStatus = document.getElementById("return-status");

  if (selectedOrderIndex === "") {
    returnStatus.textContent = "Please select an order.";
    return;
  }

  // Collect selected items
  const checkboxes = itemsContainer.querySelectorAll("input[type='checkbox']:checked");
  if (checkboxes.length === 0) {
    returnStatus.textContent = "Please select at least one item to return.";
    return;
  }

  const returnItems = Array.from(checkboxes).map(checkbox => JSON.parse(checkbox.dataset.item));

  // Mock return submission
  console.log("Submitting return request for items:", returnItems);

  // Clear status and reset form
  returnStatus.textContent = "Your return request has been submitted.";
  document.getElementById("order-select").value = "";
  itemsContainer.innerHTML = "";
  document.getElementById("submit-return").disabled = true;
}

// Initialize page
loadOrders();


// Toggle the visibility of the menu on small screens
function toggleMenu() {
  const navRight = document.querySelector(".nav-right");
  navRight.classList.toggle("active"); // Toggle the 'active' class to show/hide the menu
}