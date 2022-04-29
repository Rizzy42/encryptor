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

from interface.interactions.text import prefixedPrompt, newline

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

	if user_source_option[1] == "direct input string":
		if user_crypt_option[1] == "encrypt text":
			instruction = "to encrypt"
		else:
			instruction = "to decrypt"
		user_data["text"] = prefixedPrompt("user input", Fore.YELLOW, main_style, f"Please enter the text {instruction}: ")

	
if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("KeyboardInterrupt: End Program")
