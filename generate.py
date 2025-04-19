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
    lst_len = len(lst)
    range_lst = list(range(lst_len))
    shuffled_lst = []
    while len(range_lst):
        random_pos = secrets.choice(range_lst)
        shuffled_lst.append(lst[random_pos])
        range_lst.remove(random_pos)
    return shuffled_lst


def allowedSymbols(string: str) -> str:
    local_symbols = symbols
    string = str(set(string))
    for char in string:
        if char in local_symbols: local_symbols = local_symbols.replace(char,'')
    return local_symbols

#############################


def generate(include: list[str], exclude: str, length: int):

    if ('punc' in include) and len(exclude):
        charset['punc'] = allowedSymbols(exclude)

    allowed_chars = ''
    for i in include:
        allowed_chars += charset[i]

    print(allowed_chars)

    unshuffled_lst = (
            [secrets.choice(charset[x]) for x in include]
            +
            [secrets.choice(allowed_chars) for _ in range(length - len(include))]
        )

    shuffled_lst = randomShuffle(unshuffled_lst)
    password_generated = ''.join(shuffled_lst)
    print(password_generated)
