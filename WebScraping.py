import argparse
from blessed import Terminal
from colorama import Fore, Back, init
import webbrowser
import scraper

# When running the script it shows information about the arguments
Terminal()
init()
print(f"\n{Back.YELLOW}-------- Web scraping - by Javier Borreguero --------{Back.RESET}")
parser = argparse.ArgumentParser(description='Web scraping ')
parser.add_argument('-l', '--url', help='The coursehero url to bypass', required=False)
parser.add_argument('-o', '--output', help='Output file (default file name from CourseHero)', required=False)
parser.add_argument('--open', help='Opens the PDF in the default web browser', default=False, action='store_true')
parser.add_argument('--debug', help='Show error traceback', default=False, action='store_true')
args = parser.parse_args()

# Args config
URL = args.url
OPEN_FILE = args.open
PDF_FILE_NAME = args.output
try:
    print("Cargando página")
    if OPEN_FILE:

        print(f"\n{Fore.RESET}[{Fore.GREEN}>{Fore.RESET}]" + f" {Fore.GREEN}Completado!{Fore.RESET}")
except Exception as e:
    print(e)
    