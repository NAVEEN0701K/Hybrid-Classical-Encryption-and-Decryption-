# Hybrid Classical Cipher

A web application that demonstrates a hybrid encryption system combining the Caesar and Playfair ciphers for enhanced security.

## Features

- **Caesar Cipher**: A simple substitution cipher that shifts letters by a fixed number of positions.
- **Playfair Cipher**: A digraph substitution cipher that encrypts pairs of letters.
- **Hybrid Encryption**: Combines both ciphers for stronger security.
- **Interactive UI**: User-friendly interface for encryption and decryption.
- **Visualization**: Displays the Playfair matrix and highlights the encryption/decryption process.

## Prerequisites

- Python 3.7+
- pip (Python package manager)
- Modern web browser

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hybrid-classical-cipher.git
   cd hybrid-classical-cipher
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Flask backend server:
   ```bash
   cd backend
   python app.py
   ```

2. Open the `frontend/index.html` file in a web browser, or use a local web server:
   ```bash
   # Using Python's built-in HTTP server (run from the frontend directory)
   cd frontend
   python -m http.server 8000
   ```
   Then open `http://localhost:8000` in your browser.

## How to Use

### Encryption
1. Go to the "Encrypt" page
2. Enter your message in the text area
3. Set a Caesar shift value (1-25)
4. Enter a keyword for the Playfair cipher
5. Click "Encrypt" to see the results

### Decryption
1. Go to the "Decrypt" page
2. Paste the ciphertext in the text area
3. Enter the original Caesar shift value
4. Enter the original Playfair key
5. Click "Decrypt" to see the original message

## Project Structure

```
hybrid_classical_cipher_website/
├── backend/               # Server-side code
│   ├── app.py            # Flask application
│   ├── caesar.py         # Caesar cipher implementation
│   ├── playfair.py       # Playfair cipher implementation
│   ├── hybrid.py         # Hybrid cipher implementation
│   └── utils.py          # Utility functions
├── frontend/             # Client-side code
│   ├── index.html        # Home page
│   ├── encrypt.html      # Encryption page
│   ├── decrypt.html      # Decryption page
│   ├── about.html        # About page
│   ├── css/
│   │   └── style.css     # Styles
│   └── js/
│       ├── main.js       # Main JavaScript
│       ├── api.js        # API interactions
│       └── visualization.js # Matrix visualization
└── README.md             # This file
```

## Security Considerations

- This implementation is for educational purposes only and should not be used for securing sensitive information.
- The hybrid approach provides better security than either cipher alone but is still vulnerable to modern cryptanalysis techniques.
- For real-world applications, use established cryptographic libraries and algorithms like AES.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)
- [Playfair Cipher](https://en.wikipedia.org/wiki/Playfair_cipher)
- [Flask](https://flask.palletsprojects.com/)
- [MDN Web Docs](https://developer.mozilla.org/)
