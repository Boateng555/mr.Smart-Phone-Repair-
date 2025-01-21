let cart = [];

// Load cart from localStorage
function loadCart() {
  const savedCart = JSON.parse(localStorage.getItem("cart"));
  cart = savedCart || [];
  renderCart();
}

// Render cart items
function renderCart() {
  const cartContainer = document.getElementById("cart-container");
  const subtotalElement = document.getElementById("subtotal");
  const totalElement = document.getElementById("total");

  cartContainer.innerHTML = "";

  if (cart.length === 0) {
    cartContainer.innerHTML = "<p>Your cart is empty!</p>";
    subtotalElement.textContent = "$0";
    totalElement.textContent = "$5";
    return;
  }

  let subtotal = 0;

  cart.forEach(item => {
    subtotal += item.quantity * parseFloat(item.price.slice(1)); // Remove $ sign

    const cartItem = document.createElement("div");
    cartItem.className = "cart-item";
    cartItem.innerHTML = `
      <img src="${item.image}" alt="${item.name}">
      <div class="details">
        <h3>${item.name}</h3>
        <p>${item.price} x ${item.quantity}</p>
      </div>
      <div class="actions">
        <button onclick="removeFromCart(${item.id})">Remove</button>
        <button onclick="decreaseQuantity(${item.id})">-</button>
        <button onclick="increaseQuantity(${item.id})">+</button>
      </div>
    `;
    cartContainer.appendChild(cartItem);
  });

  const deliveryFee = 5;
  const total = subtotal + deliveryFee;

  subtotalElement.textContent = `$${subtotal.toFixed(2)}`;
  totalElement.textContent = `$${total.toFixed(2)}`;
}

// Increase quantity
function increaseQuantity(productId) {
  const product = cart.find(item => item.id === productId);
  product.quantity += 1;
  saveCart();
  renderCart();
}

// Decrease quantity
function decreaseQuantity(productId) {
  const product = cart.find(item => item.id === productId);
  if (product.quantity > 1) {
    product.quantity -= 1;
  } else {
    removeFromCart(productId);
  }
  saveCart();
  renderCart();
}

// Remove item from cart
function removeFromCart(productId) {
  cart = cart.filter(item => item.id !== productId);
  saveCart();
  renderCart();
}

// Save cart to localStorage
function saveCart() {
  localStorage.setItem("cart", JSON.stringify(cart));
}

// Navigate to checkout
function goToCheckout() {
  window.location.href = "checkout.html";
}

// Initialize
loadCart();


// Toggle the visibility of the menu on small screens
function toggleMenu() {
  const navRight = document.querySelector(".nav-right");
  navRight.classList.toggle("active");
}