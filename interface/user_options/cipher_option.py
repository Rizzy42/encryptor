from ciphers.cipher_data import included_ciphers
from interface.interactions.options import getInteger, mapOption
from interface.interactions.text import returnPrefixedText
from styles.colorama_fore import cyan

from styles.colorama_style import main_style, option_style, reset_style

def getCipherOption():
	print(f"\n{returnPrefixedText('config', cyan, main_style, 'Select a cipher:')}\n{option_style}")

	for cipher in included_ciphers:
		print(f"{included_ciphers.index(cipher) + 1}. {cipher.capitalize()} Cipher")

	user_option = getInteger(f"\n{reset_style}", [1, len(included_ciphers)])

	return mapOption(user_option, included_ciphers)
