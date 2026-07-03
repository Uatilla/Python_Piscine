from ft_filter import ft_filter
import sys


def processInput(wordList, size) -> None:
    """
    Filter words from the input string that are longer than a given size.

    Splits the input string into words, filters them using ft_filter,
    and prints the resulting list.

    Args:
        wordList (str): The input text containing words separated by spaces.
        size (int): Minimum word length to keep.

    Prints:
        The list of words longer than 'size'.
    """
    newList: list[str] = [word for word in wordList.split()]
    resultList = list(ft_filter(lambda wrd: len(wrd) > size, newList))
    print(resultList)


def main() -> None:
    """
    Main entry point of the program.

    Validates command-line arguments and processes the input text.

    Expected usage: python script.py "text here" <minimum_size>

    Raises:
        AssertionError: If the number of arguments is wrong or
                        if the size is not a valid integer.
    """
    sys.tracebacklimit = 0
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")
    try:
        size: int = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad") from None
    processInput(sys.argv[1], size)


if __name__ == "__main__":
    main()
