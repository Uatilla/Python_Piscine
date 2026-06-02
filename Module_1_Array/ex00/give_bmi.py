import numpy as np


def validation(
    checklist: list[int | float],
    lst_nm: str = "lst_nm"
) -> tuple[bool, str]:
    """Validate the content of a list."""
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
    """Calculate the BMI for each individual values from a list."""
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
    """Return a list displaying which elements are under the limit."""
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
