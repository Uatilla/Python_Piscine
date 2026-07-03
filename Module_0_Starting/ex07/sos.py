import sys


def get_morse_code() -> dict[str, str]:
    """
    Return a dictionary mapping alphanumeric characters and space to Morse code.

    Returns:
        dict[str, str]: Mapping where keys are uppercase letters, digits,
                        and space; values are their Morse code representations.
    """
    return {
        'A': '.-',    'B': '-...',  'C': '-.-.', 'D': '-..',
        'E': '.',     'F': '..-.',  'G': '--.',  'H': '....',
        'I': '..',    'J': '.---',  'K': '-.-',  'L': '.-..',
        'M': '--',    'N': '-.',    'O': '---',  'P': '.--.',
        'Q': '--.-',  'R': '.-.',   'S': '...',  'T': '-',
        'U': '..-',   'V': '...-',  'W': '.--',  'X': '-..-',
        'Y': '-.--',  'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.',
        ' ': '/'
    }


def process_input(msg):
    """
    Convert a message to Morse code and print it.

    Each character is translated to its Morse code equivalent.
    Words are separated by spaces, and the full message is printed
    as a single line with Morse symbols separated by spaces.

    Args:
        msg (str): The input message to convert.
    """
    morse_msg: list[str] = [get_morse_code()[ch.upper()] for ch in msg]
    print(" ".join(morse_msg))


def main() -> None:
    """
    Main entry point of the program.

    Validates command line arguments and converts the input message
    to Morse code.

    Expected usage: python script.py "message here"

    Raises:
        AssertionError: If the number of arguments is wrong or if the
                        message contains invalid characters.
    """
    sys.tracebacklimit = 0
    try:
        if len(sys.argv) != 2 or not all(c.isalnum()
                                         or c.isspace() for c in sys.argv[1]):
            raise AssertionError("the arguments are bad")
        process_input(sys.argv[1])
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
