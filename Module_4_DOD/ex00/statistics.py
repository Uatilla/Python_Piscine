from typing import Any


def mean(*args: Any, header: bool = True) -> float:
    """Calculates the mean from args."""
    avg = sum(args) / len(args)
    if header:
        print(f"mean : {avg:.1f}")
    return avg


def median(*args: Any, header: bool = True) -> float:
    """Calculates the median from args."""
    sort = tuple(sorted(args))
    size = len(sort)
    if (size % 2 == 1):
        med = sort[size // 2]
    else:
        med = (sort[size // 2 - 1] + sort[size // 2]) / 2
    if header:
        print(f"median : {med}")
    return med


def quartile(*args: Any, header: bool = True) -> list:
    """Calculates the quartile from args."""
    sort = tuple(sorted(args))
    size = len(sort)
    q1 = sort[size // 4]
    q3 = sort[3 * size // 4]
    quartile = [float(q1), float(q3)]
    if header:
        print(f"quartile : {quartile}")
    return quartile


def std(*args: Any, header: bool = True) -> float:
    """Calculate the std from args."""
    avg = mean(*args, header=False)
    stdArgs = [(v - avg)**2 for v in args]
    std = (mean(*stdArgs, header=False) ** 0.5)
    if header:
        print(f"std : {std:.11f}")
    return std


def var(*args: Any, header: bool = True) -> float:
    """Calculate the variance from args."""
    var = std(*args, header=False) ** 2
    if header:
        print(f"var : {var:.7f}")
    return var


functionHandler = {
    "toto": mean,
    "tutu": median,
    "tata": quartile,
    "hello": std,
    "world": var,
}


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Calculate mean, median, quartile, std dev and variance from args."""
    for key, value in kwargs.items():
        if key in functionHandler and functionHandler[key].__name__ == value:
            try:
                if not all(isinstance(arg, (int, float)) for arg in args):
                    raise
                functionHandler[key](*args)
            except Exception as e:
                e
                print("ERROR")


def main():
    """Main start of the program."""
    ft_statistics(1, 42, 360, 11, 64, toto="mean",
                  tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
