# Provides the option to select whether to encrypt or decrypt files
from interface.interactions import getInteger, mapOption
from styles.colorama_style import main_style, option_style, reset_style

def getCryptOption():
	user_option = getInteger(f'''\n{main_style}
Select encryption or decryption:{option_style}
1. Encrypt Text
2. Decrypt Text\n
{reset_style}''', [1, 2])

	return mapOption(user_option, ["encrypt text", "decrypt text"])