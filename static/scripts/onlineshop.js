console.log("onlineshop.js is loaded!");

// Search functionality
function filterProducts() {
  console.log("filterProducts() called!"); // Debugging: Check if the function is called

  const searchInput = document.getElementById('search-input').value.toLowerCase();
  const productItems = document.querySelectorAll('.product-item');

  console.log("Search input:", searchInput); // Debugging: Check the search input value
  console.log("Number of products:", productItems.length); // Debugging: Check the number of products

  productItems.forEach(item => {
    const productName = item.querySelector('.item-name h3').textContent.toLowerCase();
    console.log("Product name:", productName); // Debugging: Check each product name

    if (productName.includes(searchInput)) {
      item.style.display = 'block'; // Show the product
    } else {
      item.style.display = 'none'; // Hide the product
    }
  });
}