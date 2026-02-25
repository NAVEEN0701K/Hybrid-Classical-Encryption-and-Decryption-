from .caesar import caesar_cipher
from .playfair import playfair_encrypt, playfair_decrypt

def hybrid_encrypt(plaintext: str, caesar_shift: int, playfair_key: str) -> tuple[str, str]:
    """
    Encrypt the plaintext using a hybrid of Caesar and Playfair ciphers.
    
    Args:
        plaintext: The text to encrypt
        caesar_shift: The shift value for the Caesar cipher (1-25)
        playfair_key: The key for the Playfair cipher
        
    Returns:
        A tuple containing (caesar_result, final_ciphertext)
    """
    # First, apply Caesar cipher
    caesar_result = caesar_cipher(plaintext, caesar_shift, encrypt=True)
    
    # Then, apply Playfair cipher to the result
    final_ciphertext = playfair_encrypt(caesar_result, playfair_key)
    
    return caesar_result, final_ciphertext

def hybrid_decrypt(ciphertext: str, caesar_shift: int, playfair_key: str) -> tuple[str, str]:
    """
    Decrypt the ciphertext using the hybrid of Caesar and Playfair ciphers.
    
    Args:
        ciphertext: The text to decrypt
        caesar_shift: The shift value for the Caesar cipher (1-25)
        playfair_key: The key for the Playfair cipher
        
    Returns:
        A tuple containing (playfair_result, final_plaintext)
    """
    # First, decrypt Playfair
    playfair_result = playfair_decrypt(ciphertext, playfair_key)
    
    # Then, decrypt Caesar
    final_plaintext = caesar_cipher(playfair_result, caesar_shift, encrypt=False)
    
    return playfair_result, final_plaintext
