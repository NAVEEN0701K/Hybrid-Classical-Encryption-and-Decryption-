// API base URL - update this if your backend is hosted elsewhere
const API_BASE_URL = 'http://localhost:5000/api';

/**
 * Encrypt a message using the hybrid cipher
 * @param {string} message - The message to encrypt
 * @param {number} caesarShift - The shift value for Caesar cipher (1-25)
 * @param {string} playfairKey - The key for Playfair cipher
 * @returns {Promise<Object>} The encryption results
 */
async function encrypt(message, caesarShift, playfairKey) {
    try {
        const response = await fetch(`${API_BASE_URL}/encrypt`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                text: message,
                caesar_shift: parseInt(caesarShift),
                playfair_key: playfairKey
            })
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Encryption failed');
        }

        return await response.json();
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
}

/**
 * Decrypt a message using the hybrid cipher
 * @param {string} ciphertext - The ciphertext to decrypt
 * @param {number} caesarShift - The shift value for Caesar cipher (1-25)
 * @param {string} playfairKey - The key for Playfair cipher
 * @returns {Promise<Object>} The decryption results
 */
async function decrypt(ciphertext, caesarShift, playfairKey) {
    try {
        const response = await fetch(`${API_BASE_URL}/decrypt`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                ciphertext: ciphertext,
                caesar_shift: parseInt(caesarShift),
                playfair_key: playfairKey
            })
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error || 'Decryption failed');
        }

        return await response.json();
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
}

// Export functions for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { encrypt, decrypt };
}
