function showActions(button, id) {
    // Remove any existing menus first
    document.querySelectorAll('.action-menu').forEach(m => m.remove());

    const actions = [
        { name: 'Approve', action: 'approve', color: '#28a745' },
        { name: 'Reject', action: 'reject', color: '#dc3545' },
        { name: 'Complete', action: 'complete', color: '#17a2b8' }
    ];

    const menu = document.createElement('div');
    menu.className = 'action-menu';
    menu.style.position = 'absolute';
    menu.style.backgroundColor = 'white';
    menu.style.boxShadow = '0 2px 5px rgba(0,0,0,0.2)';
    menu.style.borderRadius = '4px';
    menu.style.zIndex = '1000';
    menu.style.minWidth = '120px';

    actions.forEach(({ name, action, color }) => {
        const option = document.createElement('div');
        option.style.padding = '8px 12px';
        option.style.color = color;
        option.style.cursor = 'pointer';
        option.style.fontSize = '14px';
        option.textContent = name;
        option.onmouseover = () => option.style.backgroundColor = '#f8f9fa';
        option.onmouseout = () => option.style.backgroundColor = 'white';
        
        option.onclick = async (e) => {
            e.preventDefault();
            e.stopPropagation();
            
            try {
                const response = await fetch(`?action=${action}&id=${id}`);
                if (response.ok) {
                    // Refresh only the table content
                    location.reload();
                }
            } catch (error) {
                console.error('Error:', error);
            }
            
            menu.remove();
        };
        
        menu.appendChild(option);
    });

    // Position the menu
    const rect = button.getBoundingClientRect();
    menu.style.top = `${rect.bottom + window.scrollY}px`;
    menu.style.left = `${rect.left + window.scrollX}px`;

    document.body.appendChild(menu);

    // Handle clicks outside the menu
    function handleClickOutside(e) {
        if (!menu.contains(e.target) && e.target !== button) {
            menu.remove();
            document.removeEventListener('click', handleClickOutside);
        }
    }

    // Add click listener with a slight delay
    setTimeout(() => {
        document.addEventListener('click', handleClickOutside);
    }, 100);

    // Prevent the initial click from triggering the document click handler
    button.onclick = (e) => {
        e.stopPropagation();
    };
}