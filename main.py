# This main program brings all the components together and does the actual heavy work of encryption

# Initialises colorama to convert ANSI codes to win32 so that the display correctly on Windows
from colorama import init as colorama_init 

from utils.files import importLines, writeLines, appendLines

# Interface programs
from interface.user_options.input_source import getInputSource
from interface.user_options.crypt_option import getCryptOption
from interface.user_options.cipher_option import getCipherOption

from ciphers.caesar import CaesarCipherInstance
from ciphers.atbash import AtbashCipherInstance

colorama_init()

def main():
	# All the abstraction paid off, this looks great!
	user_source_option = getInputSource()
	user_crypt_option = getCryptOption()
	user_cipher_option = getCipherOption()

	
if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("KeyboardInterrupt: End Program")
