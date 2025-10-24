def prepare_text(text: str) -> str:
    """Prepare the input text for Playfair cipher processing."""
    # Convert to uppercase and remove non-alphabetic characters
    text = ''.join(c.upper() for c in text if c.isalpha())
    
    # Replace J with I (standard Playfair convention)
    text = text.replace('J', 'I')
    
    # Split into digraphs, adding X between double letters and at the end if needed
    i = 0
    while i < len(text) - 1:
        if text[i] == text[i+1]:
            text = text[:i+1] + 'X' + text[i+1:]
            i += 2  # Skip the X we just added
        else:
            i += 1
    
    # Add X if the length is odd
    if len(text) % 2 != 0:
        text += 'X'
        
    return text

def create_matrix(key: str) -> list:
    """Create the 5x5 Playfair matrix from the given key."""
    # Convert key to uppercase and remove duplicates
    key = key.upper().replace('J', 'I')
    key_chars = []
    for char in key:
        if char not in key_chars and char.isalpha():
            key_chars.append(char)
    
    # Add remaining alphabet letters (except J)
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # No J in Playfair
    for char in alphabet:
        if char not in key_chars:
            key_chars.append(char)
    
    # Create 5x5 matrix
    matrix = [key_chars[i*5:(i+1)*5] for i in range(5)]
    return matrix

def find_position(matrix: list, char: str) -> tuple:
    """Find the row and column of a character in the matrix."""
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return (i, j)
    return (-1, -1)  # Should not happen if input is prepared properly

def playfair_encrypt(plaintext: str, key: str) -> str:
    """Encrypt the plaintext using the Playfair cipher."""
    # Prepare the text and create the matrix
    text = prepare_text(plaintext)
    matrix = create_matrix(key)
    ciphertext = []
    
    # Process each digraph
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        
        # Same row
        if row1 == row2:
            ciphertext.append(matrix[row1][(col1 + 1) % 5])
            ciphertext.append(matrix[row2][(col2 + 1) % 5])
        # Same column
        elif col1 == col2:
            ciphertext.append(matrix[(row1 + 1) % 5][col1])
            ciphertext.append(matrix[(row2 + 1) % 5][col2])
        # Rectangle
        else:
            ciphertext.append(matrix[row1][col2])
            ciphertext.append(matrix[row2][col1])
    
    return ''.join(ciphertext)

def playfair_decrypt(ciphertext: str, key: str) -> str:
    """Decrypt the ciphertext using the Playfair cipher."""
    # Prepare the text and create the matrix
    text = prepare_text(ciphertext)
    matrix = create_matrix(key)
    plaintext = []
    
    # Process each digraph
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        
        # Same row
        if row1 == row2:
            plaintext.append(matrix[row1][(col1 - 1) % 5])
            plaintext.append(matrix[row2][(col2 - 1) % 5])
        # Same column
        elif col1 == col2:
            plaintext.append(matrix[(row1 - 1) % 5][col1])
            plaintext.append(matrix[(row2 - 1) % 5][col2])
        # Rectangle
        else:
            plaintext.append(matrix[row1][col2])
            plaintext.append(matrix[row2][col1])
    
    # Remove any trailing X and handle potential padding
    result = ''.join(plaintext)
    if len(result) > 0 and result[-1] == 'X':
        result = result[:-1]
    return result
