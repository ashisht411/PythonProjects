import os
print(os.getcwd())
os.makedirs("newFilefromCLIcommands")
os.rename("newFilefromCLIcommands", "newFilefromCLIcommandsRenamed")


import sys
print(sys.argv)
print(sys.version)

import argparse
parser = argparse.ArgumentParser(description="Simple CLI command")
parser.add_argument("name", help="Your Name (used for greeting)")
try:
    args = parser.parse_args()
    print(f"Hello, '{args.name}'!")
except Exception as e:
    print(f"Error: {e}")
    args = argparse.Namespace(name="Guest")  # Default value
    print(f"Hello, '{args.name}'!")