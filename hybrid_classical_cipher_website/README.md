# Hybrid Classical Cipher System

A modern web application that demonstrates a **Hybrid Encryption approach**, combining two classic cryptographic techniques: the **Caesar Cipher** and the **Playfair Cipher**. By layering these methods, the system provides enhanced security against simple frequency analysis and basic cryptanalysis.

## 🚀 Key Features

- **Double-Layer Encryption**: Processes text through Caesar substitution followed by Playfair digraph substitution.
- **Interactive Web Interface**: A clean, responsive UI built with vanilla JavaScript and CSS.
- **Hybrid Logic**:
    - **Encryption**: `Plaintext` → `Caesar Cipher` → `Intermediate Text` → `Playfair Cipher` → `Final Ciphertext`.
    - **Decryption**: `Ciphertext` → `Playfair Decryption` → `Intermediate Text` → `Caesar Decryption` → `Original Plaintext`.
- **Dynamic Visualization**: Highlights the Playfair 5x5 matrix used during the encryption/decryption process.
- **Deployment Ready**: Configured for seamless hosting on platforms like Vercel.

## 🛠️ Technology Stack

- **Backend**: Python, Flask, Flask-CORS
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Infrastructure**: Vercel (Serverless Functions)

## 📁 Project Structure

```text
├── backend/
│   ├── app.py          # Flask API entry point
│   ├── hybrid.py       # Core hybrid logic (orchestration)
│   ├── caesar.py       # Caesar cipher implementation
│   ├── playfair.py     # Playfair cipher implementation
├── frontend/
│   ├── index.html      # Landing page
│   ├── encrypt.html    # Encryption interface
│   ├── decrypt.html    # Decryption interface
│   ├── css/            # Stylesheets
│   ├── js/             # API integration and logic
├── vercel.json         # Deployment configuration
└── requirements.txt    # Python dependencies
```

## ⚙️ Setup & Installation

### Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/NAVEEN0701K/Hybrid-Classical-Encryption-and-Decryption-.git
   cd Hybrid-Classical-Encryption-and-Decryption-
   ```

2. **Set up the backend**:
   ```bash
   cd backend
   pip install -r ../requirements.txt
   python app.py
   ```
   *The backend will run on `http://localhost:5000`.*

3. **Open the frontend**:
   Open `frontend/index.html` in your web browser.

### Deployment (Vercel)

This project is pre-configured for Vercel. Simply connect your GitHub repository to Vercel.

> [!IMPORTANT]
> **Fixing the "Root Directory" Error**:
> During the Vercel setup, if you see an error about the **Root Directory**, follow these steps:
> 1. Go to your **Project Settings** in Vercel.
> 2. Find the **Root Directory** field.
> 3. **Clear the field completely** (remove `./` or any other text). It should be **left empty**.
> 4. Click **Save**.
> 5. Go to the **Deployments** tab and redeploy the latest commit.

Vercel will then automatically:
- Deploy the Python backend as serverless functions from the `/api` directory.
- Host the frontend files (now in the root) as static assets.
- Configure proper routing automatically.

## 🔒 Security Explanation

1. **Caesar Cipher (Substitution)**: Shifts each letter by a fixed value. While weak on its own, it serves as the first transformation layer.
2. **Playfair Cipher (Digraph Substitution)**: Encrypts pairs of letters using a 5x5 grid generated from a keyword. This creates a more complex ciphertext that hides single-letter frequency patterns.
3. **Hybrid Strength**: By combining both, we increase the keyspace and complexity, making it significantly harder to crack than either method individually.

## 📄 License

This project is open-source and available under the MIT License.
