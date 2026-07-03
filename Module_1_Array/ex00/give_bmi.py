import numpy as np


def validation(
    checklist: list[int | float],
    lst_nm: str = "lst_nm"
) -> tuple[bool, str]:
    """
    Validate a list of numbers.

    Checks if the list is non-empty, contains only numbers (int/float),
    and all values are positive.

    Args:
        checklist (list[int | float]): List to validate.
        lst_nm (str): Name of the list (used in error messages).

    Returns:
        tuple[bool, str]: (is_valid, error_message)
    """
    if not checklist:
        return False, f"{lst_nm} cannot be empty."

    if not all(isinstance(x, (int, float)) for x in checklist):
        return False, f"{lst_nm} must contain only numbers."
    if any(x <= 0 for x in checklist):
        return False, f"{lst_nm} must contain only positive numbers."
    return True, ""


def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    """
    Calculate BMI for each person given lists of heights and weights.

    Formula: BMI = weight / (height ** 2)

    Args:
        height (list[int | float]): List of heights (in meters).
        weight (list[int | float]): List of weights (in kg).

    Returns:
        list[float]: List of BMI values.

    Raises:
        ValueError: If lists have different lengths or contain invalid data.
    """
    if len(height) != len(weight):
        raise ValueError("Height and Weight lists must have the same length.")
    for data, name in [(height, "Height"), (weight, "Weight")]:
        valid, error_msg = validation(data, name)
        if not valid:
            raise ValueError(f"{error_msg}")
    heightArr = np.array(height) ** 2
    weightArr = np.array(weight)
    return (weightArr / heightArr).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Check which BMI values exceed the given limit.

    Args:
        bmi (list[int | float]): List of BMI values.
        limit (int): The threshold value.

    Returns:
        list[bool]: True for each BMI > limit, False otherwise.

    Raises:
        ValueError: If the BMI list contains invalid data.
    """
    valid, error_msg = validation(bmi, "BMI")
    if not valid:
        raise ValueError(f"{error_msg}")
    return (np.array(bmi) > limit).tolist()


def main():
    """Simple tester."""
    l1 = [2.71, 1.15]
    l2 = [165.3, 38.4]
    bmiArr = give_bmi(l1, l2)
    print(bmiArr)
    result = apply_limit(bmiArr, 26)
    print(result)


if __name__ == "__main__":
    main()
