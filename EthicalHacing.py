# Get subdomains
# ==============
import sys
import requests
from os import path
import argparse

# The argparse module makes it easy to create user-friendly command-line interfaces.
# The program defines the arguments it requires, and argparse will handle parsing them from sys.argv.
# The argparse module also generates help and usage messages automatically and reports errors when users
# provide invalid arguments to the program.
parser = argparse.ArgumentParser()

# The ArgumentParser.add_argument() method attaches individual argument specifications to the parser.
# It supports positional arguments, options that accept values, and enable/disable flags.
parser.add_argument('-t', '--target', help="Which domain do you want to target?")
parser = parser.parse_args()


# Main function
def main():
    if parser.target:
        # Look for subdomains in the file
        if path.exists('resources/subdomains.txt'):
            subdomains_list = open('resources/subdomains.txt', 'r')
            subdomains_list = subdomains_list.read().split('\n')
            # For each discovered subdomain, construct the URL
            for subdomain in subdomains_list:
                for protocol in ["http://", "https://"]:
                    url = protocol + subdomain + "." + parser.target
                    # Start the search
                    try:
                        response = requests.get(url)
                        if response.status_code == 200:
                            print("(+) Subdomain discovered: " + url)
                    except requests.ConnectionError:
                        pass
    else:
        print("The entered domain is not valid. Please try again.")
        sys.exit()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
