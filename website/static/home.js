function deleteStudent(element, id) {
    var closestForm = document.getElementById("deleteStudent_" + id);

    closestForm.submit();
  }

  function endSession(event) {
    // Prevent the default form submission
    event.preventDefault();

    // Show confirmation dialog
    const userConfirmed = confirm("Are you sure you want to end the session?");
    if (userConfirmed) {
        // If user clicks "Yes", submit the form
        document.getElementById('endSessionForm').submit();
    } else {
        // If user clicks "No", do nothing
        alert('Session end canceled.');
    }
}