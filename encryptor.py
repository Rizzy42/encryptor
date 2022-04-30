# This main program brings all the components together and does the actual heavy work of encryption

# Initialises colorama to convert ANSI codes to win32 so that the display correctly on Windows
from colorama import init as colorama_init
from colorama import Fore

from utils.files import importLines, writeLines, appendLines

# Interface programs
from interface.welcome import welcomeMsg
from interface.user_options.input_source import getInputSource
from interface.user_options.crypt_option import getCryptOption
from interface.user_options.cipher_option import getCipherOption
from interface.user_options.save_option import getSaveOption

from interface.interactions.options import getInteger
from interface.interactions.text import prefixedPrompt, newline, returnPrefixedText

from styles.colorama_fore import red, yellow
from styles.colorama_style import main_style

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

	user_data = {}
	user_data["output"] = []

	if user_crypt_option[1] == "encrypt text":
		instruction = "to encrypt"
	else:
		instruction = "to decrypt"

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
	
	if user_crypt_option[1] == "encrypt text":
		if user_cipher_option[1] == "caesar":
			while True:
				try:
					key = getInteger(returnPrefixedText("user input", yellow, main_style, f"Since you're using the Caesar Cipher, you'll need to provide an encryption key: "), list(range(26)))
					if key == 0:
						raise Exception
					cipher = CaesarCipherInstance("", "", key)
					break
				except Exception:
					print(returnPrefixedText("error", red, main_style, "You will need to provide a key between 1 and 25 inclusive"))
		elif user_cipher_option[1] == "atbash":
			cipher = AtbashCipherInstance("", "")

		for line in user_data["text"]:
			cipher.plaintext = line
			cipher.encrypt()
			user_data["output"].append(cipher.ciphertext)
			cipher.clear()
	if user_crypt_option[1] == "decrypt text":
		if user_cipher_option[1] == "caesar":
			while True:
				try:
					key = getInteger(returnPrefixedText("user input", yellow, main_style, f"Since you're using the Caesar Cipher, you'll need to provide the decryption key: "), list(range(26)))
					if key == 0:
						raise Exception
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
	
	user_save_option = getSaveOption()
	if user_save_option[0] == True:
		with open(user_save_option[1], "w") as file:
			file.writelines(user_data["output"])
	
	
if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\nKeyboardInterrupt: End Program")
