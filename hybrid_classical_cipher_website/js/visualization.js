/**
 * Display the Playfair matrix in the specified container
 * @param {Array<Array<string>>} matrix - The 5x5 Playfair matrix
 * @param {string} containerId - The ID of the container element
 */
function displayPlayfairMatrix(matrix, containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    // Clear previous content
    container.innerHTML = '';

    // Create table element
    const table = document.createElement('div');
    table.className = 'matrix';

    // Create matrix cells
    for (let i = 0; i < 5; i++) {
        for (let j = 0; j < 5; j++) {
            const cell = document.createElement('div');
            cell.className = 'matrix-cell';
            cell.textContent = matrix[i][j];
            cell.setAttribute('data-row', i);
            cell.setAttribute('data-col', j);
            table.appendChild(cell);
        }
    }

    // Add the table to the container
    container.appendChild(table);
}

/**
 * Highlight cells in the Playfair matrix
 * @param {string} containerId - The ID of the matrix container
 * @param {Array<{row: number, col: number}>} cells - Array of cell positions to highlight
 * @param {string} [colorClass='highlight'] - CSS class for highlighting
 */
function highlightCells(containerId, cells, colorClass = 'highlight') {
    const container = document.getElementById(containerId);
    if (!container) return;

    // Remove previous highlights
    const previousHighlights = container.querySelectorAll(`.${colorClass}`);
    previousHighlights.forEach(el => el.classList.remove(colorClass));

    // Add new highlights
    cells.forEach(pos => {
        const selector = `.matrix-cell[data-row="${pos.row}"][data-col="${pos.col}"]`;
        const cell = container.querySelector(selector);
        if (cell) {
            cell.classList.add(colorClass);
        }
    });
}

/**
 * Animate the encryption/decryption process
 * @param {string} containerId - The ID of the matrix container
 * @param {Array} steps - Array of steps to animate
 * @param {number} [delay=1000] - Delay between steps in milliseconds
 */
function animateProcess(containerId, steps, delay = 1000) {
    let index = 0;
    
    function nextStep() {
        if (index >= steps.length) return;
        
        const step = steps[index];
        highlightCells(containerId, step.cells, step.type || 'highlight');
        
        // Optional: Update a status element if it exists
        const statusElement = document.getElementById('animation-status');
        if (statusElement) {
            statusElement.textContent = step.description || '';
        }
        
        index++;
        setTimeout(nextStep, delay);
    }
    
    nextStep();
}

// Export functions for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        displayPlayfairMatrix,
        highlightCells,
        animateProcess
    };
}
