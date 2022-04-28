# Provides the input source the user will take their text from

from interface.data import name, version
from interface.interactions import getInteger

# Cyan and Yellow aren't repeated, so no need to import from utils
from colorama import Fore

# These colours are repeated, so we import them
from styles.colorama_fore import white
# Allows style consistency
from styles.colorama_style import main_style, option_style, reset_style

def getInputSource():
	print(f"\n{main_style}Welcome to {Fore.CYAN}{name}{white} (Version: {Fore.YELLOW}{version}{white})")

	return getInteger(f'''{main_style}
Please select an input source:{option_style}
1. External file
2. Direct input string\n
{reset_style}''', [1, 2])
