# Provides the input source the user will take their text from

from interface.data import name, version
from interface.interactions import getInteger, mapOption

# These colours are repeated, so we import them
from styles.colorama_fore import white
# Allows style consistency
from styles.colorama_style import main_style, option_style, reset_style

def getInputSource():
	user_option = getInteger(f'''{main_style}
Please select an input source:{option_style}
1. External file
2. Direct input string\n
{reset_style}''', [1, 2])

	return mapOption(user_option, ["external file", "direct input string"])
