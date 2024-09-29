import getpass

print("------------ Welcome to the Caesar Cipher Program ------------")
print("")

def message_analysis(msg):
    letter_count = sum(char.isalpha() for char in msg)
    digit_count = sum(char.isdigit() for char in msg)
    special_count = len(msg) - letter_count - digit_count

    print("Analyze the input message with the following details:")
    print(f"\nFirst and last characters: {msg[:1]}***{msg[-1]}")
    print(f"Total characters: {len(msg)}")
    print(f"Letters: {letter_count}")
    print(f"Digits: {digit_count}")
    
    if special_count > 0:
        print(f"Special characters count: {special_count}")
        print("The message contains special characters.")
    else:
        print("There are no special characters in the message.")

def perform_caesar(text, shift_value, mode):
    output = ""
    for character in text:
        if character.isalpha():
            alphabet_start = ord('a') if character.islower() else ord('A')
            if mode == 'e':
                new_char = chr((ord(character) - alphabet_start + shift_value) % 26 + alphabet_start)
            elif mode == 'd':
                new_char = chr((ord(character) - alphabet_start - shift_value) % 26 + alphabet_start)
            else:
                raise ValueError("Invalid option. Choose 'e' for encryption or 'd' for decryption.")
            output += new_char
        else:
            output += character
    return output

def main():
    while True:
        user_choice = input("Do you want to (e)ncrypt, (d)ecrypt a message, or (q)uit?: ").lower()
        if user_choice == 'q':
            print("Thanks for using the tool! Goodbye.")
            return
        elif user_choice in ['e', 'd']:
            break
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q' to exit.")

    if user_choice == 'q':
        return

    user_message = getpass.getpass(prompt="Please type your message (hidden input): ")

    if user_choice != 'q':
        message_analysis(user_message)

        shift_value = int(getpass.getpass(prompt="Enter the shift amount (hidden input): "))

        if user_choice == 'e':
            encrypted_message = perform_caesar(user_message, shift_value, 'e')
            print("\nEncrypted message:", encrypted_message)
        elif user_choice == 'd':
            decrypted_message = perform_caesar(user_message, shift_value, 'd')
            print("\nDecrypted message:", decrypted_message)

if __name__ == "__main__":
    main()
