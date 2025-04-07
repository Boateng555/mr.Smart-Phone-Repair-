let MenuItems = document.getElementById("MenuItems");

MenuItems.style.maxHeight = "0px"

function menutoggle(){
  if(MenuItems.style.maxHeight == "0px")
      {
        MenuItems.style.maxHeight = "200px"
      }
  else
      {
        MenuItems.style.maxHeight = "0px"
      }
} 

document.addEventListener("DOMContentLoaded", function () {
  // Image slideshow
  const images = document.querySelectorAll('.slideshow img');
  let currentImageIndex = 0;
  
  function changeImage() {
      images[currentImageIndex].classList.remove('active');
      currentImageIndex = (currentImageIndex + 1) % images.length;
      images[currentImageIndex].classList.add('active');
  }
  
  // Start slideshow if images exist
  if(images.length > 0) {
      setInterval(changeImage, 5000);
  }

  // Keep your existing menu toggle code
  let MenuItems = document.getElementById("MenuItems");
  MenuItems.style.maxHeight = "0px";
  
  function menutoggle(){
      if(MenuItems.style.maxHeight == "0px") {
          MenuItems.style.maxHeight = "200px";
      } else {
          MenuItems.style.maxHeight = "0px";
      }
  }
});