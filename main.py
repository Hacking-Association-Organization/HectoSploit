from rich import print, pretty
import pyfiglet

pretty.install()

Format = pyfiglet.figlet_format("HectoSploit", "slant")
print(f"{Format}{' '*40}v 0.0.1")
