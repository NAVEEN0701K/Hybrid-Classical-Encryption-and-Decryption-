/**
 * Main JavaScript for Hybrid Classical Cipher
 * Handles UI interactions and initializations
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    initializeTooltips();
    
    // Initialize any other UI components
    initializeUI();
    
    // Set up event listeners
    setupEventListeners();
});

/**
 * Initialize tooltips using the browser's built-in title attribute
 */
function initializeTooltips() {
    // This is a simple implementation using the title attribute
    // For more advanced tooltips, consider using a library like Tippy.js
    const tooltipElements = document.querySelectorAll('[data-tooltip]');
    
    tooltipElements.forEach(element => {
        const tooltipText = element.getAttribute('data-tooltip');
        if (tooltipText) {
            element.setAttribute('title', tooltipText);
        }
    });
}

/**
 * Initialize UI components
 */
function initializeUI() {
    // Set current year in footer
    const yearElement = document.getElementById('current-year');
    if (yearElement) {
        yearElement.textContent = new Date().getFullYear();
    }
    
    // Initialize any other UI components here
}

/**
 * Set up event listeners
 */
function setupEventListeners() {
    // Copy buttons functionality
    document.querySelectorAll('.btn-copy').forEach(button => {
        button.addEventListener('click', function() {
            const targetId = this.getAttribute('data-copy-target');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                // Select the text
                const range = document.createRange();
                range.selectNode(targetElement);
                window.getSelection().removeAllRanges();
                window.getSelection().addRange(range);
                
                try {
                    // Copy the text
                    document.execCommand('copy');
                    
                    // Show feedback
                    const originalText = this.textContent;
                    this.textContent = 'Copied!';
                    
                    // Revert button text after a delay
                    setTimeout(() => {
                        this.textContent = originalText;
                    }, 2000);
                } catch (err) {
                    console.error('Failed to copy text: ', err);
                }
                
                // Clear selection
                window.getSelection().removeAllRanges();
            }
        });
    });
    
    // Clear buttons functionality
    document.querySelectorAll('.btn-clear').forEach(button => {
        button.addEventListener('click', function() {
            const targetId = this.getAttribute('data-clear-target');
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                targetElement.value = '';
                targetElement.textContent = '';
            }
        });
    });
    
    // Auto-resize textareas
    document.querySelectorAll('textarea').forEach(textarea => {
        textarea.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = (this.scrollHeight) + 'px';
        });
    });
}

/**
 * Show a notification message
 * @param {string} message - The message to display
 * @param {string} type - The type of notification (success, error, info, warning)
 * @param {number} duration - How long to show the notification in milliseconds
 */
function showNotification(message, type = 'info', duration = 3000) {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification ${type}`;
    notification.textContent = message;
    
    // Add to the notifications container or create one if it doesn't exist
    let container = document.getElementById('notifications');
    if (!container) {
        container = document.createElement('div');
        container.id = 'notifications';
        document.body.appendChild(container);
    }
    
    // Add the notification to the container
    container.appendChild(notification);
    
    // Show the notification
    setTimeout(() => {
        notification.classList.add('show');
    }, 10);
    
    // Remove the notification after the specified duration
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, duration);
}

/**
 * Toggle password visibility
 * @param {string} inputId - The ID of the password input
 * @param {string} buttonId - The ID of the toggle button
 */
function togglePasswordVisibility(inputId, buttonId) {
    const input = document.getElementById(inputId);
    const button = document.getElementById(buttonId);
    
    if (input && button) {
        if (input.type === 'password') {
            input.type = 'text';
            button.textContent = 'Hide';
            button.setAttribute('aria-label', 'Hide password');
        } else {
            input.type = 'password';
            button.textContent = 'Show';
            button.setAttribute('aria-label', 'Show password');
        }
    }
}

// Export functions for testing or if using modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        initializeTooltips,
        initializeUI,
        setupEventListeners,
        showNotification,
        togglePasswordVisibility
    };
}
