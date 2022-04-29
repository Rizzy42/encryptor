# Provides the input source the user will take their text from

from interface.data import name, version
from interface.interactions.options import getInteger, mapOption
from interface.interactions.text import returnPrefixedText

# These colours are repeated, so we import them
from styles.colorama_fore import cyan
# Allows style consistency
from styles.colorama_style import main_style, option_style, reset_style

def getInputSource():
	user_option = getInteger(f'''{main_style}
{returnPrefixedText("config", cyan, main_style, "Please select an input source:")}\n{option_style}
1. External file
2. Direct input string\n
{reset_style}''', [1, 2])

	return mapOption(user_option, ["external file", "direct input string"])
