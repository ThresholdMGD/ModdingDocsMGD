document.addEventListener("DOMContentLoaded", function() {
    const toggles = document.querySelectorAll('.md-nav__toggle');

    toggles.forEach(toggle => {
        toggle.addEventListener('change', function() {
            // Only process when opening a toggle
            if (this.checked) {
                const currentNavItem = toggle.closest('.md-nav__item');
                const currentParentNav = currentNavItem ? currentNavItem.parentElement : null;
                
                toggles.forEach(otherToggle => {
                    if (otherToggle !== toggle) {
                        const otherNavItem = otherToggle.closest('.md-nav__item');
                        const otherParentNav = otherNavItem ? otherNavItem.parentElement : null;
                        
                        // Only close toggles that are siblings (same direct parent)
                        // Don't close parent or child toggles
                        if (currentParentNav && otherParentNav && 
                            currentParentNav === otherParentNav && 
                            !currentNavItem.contains(otherNavItem) && 
                            !otherNavItem.contains(currentNavItem)) {
                            otherToggle.checked = false;
                        }
                    }
                });
            }
        });
    });
});