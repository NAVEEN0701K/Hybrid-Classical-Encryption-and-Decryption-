from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from .caesar import caesar_cipher
from .playfair import playfair_encrypt, playfair_decrypt, create_matrix
from .hybrid import hybrid_encrypt, hybrid_decrypt

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return "Hybrid Classical Cipher API is running!"

@app.route('/api/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    
    if not data or 'text' not in data or 'caesar_shift' not in data or 'playfair_key' not in data:
        return jsonify({'error': 'Missing required parameters'}), 400
    
    try:
        text = data['text']
        caesar_shift = int(data['caesar_shift'])
        playfair_key = data['playfair_key']
        
        # Validate inputs
        if not playfair_key or not playfair_key.strip():
            return jsonify({'error': 'Playfair key cannot be empty'}), 400
            
        if not isinstance(caesar_shift, int) or caesar_shift < 1 or caesar_shift > 25:
            return jsonify({'error': 'Caesar shift must be an integer between 1 and 25'}), 400
        
        # Perform hybrid encryption
        caesar_result, final_ciphertext = hybrid_encrypt(text, caesar_shift, playfair_key)
        
        # Get the Playfair matrix for visualization
        matrix = create_matrix(playfair_key)
        
        return jsonify({
            'status': 'success',
            'caesar_result': caesar_result,
            'ciphertext': final_ciphertext,
            'playfair_matrix': matrix
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    
    if not data or 'ciphertext' not in data or 'caesar_shift' not in data or 'playfair_key' not in data:
        return jsonify({'error': 'Missing required parameters'}), 400
    
    try:
        ciphertext = data['ciphertext']
        caesar_shift = int(data['caesar_shift'])
        playfair_key = data['playfair_key']
        
        # Validate inputs
        if not playfair_key or not playfair_key.strip():
            return jsonify({'error': 'Playfair key cannot be empty'}), 400
            
        if not isinstance(caesar_shift, int) or caesar_shift < 1 or caesar_shift > 25:
            return jsonify({'error': 'Caesar shift must be an integer between 1 and 25'}), 400
        
        # Perform hybrid decryption
        playfair_result, final_plaintext = hybrid_decrypt(ciphertext, caesar_shift, playfair_key)
        
        # Get the Playfair matrix for visualization
        matrix = create_matrix(playfair_key)
        
        return jsonify({
            'status': 'success',
            'playfair_result': playfair_result,
            'plaintext': final_plaintext,
            'playfair_matrix': matrix
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
