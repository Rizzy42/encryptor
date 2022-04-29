from cgitb import reset
from interface.interactions.options import getInteger
from interface.interactions.text import returnPrefixedText, prefixedPrompt

from styles.colorama_fore import yellow, cyan
from styles.colorama_style import main_style, option_style, reset_style

def getSaveOption():
	user_choice = getInteger(f'''\n{returnPrefixedText('config', yellow, main_style, 'Would you like to write the output to a file?')}
{option_style}
1. Yes
2. No
{reset_style}\n''', [1, 2])

	if user_choice == 1:
		return [True, prefixedPrompt("config", cyan, main_style, "Where would you like to save this to? ")]
	else:
		return [False, ""]