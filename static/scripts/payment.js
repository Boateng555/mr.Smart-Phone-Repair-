// Load Total Amount from Checkout
function loadPaymentTotal() {
  const total = JSON.parse(localStorage.getItem("paymentTotal")); // Stored in checkout page
  document.getElementById("payment-total").textContent = `€${total.toFixed(2)}`;
}

// Process Credit Card Payment
function processCreditCardPayment() {
  const cardName = document.getElementById("card-name").value.trim();
  const cardNumber = document.getElementById("card-number").value.trim();
  const expiryDate = document.getElementById("expiry-date").value.trim();
  const cvv = document.getElementById("cvv").value.trim();

  // Validate credit card details
  if (!cardName || !cardNumber || !expiryDate || !cvv) {
    alert("Bitte füllen Sie alle Zahlungsdetails aus.");
    return;
  }

  if (cardNumber.length !== 16 || isNaN(cardNumber)) {
    alert("Die Kartennummer muss 16 Ziffern lang sein.");
    return;
  }

  if (cvv.length !== 3 || isNaN(cvv)) {
    alert("Der CVV muss 3 Ziffern lang sein.");
    return;
  }

  // Simulate payment success
  alert("Zahlung erfolgreich! Vielen Dank für Ihren Einkauf.");

  // Clear localStorage and redirect to home
  localStorage.removeItem("cart");
  localStorage.removeItem("paymentTotal");
  window.location.href = "index.html";
}

// Render PayPal Button
function renderPayPalButton() {
  paypal.Buttons({
    createOrder: function (data, actions) {
      // Set up the transaction
      return actions.order.create({
        purchase_units: [{
          amount: {
            value: JSON.parse(localStorage.getItem("paymentTotal")).toFixed(2) // Total amount from localStorage
          }
        }]
      });
    },
    onApprove: function (data, actions) {
      // Capture the payment
      return actions.order.capture().then(function (details) {
        // Redirect to a success page or handle the payment confirmation
        alert("Zahlung erfolgreich! Vielen Dank für Ihren Einkauf.");
        localStorage.removeItem("cart");
        localStorage.removeItem("paymentTotal");
        window.location.href = "index.html"; // Redirect to home page
      });
    },
    onError: function (err) {
      // Handle errors
      console.error(err);
      alert("Zahlung fehlgeschlagen. Bitte versuchen Sie es erneut.");
    }
  }).render('#paypal-button-container'); // Display the PayPal button
}

// Toggle the visibility of the menu on small screens
function toggleMenu() {
  const navRight = document.querySelector(".nav-right");
  navRight.classList.toggle("active"); // Toggle the 'active' class to show/hide the menu
}

// Initialize Payment Page
function initializePaymentPage() {
  // Load the total amount
  loadPaymentTotal();

  // Render PayPal button if PayPal is selected
  const paymentMethods = document.querySelectorAll('input[name="payment-method"]');
  const creditCardForm = document.getElementById('credit-card-form');
  const paypalForm = document.getElementById('paypal-form');
  const bankTransferForm = document.getElementById('bank-transfer-form');

  paymentMethods.forEach(method => {
    method.addEventListener('change', (event) => {
      const selectedMethod = event.target.value;

      // Hide all forms
      creditCardForm.style.display = 'none';
      paypalForm.style.display = 'none';
      bankTransferForm.style.display = 'none';

      // Show the selected form
      if (selectedMethod === 'credit-card') {
        creditCardForm.style.display = 'block';
      } else if (selectedMethod === 'paypal') {
        paypalForm.style.display = 'block';
        renderPayPalButton(); // Render PayPal button when PayPal is selected
      } else if (selectedMethod === 'bank-transfer') {
        bankTransferForm.style.display = 'block';
      }
    });
  });

  // Render PayPal button initially if PayPal is selected by default
  const initialSelectedMethod = document.querySelector('input[name="payment-method"]:checked').value;
  if (initialSelectedMethod === 'paypal') {
    renderPayPalButton();
  }

  // Attach event listener to credit card form submission
  const creditCardFormElement = document.getElementById('credit-card-payment-form');
  if (creditCardFormElement) {
    creditCardFormElement.addEventListener('submit', function (event) {
      event.preventDefault(); // Prevent form submission
      processCreditCardPayment(); // Process credit card payment
    });
  }
}

// Initialize the payment page when the DOM is loaded
document.addEventListener('DOMContentLoaded', initializePaymentPage);