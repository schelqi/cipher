# Simple Substitution Ciphers
# Replace each character in the text by another one

MAIN_CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
SUBSTITUTION_CHARACTERS = "TIMEODANSFRBCGHJKLPQUVWXYZ"


def encrypt(content):
    encrypted_text = str()
    text = content.upper()
    for c in text:
        try:
            c_position = MAIN_CHARACTERS.index(c, 0, len(MAIN_CHARACTERS))
            encrypted_text += SUBSTITUTION_CHARACTERS[c_position]
        except ValueError:
            return None
    return encrypted_text


def decrypt(content):
    decrypted_text = str()
    text = content.upper()
    for c in text:
        try:
            c_position = SUBSTITUTION_CHARACTERS.index(c, 0, len(SUBSTITUTION_CHARACTERS))
            decrypted_text += MAIN_CHARACTERS[c_position]
        except ValueError:
            return None
    return decrypted_text


print(encrypt("hello"))
print(decrypt(encrypt("hello")))
