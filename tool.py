import sys
import argparse


############# VARS #############

symbols = '!@#$%^&~'
include_help = 'Charsets to include in the password. "upper", "dig", "punc" refer to Uppercase [A-Z], Digits [0-9] and Symbols, respectively.'
exclude_help = "Symbols to exclude from generated password. Must be a single string including all symbols to exclude, contained inside 'single quotes' (to be wary of bash special variables and substitution)."
length_help = "Length of password to generate. Must be between 8 and 20, including both edges."

################################


####### HELPER FUNCTIONS #######

def checkExcluded(string):
    if not string:
        return string
    string = ''.join(set(string))
    unavailable = ''
    for char in string:
        if char not in symbols:
            string = string.replace(char,'')
            unavailable+=char
    if unavailable:
        print(f'Following characters are not included in the symbols charset and will hence be ignored: {unavailable}')
    return string


def checkLenRange(string):
    try:
        int_num = int(string)
        if int_num not in range(8,21):
            raise argparse.ArgumentTypeError(
                    f'Passed number - {int_num} - seems to be out of range. Please pass an integer between 8 and 20 (edges included).'
                )
        return int_num
    except ValueError:
        raise argparse.ArgumentTypeError(
                f'Passed length - {string} - seems erronous, please pass an integer between 8 and 20 (edges included).'
            )

################################


############# ARGS #############

parser = argparse.ArgumentParser(prog='pass-gen', description="Tool to generate passwords securely.")

parser.add_argument(
        '-include',
        nargs='+',
        default=['uppr'],
        choices=['uppr','punc','dig'],
        help=include_help
    )
parser.add_argument(
        '-exclude',
        nargs='?',
        default='',
        type=checkExcluded,
        help=exclude_help
    )
parser.add_argument(
        '-length',
        default='14',
        type=checkLenRange,
        help=length_help
    )

################################


args = parser.parse_args()

print(args.include)
print(args.exclude)
print(args.length)
