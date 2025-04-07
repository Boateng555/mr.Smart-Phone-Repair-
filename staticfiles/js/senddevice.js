document.getElementById("repairForm").addEventListener("submit", function(event) {
  event.preventDefault();
  console.log("Form submission intercepted.");

  // Show the modal
  var myModal = new bootstrap.Modal(document.getElementById('successModal'), {
    keyboard: false
  });
  myModal.show();
  console.log("Modal shown.");

  // Submit the form data to the server
  const formData = new FormData(document.getElementById("repairForm"));
  console.log("Form data:", formData);

  fetch(submitRepairRequestUrl, {  // Use the URL passed from the template
    method: "POST",
    body: formData,
    headers: {
      "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
    },
  })
  .then(response => {
    console.log("Response received:", response);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  })
  .then(data => {
    console.log("Response data:", data);
    if (data.success) {
      console.log("Form submitted successfully!");
    } else {
      console.error("Form submission failed:", data.error);
    }
  })
  .catch(error => {
    console.error("Error:", error);
  });

  // Optionally, you can reset the form after submission
  document.getElementById("repairForm").reset();
  console.log("Form reset.");
});