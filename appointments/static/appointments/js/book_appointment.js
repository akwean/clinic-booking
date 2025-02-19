

// Navbar scroll handler
window.addEventListener("scroll", function() {
    const navbar = document.querySelector(".navbar");
    if (window.scrollY > 0) {
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled");
    }
});

// for confirmation
function showConfirmationModal() {
    var form = document.getElementById('appointment-form');
    var formData = new FormData(form);
    var confirmationDetails = document.getElementById('confirmationDetails');
    var selectedDate = document.getElementById('selected-date').textContent;
    confirmationDetails.innerHTML = '';

    // First add the selected date
    confirmationDetails.innerHTML = `<p><strong>Appointment Date:</strong> ${selectedDate}</p>`;

    // Then add other form fields
    formData.forEach(function(value, key) {
        // Skip csrf token, selected_date, and date fields
        if (key !== 'csrfmiddlewaretoken' && 
            key !== 'selected_date' && 
            key !== 'date') {
            const formattedKey = key.replace(/_/g, ' ').replace(/\b\w/g, char => char.toUpperCase());
            confirmationDetails.innerHTML += `<p><strong>${formattedKey}:</strong> ${value}</p>`;
        }
    });

    var modal = document.getElementById('confirmationModal');
    modal.style.display = 'block';
}

function closeConfirmationModal() {
    var modal = document.getElementById('confirmationModal');
    modal.style.display = 'none';
}

function confirmAppointment() {
    var form = document.getElementById('appointment-form');
    var selectedDateElement = document.getElementById('selected_date');
    var selectedDateText = document.getElementById('selected-date').textContent;
    
    // Debug logs
    console.log('Selected date text:', selectedDateText);
    console.log('Current selected_date value:', selectedDateElement.value);
    
    // Extract the date from the text (e.g., "February 18, 2025" -> "2025-02-18")
    var dateParts = selectedDateText.match(/February (\d+), 2025/);
    if (dateParts) {
        var day = dateParts[1].padStart(2, '0');
        var formattedDate = `2025-02-${day}`;
        
        // Set both the hidden input and the date field
        selectedDateElement.value = formattedDate;
        document.querySelector('input[name="date"]').value = formattedDate;
        
        console.log('Submitting form with date:', formattedDate);
        form.submit();
    } else {
        console.error('Invalid date format');
    }
}
// Update the calendar click handler
document.querySelectorAll('.calendar .day:not(.day-header)').forEach(day => {
    day.addEventListener('click', function() {
        if (!day.classList.contains('disabled')) {
            const date = day.getAttribute('data-date');
            const selectedDate = `2025-02-${date.padStart(2, '0')}`;
            document.getElementById('selected-date').textContent = `February ${date}, 2025`;
            document.getElementById('selected_date').value = selectedDate;
            let dropdownPanel = new bootstrap.Collapse(document.getElementById('dropdown-panel'), { toggle: true });
        }
    });
});