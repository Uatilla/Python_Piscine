from ft_filter import ft_filter
import sys
sys.tracebacklimit = 0


def processInput(wordList, size) -> None:
    """Extract the words and prints them if bigger than size."""
    newList: list[str] = [word for word in wordList.split()]
    resultList = list(ft_filter(lambda wrd: len(wrd) > size, newList))
    print(resultList)


def main() -> None:
    """Validate the input, raise errors when applicable prints the stats
    about the input received."""
    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")
    try:
        size: int = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad") from None
    processInput(sys.argv[1], size)


if __name__ == "__main__":
    main()
