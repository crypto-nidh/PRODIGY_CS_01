import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def banner():
    print("=" * 50)
    print("       🔐 Caesar Cipher Encryption Tool 🔐       ")
    print("=" * 50)


def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char  # Non-alphabetic characters stay the same

    return result


def get_shift_value():
    while True:
        try:
            shift = int(input("🔁 Enter shift value (0-25): "))
            if 0 <= shift <= 25:
                return shift
            else:
                print("⚠️  Please enter a number between 0 and 25.")
        except ValueError:
            print("⚠️  Invalid input. Please enter a number.")


def main_menu():
    while True:
        clear_screen()
        banner()
        print("1️⃣  Encrypt a message")
        print("2️⃣  Decrypt a message")
        print("3️⃣  Exit")
        choice = input("\nChoose an option (1-3): ").strip()

        if choice == '1':
            clear_screen()
            banner()
            msg = input("📝 Enter your message to encrypt: ")
            shift = get_shift_value()
            encrypted = caesar_cipher(msg, shift, 'encrypt')
            print(f"\n🔒 Encrypted Message: {encrypted}")
            input("\nPress Enter to return to menu...")

        elif choice == '2':
            clear_screen()
            banner()
            msg = input("📝 Enter your message to decrypt: ")
            shift = get_shift_value()
            decrypted = caesar_cipher(msg, shift, 'decrypt')
            print(f"\n🔓 Decrypted Message: {decrypted}")
            input("\nPress Enter to return to menu...")

        elif choice == '3':
            print("\n👋 Exiting Caesar Cipher Tool. Stay secure!")
            sys.exit()

        else:
            print("⚠️  Invalid choice! Please choose from 1, 2, or 3.")
            input("\nPress Enter to try again...")


if __name__ == "__main__":
    main_menu()
