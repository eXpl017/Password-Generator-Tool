
##################################
def checkExcluded(string):
    local_symbols = symbols
    string = str(set(string))
    unavailable = ''
    for char in string:
        if char in local_symbols: local_symbols = local_symbols.replace(char,'')
        else: unavailable += char
    if unavailable:
        print(f'Following characters are not included in the charset and will hence be ignored: {unavailable}')
    return local_symbols
####################################
