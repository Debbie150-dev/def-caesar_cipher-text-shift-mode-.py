def caesar_cipher(text, shift, mode):
  """
  Encrypts or decrypts text using Caesar Cipher algorithm.

  Args:
      text: The text to encrypt or decrypt.
      shift: The number of positions to shift letters (positive for encryption, negative for decryption).
      mode: 'encrypt' or 'decrypt'

  Returns:
      The encrypted or decrypted text.
  """
  alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  new_text = ''
  for char in text:
    if char not in alphabet:
      # Keep non-alphabetic characters unchanged
      new_text += char
      continue
    new_pos = (alphabet.index(char) + shift) % 26
    new_text += alphabet[new_pos]
  return new_text

def main():
  """
  Prompts user for input and performs encryption or decryption.
  """
  while True:
    print("Caesar Cipher")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    choice = input("1 ")

    if choice == '1':
      text = input("Top Secret! Meet me at the hidden library tomorrow at noon. Bring the book with the red spine!")
      shift = int(input("5"))
      encrypted_text = caesar_cipher(text, shift, 'encrypt')
      print("Encrypted message:", encrypted_text)
    elif choice == '2':
      text = input("Enter message to decrypt: ")
      shift = int(input("Enter shift value (positive integer): "))
      decrypted_text = caesar_cipher(text, -shift, 'decrypt')  # Use negative shift for decryption
      print("Decrypted message:", decrypted_text)
    elif choice == '3':
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()
1
