# Provides convenient methods regarding user options that are needed by the user_options programs
from styles.colorama_fore import red, white

from interface.interactions.text import returnPrefixedText

# Provides a way of safely getting an integer from the user
def getInteger(prompt, numbers):
	while True:
		try:
			return_int = int(input(prompt))
			if return_int not in numbers:
				raise Exception
			
			return return_int
		except ValueError:
			print(returnPrefixedText("error", red, "", "That's not an integer"))
		except Exception:
			print(returnPrefixedText("error", red, "", f"Please select from the list of given options [{numbers[0]}-{numbers[len(numbers) - 1]}]"))

# Provides a way of mapping an integer choice (selected by the user) to the text choice itself
# This makes variables that track user options more informative as they provide the actual option the user picked
def mapOption(option, choices):
	for choice in choices:
		mapped_choice = choices.index(choice)
		if mapped_choice == option - 1:
			break
	
	return [option, choices[mapped_choice]]