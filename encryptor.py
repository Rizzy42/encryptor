# Disables either unimportant, irrelevant, or out of context pylint errors
# pylint: disable=C0301, W0703, C0114, C0116, R0912, R0915
# This main program brings all the components together and does the actual heavy work of encryption

# Initialises colorama to convert ANSI codes to win32 so that the display correctly on Windows
from colorama import init as colorama_init

from utils.files import importLines, writeLines

# Interface programs
from interface.welcome import welcomeMsg
from interface.user_options.input_source import getInputSource
from interface.user_options.crypt_option import getCryptOption
from interface.user_options.cipher_option import getCipherOption
from interface.user_options.save_option import getSaveOption

# Interface Utilities
from interface.interactions.options import getInteger
from interface.interactions.text import prefixedPrompt, newline, returnPrefixedText

# Styles
from styles.colorama_fore import red, yellow, cyan
from styles.colorama_style import main_style, option_style

# Ciphers
from ciphers.caesar import CaesarCipherInstance
from ciphers.atbash import AtbashCipherInstance

colorama_init()

def main():
    # All the abstraction paid off, this looks great!
    welcomeMsg()

    user_source_option = getInputSource()
    user_crypt_option = getCryptOption()
    user_cipher_option = getCipherOption()

    newline()

    # Will store input text and output text
    user_data = {}
    user_data["output"] = []

    # For aesthetics only
    if user_crypt_option[1] == "encrypt text":
        instruction = "to encrypt"
    else:
        instruction = "to decrypt"

    # Gets the input text
    if user_source_option[1] == "direct input string":
        user_data["text"] = [prefixedPrompt("user input", yellow, main_style, f"Please enter the text {instruction}: ")]
    else:
        while True:
            try:
                user_file = prefixedPrompt("user input", yellow, main_style, f"Please enter the file containing the text {instruction}: ")
                user_data["text"] = importLines(user_file)
                break
            except Exception:
                print(returnPrefixedText("error", red, "", "File does not exist. Please enter the full path or try again."))

    # Creates the cipher
    if user_crypt_option[1] == "encrypt text":
        if user_cipher_option[1] == "caesar":
            while True:
                try:
                    # The key has 25 possible values that are conveniently generated using range(26) and can be operated on by transforming the range into a list
                    key = getInteger(returnPrefixedText("user input", yellow, main_style, "Since you're using the Caesar Cipher, you'll need to provide an encryption key: "), list(range(26)))
                    # Cipher validates inputs so it will raise an exception if needed
                    cipher = CaesarCipherInstance("", "", key)
                    break
                except Exception:
                    print(returnPrefixedText("error", red, main_style, "You will need to provide a key between 1 and 25 inclusive"))
        elif user_cipher_option[1] == "atbash":
            cipher = AtbashCipherInstance("", "")

        for line in user_data["text"]:
            # Uses the instance repeatedly to encrypt text
            cipher.plaintext = line
            cipher.encrypt()
            # Prepares the output object
            user_data["output"].append(cipher.ciphertext)
            # Clears the cipher's data (except the key) for the next iteration
            cipher.clear()
    # Does the same as above except cipher.encrypt() is just cipher.decrypt()
    if user_crypt_option[1] == "decrypt text":
        if user_cipher_option[1] == "caesar":
            while True:
                try:
                    key = getInteger(returnPrefixedText("user input", yellow, main_style, "Since you're using the Caesar Cipher, you'll need to provide the decryption key: "), list(range(26)))
                    cipher = CaesarCipherInstance("", "", key)
                    break
                except Exception:
                    print(returnPrefixedText("error", red, main_style, "You will need to provide a key between 1 and 25 inclusive"))
        elif user_cipher_option[1] == "atbash":
            cipher = AtbashCipherInstance("", "")
        for line in user_data["text"]:
            cipher.ciphertext = line
            cipher.decrypt()
            user_data["output"].append(cipher.plaintext)
            cipher.clear()

    # Checks if the user wants to save to an external file
    user_save_option = getSaveOption()
    if user_save_option[0] is True:
        writeLines(user_save_option[1], user_data["output"])
    else:
        print(f"\n{returnPrefixedText('output', cyan, main_style, 'Here is your output: ')}")
        print(option_style)
        # Prints each item in the list on a line (got from an answer on Stack Overflow)
        print(*user_data["output"])


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # Ensures we get no ugly (or telling) traceback
        print("\nKeyboardInterrupt: End Program")
