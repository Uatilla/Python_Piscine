import sys
sys.tracebacklimit = 0

if (len(sys.argv) == 1):
    sys.exit(1)
elif (len(sys.argv) > 2):
    raise AssertionError("more than one argument is provided") from None
try:
    number = int(sys.argv[1])
except ValueError:
    raise AssertionError("argument is not an integer") from None
print("I'm Even." if number % 2 == 0 else "I'm Odd.")
