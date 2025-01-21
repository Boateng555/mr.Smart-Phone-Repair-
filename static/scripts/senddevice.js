// JavaScript, um das Reparatur-Formular anzuzeigen/verbergen
document.getElementById("start-repair").addEventListener("click", function() {
  document.querySelector(".overview").classList.add("hidden");
  document.getElementById("repair-form").classList.remove("hidden");
});

document.getElementById("repairForm").addEventListener("submit", function(event) {
  event.preventDefault();
  alert("Reparaturanfrage gesendet! Wir werden uns bald bei Ihnen melden.");
  // Optional: Hier könnte die Formularübermittlung an den Server erfolgen
  document.getElementById("repairForm").reset();
});