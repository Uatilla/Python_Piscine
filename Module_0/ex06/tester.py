# tester.py
from ft_filter import ft_filter   # or just paste the function if in same file

def test_ft_filter():
    tests = [
        # (function, iterable, description)
        (lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6], "Even numbers"),
        (lambda x: x > 10, [5, 12, 8, 15, 3], "Greater than 10"),
        (None, [0, 1, False, "hello", [], None, True], "Truthy values (None case)"),
        (None, [], "Empty iterable"),
        (lambda x: x.isalpha(), "a1b2c3d", "String filtering"),
        (lambda x: len(x) > 3, ["hi", "python", "42", "test"], "Length filter"),
    ]

    print("=== Testing ft_filter vs built-in filter ===\n")
    
    for i, (func, iterable, desc) in enumerate(tests, 1):
        # Original filter
        original = list(filter(func, iterable))
        # Your implementation
        yours = list(ft_filter(func, iterable))
        
        status = "✅ PASS" if original == yours else "❌ FAIL"
        
        print(f"{i}. {desc}")
        print(f"   Original : {original}")
        print(f"   Yours    : {yours}")
        print(f"   Result   : {status}\n")

    print("All tests finished.")

if __name__ == "__main__":
    print(f" AaAAAAA: {ft_filter.__doc__}")
    test_ft_filter()