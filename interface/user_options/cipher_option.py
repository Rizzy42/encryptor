from interface.interactions import getInteger
from ciphers.cipher_data import included_ciphers

from styles.colorama_style import main_style, option_style, reset_style

def getCipherOption():
	print(f"\n{main_style}What cipher would you like to use?")

	print(option_style)
	for cipher in included_ciphers:
		print(f"{included_ciphers.index(cipher) + 1}. {cipher.capitalize()} Cipher")

	return getInteger(f"\n{reset_style}", [1, len(included_ciphers)])
