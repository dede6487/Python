import argparse
import os
import re

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input_file", type=str,
                    help="Specifies the path of the input file from which patterns should be extracted.", required=True)

parser.add_argument("-p", "--patterns", type=str, required=True, nargs="+",  # "+" for nargs >=1
                    help="Specifies a non-empty list of string patterns that are regular expressions.")

parser.add_argument("-s", "--seperator", type=str, default="\n",
                    help="The string to use for separating extracted pattern matches.")

parser.add_argument("-e", "--encoding", type=str, default="utf-8",
                    help="The character encoding to use for accessing all files.")

args = parser.parse_args()

# now checking all the requirements for the arguments:

if not os.path.isfile(args.input_file):
    print("Error: path must be a file")
    raise ValueError

with open(args.input_file, "r") as f:
    i = 0
    search_file = f.read()
    for regex in args.patterns:
        with open(f"{os.path.basename(args.input_file)}_{i}.txt", "w") as out:
            print(f"regex: {regex}", file=out)
            for result in re.finditer(regex, search_file):
                print(result.group(0), end=args.seperator, file=out)
        i += 1
