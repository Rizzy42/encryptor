# Provides the option to select whether to encrypt or decrypt files
from interface.interactions import getInteger
from styles.colorama_style import main_style, option_style, reset_style

def getCryptOption():
	print(f"\n{main_style}Select encryption or decryption.")
	print(f'''{option_style}
1. Encrypt Text
2. Decrypt Text
	''')

	return getInteger(f"\n{reset_style}", [1, 2])