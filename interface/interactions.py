# Provides convenient methods that may be needed by other interface programs 
from styles.colorama_fore import red, white

# Provides a way of safely getting an integer from the user
def getInteger(prompt, numbers):
	while True:
		try:
			return_int = int(input(prompt))
			if return_int not in numbers:
				raise Exception
			
			return return_int
		except ValueError:
			print(f"\n{red}ERROR{white} That's not an integer.")
		except Exception:
			print(f"\n{red}ERROR{white} Please select from the list of given options [{numbers[0]}-{numbers[len(numbers) - 1]}]")