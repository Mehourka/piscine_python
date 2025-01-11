from ft_filter import ft_filter
from sys import argv


def throw(error):
    """print error and exit"""
    print("AssertError: ", error)
    exit(1)


def parseArgv():
    """Checks arguments validity
    returns the text to split
    and min word length
    """
    if not (len(argv) == 3 and isinstance(argv[1], str)):
        throw("the arguments are bad")
    try:
        int(argv[2])
    except ValueError:
        throw("the arguments are bad")

    text = argv[1]
    min_word_len = int(argv[2])
    return text, min_word_len


def main():
    """Filters words which length is lesser than N"""
    text, min_word_len = parseArgv()

    words = text.split(" ")
    result = ft_filter(lambda w: len(w) >= min_word_len, words)

    print(list(result))


if __name__ == "__main__":
    main()
