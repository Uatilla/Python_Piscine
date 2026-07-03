import numpy as np


def check_family(family: list) -> None:
    """Validates the family 2D list. Raises clear errors if invalid."""
    if not isinstance(family, list):
        raise TypeError("family must be a list")
    if not family or not isinstance(family[0], list):
        raise ValueError("family must be a non-empty 2D list")
    row_len = len(family[0])
    if not all(isinstance(r, list) and len(r) == row_len for r in family):
        raise ValueError("all rows in family must have the same length")


def slice_me(family: list, start: int, end: int) -> list:
    """It takes a list, and slice it using start and end"""
    try:
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("Start and/or End must be integers.")
        check_family(family)
        origArray = np.array(family)
        slicedArray = origArray[start:end]
        print(f"My shape is : {origArray.shape}")
        print(f"My new shape is : {slicedArray.shape}")
        return (slicedArray.tolist())
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return []


def main():
    """Main function including its own tester."""
    testList = [[1.9, 7.2], [4.20, 911.7], [208.04, 870.5], [1.8, 320.2]]
    print(slice_me(testList, 0, 3))
    print(slice_me(testList, 2, -1))


if __name__ == "__main__":
    main()
