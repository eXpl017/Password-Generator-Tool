import secrets
import string


############ VARS ###########

symbols = '!@#$%^&~'
charset = {
        'lowr': string.ascii_lowercase,
        'uppr': string.ascii_uppercase,
        'dig': string.digits,
        'punc': symbols
    }

#############################


####### HELPER FUNCS ########

def randomShuffle(lst: list[str]) -> list[str]:

    """
    Shuffles given list securely, using secrets module instead of the predictable random module.

    Args:
        lst: List of characters to be shuffled.

    Returns:
        Shuffled list.
    """

    lst_len = len(lst)
    range_lst = list(range(lst_len))
    shuffled_lst = []
    while len(range_lst):
        random_pos = secrets.choice(range_lst)
        shuffled_lst.append(lst[random_pos])
        range_lst.remove(random_pos)
    return shuffled_lst


def allowedSymbols(string: str) -> str:

    """
    Excludes user provided characters from default symbols.

    Args:
        string: String of symbols to exclude from default symbols.

    Returns:
        String of symbols which can be used in the password.
    """

    local_symbols = symbols
    string = str(set(string))
    for char in string:
        if char in local_symbols: local_symbols = local_symbols.replace(char,'')
    return local_symbols

#############################


def generate(include: list[str], exclude: str, length: int):

    """
    Generates password of given length using characters specified by user.

    Args:
        include: List of strings containg character sets to include in the password.
        exclude: String of symbols to exclude from Symbol/Punctuations.
        length: Length of password to generate.

    Returns:
        Password as a string.
    """

    if ('punc' in include) and len(exclude):
        charset['punc'] = allowedSymbols(exclude)

    allowed_chars = ''
    for i in include:
        allowed_chars += charset[i]

    unshuffled_lst = (
            [secrets.choice(charset[x]) for x in include]
            +
            [secrets.choice(allowed_chars) for _ in range(length - len(include))]
        )
    shuffled_lst = randomShuffle(unshuffled_lst)
    password_generated = ''.join(shuffled_lst)

    return password_generated

#if __name__=="__main__":
#    password = generate()
