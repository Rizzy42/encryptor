from interface.data import name, version
from styles.colorama_fore import white, cyan

from colorama import Fore
from platform import platform

def welcomeMsg():
	user_platform = platform()
	if user_platform == "Linux-5.16.19-76051619-generic-x86_64-with":
		user_platform = "Docker Universal"

	print(f"\nWelcome to {cyan}Encryptor{white} (Version {cyan}{version}{white}) on {cyan}{user_platform}{white}")

	
