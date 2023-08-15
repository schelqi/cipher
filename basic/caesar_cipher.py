# Caesar Cipher
# Replace each character in the text by another one

moves = 3
edge = ord('z')


def encrypt(content):
    encrypted_text = str()
    text = content.lower()

    for c in text:
        c_position = (ord(c) + moves) % edge
        encrypted_text += chr(c_position)

    return encrypted_text


def decrypt(content):
    decrypted_text = str()
    text = content.lower()
    for c in text:
        c_position = (ord(c) - moves) % edge
        decrypted_text += chr(c_position)

    return decrypted_text


print(encrypt("hello"))
print(decrypt(encrypt("hello")))
