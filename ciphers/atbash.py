# Classes are more portable and concise than functions
class AtbashCipherInstance:
	# Initialises the two components of the cipher
	def __init__(self, plaintext, ciphertext):
		# Identification of cipher 
		self.ciphertype = "atbash"
		self.plaintext = plaintext
		self.ciphertext = ciphertext

	# These are used to help maintain capitalisation in messages
	alphabet_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
	alphabet_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

	# This private method is not accessible outside of the class, which obeys abstraction
	# It'll help us to prevent repeating ourselves when we encrypt or decrypt
	def __cipher_unified(self, operation):
		# Should another programmer use this code, the below else statement will help them identify if an error has occurred in what operation they requested
		if operation == "encrypt":
			text_input = self.plaintext
		elif operation == "decrypt":
			text_input = self.ciphertext
		else:
			raise Exception("Invalid operation")

		# Aliasing variables to prevent repetition of "self"
		alphabet_lower = self.alphabet_lower
		alphabet_upper = self.alphabet_upper

		# This mutate operation mutates the required class property by an argument
		# It handles which operation is being used and prevents repetition while increasing modularity
		def mutate(arg):
			if operation == "encrypt":
				self.ciphertext = self.ciphertext + arg
			else:
				self.plaintext = self.plaintext + arg

		for letter in text_input:
			# Spaces should not be shifted
			if letter == " ":
				mutate(" ")
				continue
			# Copies to a local alphabet_local variable for that specific letter
			# Maintaisn capitalisation, as said before
			elif letter in alphabet_lower or letter in alphabet_upper:
				if letter in alphabet_lower:
					alphabet_local = alphabet_lower
				elif letter in alphabet_upper:
					alphabet_local = alphabet_upper

				# Genereates the shifted index using the user's key
				letter_shifted_index = 25 - alphabet_local.index(letter)
				mutate(alphabet_local[letter_shifted_index])

			# While the instructions called for alphabet letters only, most messages won't consist of such
			# It'll be helpful to preserve them in the original message to make this program more useful
			else:
				mutate(letter)

	# Exposed methods which really just call the above method
	def encrypt(self):
		self.__cipher_unified("encrypt")
	
	def decrypt(self):
		self.__cipher_unified("decrypt")

	def clear(self):
		self.plaintext = ""
		self.ciphertext = ""
