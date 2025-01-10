from sys import argv


def getCharCount(string: str) -> dict:
    """
    Function that counts the different types of chars
    and return a count dictionnary with keys
    """
    count = {"total": 0, "upper": 0, "lower": 0, "digit": 0, "space": 0, "punc": 0}
    for c in string:
        count["total"] += 1
        if c.isupper():
            count["upper"] += 1
        elif c.islower():
            count["lower"] += 1
        elif c.isdigit():
            count["digit"] += 1
        elif c.isspace():
            count["space"] += 1
        else:
            count["punc"] += 1
    return count


def printCount(count: dict) -> None:
    """
    Prints a description
    from the count object returned by getCharCount()
    """

    print(f'''The text contains {count["total"]} characters:
{count["upper"]} upper letters
{count["lower"]} lower letters
{count["punc"]} punctuation marks
{count["space"]} spaces
{count["digit"]} digits
    ''')


def getText() -> str:
    """
    Get's the text from the stdin if it exists
    prompts the user otherwise
    """
    if len(argv) == 2:
        return argv[1]

    text = input("What is the text to count?\n")
    return text


def main() -> int:
    """
    Analyse a string, counting the spaces, uppercase, lowercase and
    special characters
    then prints the result
    """

    text = getText()

    count = getCharCount(text)

    printCount(count)

    return 0


if __name__ == "__main__":
    main()
