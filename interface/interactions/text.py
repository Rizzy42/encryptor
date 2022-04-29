from styles.colorama_fore import white

def returnPrefixedText(prefix, prefix_colour, prefix_style, text):
	return f"{prefix_style}{prefix_colour}{prefix.upper()}{white} {text}"

def prefixedPrompt(prefix, prefix_colour, prefix_style, text):
	return input(f"{prefix_style}{prefix_colour}{prefix.upper()}{white} {text}")

def newline():
	print("\n")