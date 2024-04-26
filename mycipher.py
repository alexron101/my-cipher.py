import sys

def cipher(message, shift):
    encrypted_message = ''
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_char = chr((ord(char) - 97 + shift) % 26 + 65)
            encrypted_message += encrypted_char

    return encrypted_message

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 mycipher.py <shift>")
        sys.exit(1)

    shift = int(sys.argv[1])

    message = input().upper()

    encoded_message = ''
    for char in message:
        if char.isalpha():
            encoded_message += cipher(char, shift)

    count = 0
    for char in encoded_message:
        print(char, end='')
        count += 1
        if count == 5:
            print(' ', end='')
            count = 0

if __name__ == "__main__":
    main()
