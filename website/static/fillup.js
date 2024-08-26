document.addEventListener('DOMContentLoaded', function () {
    // Get references to the form and the table body
    const form = document.getElementById('attendance-form');
    const tableBody = document.getElementById('table-body');

    // Handle form submission
    document.getElementById('save-attendance').addEventListener('click', function () {
        // Get form values
        const studentId = document.getElementById('student-id').value;
        const firstName = document.getElementById('first-name').value;
        const lastName = document.getElementById('last-name').value;
        const section = document.getElementById('section').value;
        const attendance = document.querySelector('input[name="attendance"]:checked').value;

        // Check if all fields are filled
        if (studentId && firstName && lastName && section && attendance) {
            // Create a new table row
            const newRow = document.createElement('tr');
            newRow.innerHTML = `
                <td>${studentId}</td>
                <td>${firstName}</td>
                <td>${lastName}</td>
                <td>Section ${section}</td>
                <td>example@example.com</td> <!-- Placeholder for email -->
                <td>${attendance === 'Present' ? '<input type="radio" name="attendance' + studentId + '" value="Present" checked>' : '<input type="radio" name="attendance' + studentId + '" value="Present">'}</td>
                <td>${attendance === 'Absent' ? '<input type="radio" name="attendance' + studentId + '" value="Absent" checked>' : '<input type="radio" name="attendance' + studentId + '" value="Absent">'}</td>
            `;

            // Append the new row to the table
            tableBody.appendChild(newRow);

            // Reset the form and close the modal
            form.reset();
            const modal = bootstrap.Modal.getInstance(document.getElementById('mymodal'));
            modal.hide();
        } else {
            alert('Please fill out all fields.');
        }
    });
});