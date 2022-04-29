from styles.colorama_fore import white

def returnPrefixedText(prefix, prefix_colour, prefix_style, text):
	return f"{prefix_style}{prefix_colour}{prefix.upper()}{white} {text}"