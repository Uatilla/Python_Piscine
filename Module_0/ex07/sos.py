import sys


def get_morse_code() -> dict[str, str]:
    """Return a dictionary mapping alphanumeric characters to Morse code."""
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
    """Process each character from the message converting them into Morse
    code, printing and the end."""
    morse_msg: list[str] = [get_morse_code()[ch.upper()] for ch in msg]
    print(" ".join(morse_msg))


def main() -> None:
    """Validate the input, raise errors when applicable prints the stats
    about the input received."""
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
