def caesar_cipher(text: str, shift: int, encrypt: bool = True) -> str:
    """
    Implements the Caesar cipher encryption and decryption.
    
    Args:
        text: The input text to process
        shift: The shift value (1-25)
        encrypt: If True, encrypt; if False, decrypt
        
    Returns:
        The processed text
    """
    if not text:
        return ""
        
    result = []
    shift = shift % 26  # Ensure shift is within 0-25
    
    for char in text.upper():
        if char.isalpha():
            # Shift character while maintaining case
            shift_amount = shift if encrypt else -shift
            code = ord(char) + shift_amount
            
            # Handle wrap-around for uppercase letters
            if char.isupper():
                if code > ord('Z'):
                    code -= 26
                elif code < ord('A'):
                    code += 26
            else:
                if code > ord('z'):
                    code -= 26
                elif code < ord('a'):
                    code += 26
                    
            result.append(chr(code))
        else:
            # Leave non-alphabetic characters as-is
            result.append(char)
            
    return ''.join(result)
