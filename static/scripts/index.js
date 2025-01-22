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


// Add touch support for dropdowns
// document.querySelectorAll("nav ul li").forEach((item) => {
//     item.addEventListener("touchstart", function () {
//       const dropdown = this.querySelector(".dropdown");
//       if (dropdown) {
//         dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
//       }
//     });
//   });
  
 




  document.querySelectorAll("nav ul li").forEach((item) => {
    item.addEventListener("mouseenter", function () {
      const dropdown = this.querySelector(".dropdown");
      if (dropdown) {
        dropdown.style.display = "block";
      }
    });
  
    item.addEventListener("mouseleave", function () {
      const dropdown = this.querySelector(".dropdown");
      if (dropdown) {
        dropdown.style.display = "none";
      }
    });
  
    // Support touch devices
    item.addEventListener("touchstart", function () {
      const dropdown = this.querySelector(".dropdown");
      if (dropdown) {
        dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
      }
    });
  });
  
