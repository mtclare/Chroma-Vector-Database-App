// Additional JavaScript functionality for Email Vector Database

// Utility functions
const utils = {
    // Show notification
    showNotification: function(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `fixed top-4 right-4 p-4 rounded-md shadow-lg z-50 ${
            type === 'error' ? 'bg-red-500 text-white' : 
            type === 'success' ? 'bg-green-500 text-white' : 
            'bg-blue-500 text-white'
        }`;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        // Auto-remove after 3 seconds
        setTimeout(() => {
            notification.remove();
        }, 3000);
    },
    
    // Format date
    formatDate: function(dateString) {
        const date = new Date(dateString);
        return date.toLocaleDateString() + ' ' + date.toLocaleTimeString();
    },
    
    // Debounce function
    debounce: function(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
};

// Enhanced form validation
function validateEmailForm() {
    const subject = document.getElementById('subject').value.trim();
    const sender = document.getElementById('sender').value.trim();
    const recipient = document.getElementById('recipient').value.trim();
    const content = document.getElementById('content').value.trim();
    
    if (!subject || !sender || !recipient || !content) {
        utils.showNotification('Please fill in all required fields', 'error');
        return false;
    }
    
    // Basic email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(sender) || !emailRegex.test(recipient)) {
        utils.showNotification('Please enter valid email addresses', 'error');
        return false;
    }
    
    return true;
}

// Enhanced search with debouncing
const debouncedSearch = utils.debounce(async function(query) {
    if (query.length < 2) return;
    
    // This could be used for real-time search suggestions
    console.log('Searching for:', query);
}, 300);

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    console.log('Email Vector Database initialized');
    
    // Add enhanced validation to forms
    const addEmailForm = document.getElementById('addEmailForm');
    if (addEmailForm) {
        addEmailForm.addEventListener('submit', function(e) {
            if (!validateEmailForm()) {
                e.preventDefault();
            }
        });
    }
    
    // Add real-time search input handling
    const searchInput = document.getElementById('searchQuery');
    if (searchInput) {
        searchInput.addEventListener('input', function(e) {
            debouncedSearch(e.target.value);
        });
    }
});

// Export for use in other scripts
window.EmailVectorDB = {
    utils: utils,
    validateEmailForm: validateEmailForm
}; 