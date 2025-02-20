// Calendar click handler
document.querySelectorAll('.calendar .day:not(.day-header)').forEach(day => {
    day.addEventListener('click', function() {
        if (!day.classList.contains('disabled')) {
            document.getElementById('selected-date').textContent = `Day ${day.getAttribute('data-date')}`;
            let dropdownPanel = new bootstrap.Collapse(document.getElementById('dropdown-panel'), { toggle: true });
        }
    });
});

// Navbar scroll handler
window.addEventListener("scroll", function() {
    const navbar = document.querySelector(".navbar");
    if (window.scrollY > 0) {
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled");
    }
});