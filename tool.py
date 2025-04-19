import argparse
from generate import generate


############# VARS #############

symbols = '!@#$%^&~'
include_help = 'Charsets to include in the password. "upper", "dig", "punc" refer to Uppercase [A-Z], Digits [0-9] and Symbols, respectively.'
exclude_help = "Symbols to exclude from generated password. Must be a single string including all symbols to exclude, contained inside 'single quotes' (to be wary of bash special variables and substitution)."
length_help = "Length of password to generate. Must be between 8 and 20, including both edges."

################################


#### CLASS METHOD OVERRIDE #####

class MyAction(argparse.Action):

    def __init__(self, option_strings, dest, **kwargs):

        """
        Changes 'default' parameter value to include the list ['lowr'] by default.
        Setting 'default' in arg definition to ['lowr'], will achieve same results.
        """

        if 'default' not in kwargs:
            kwargs['default'] = ['lowr']
        super().__init__(option_strings, dest, **kwargs)


    def __call__(self, parser, namespace, values, option_string=None):

        """
        Adds 'lowr' to args.include list everytime the option is used.
        'lowr' is not one of the choices, but is required in the list due to nature of the generate() function.
        """

        initial_list = ['lowr']
        if values:
            final_list = initial_list + [x for x in values]
        else:
            final_list = initial_list
        setattr(namespace, self.dest, final_list)

################################


####### HELPER FUNCTIONS #######

def checkExcluded(string: str) -> str:

    """
    Checks if 'exclude' string passed by user contains only characters from allowed symbols, ignores ones which are not.

    Args:
        string: String of symbols to be excluded from generated password.

    Returns:
        String of allowed symbols to be excluded from passsword, as requested by user.
    """

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

    """
    Checks if user requested password length is allowed, i.e, in the range 8 to 20.

    Args:
        string: An integer in string format.

    Returns:
        Length of password to be generated, in integer form.

    Raises:
        ArgumentTypeError if passed string is not in range 8-20.
        ArgumentTypeError if passed string is not convertible to integer.
    """

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
        #default=None,
        choices=['uppr','punc','dig'],
        action=MyAction,
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

password = generate(args.include, args.exclude, args.length)
print(password)
