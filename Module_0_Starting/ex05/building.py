import sys


def main():
    """
    Entry point of the program.

    Handles command line arguments or interactive input.
    Validates input and delegates processing to processMsg().

    Raises:
        AssertionError: If more than one argument is provided.
    """
    sys.tracebacklimit = 0
    try:
        if (len(sys.argv) == 1):
            string = ""
            while (string == ""):
                print("What is the text to count?")
                string = input()
            processMsg(string)
        elif (len(sys.argv) > 2):
            raise AssertionError("more than one argument is provided")
        else:
            processMsg(sys.argv[1])
    except EOFError:
        raise AssertionError("EOFError occurred") from None


def processMsg(msg):
    """
    Count and display statistics about character types in the given string.

    Counts:
        - Uppercase letters
        - Lowercase letters
        - Punctuation marks
        - Spaces
        - Digits

    Args:
        msg (str): The input text to analyze.

    Prints the total character count and breakdown by category.
    """
    stats = {"upper": 0, "lower": 0, "punct": 0, "spaces": 0, "digits": 0}
    for char in msg:
        if char.isupper():
            stats["upper"] += 1
        elif char.islower():
            stats["lower"] += 1
        elif char.isspace():
            stats["spaces"] += 1
        elif char.isdigit():
            stats["digits"] += 1
        else:
            stats["punct"] += 1
    print(f"The text contains {len(msg)} characters:")
    print(f"{stats['upper']} upper letters")
    print(f"{stats['lower']} lower letters")
    print(f"{stats['punct']} punctuation marks")
    print(f"{stats['spaces']} spaces")
    print(f"{stats['digits']} digits")


if __name__ == "__main__":
    main()
