import sys
sys.tracebacklimit = 0


def main():
    """Validate the input, raise errors when applicable prints the stats
    about the input received."""
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
    """Counts how much of each char type is present inside the input msg."""
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
