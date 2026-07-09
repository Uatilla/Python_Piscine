import pandas as pd


def load(file: str) -> pd.DataFrame:
    """Load a file, print its dimmensions and return it"""
    try:
        df = pd.read_csv(file)
        print(f"Loading dataset of dimmensions {df.shape}")
        return df
    except FileNotFoundError:
        print(f"Error: The file {file} was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file {file} is completely empty.")
    except pd.errors.ParserError:
        print(f"Error: {file} malformed or corrupt.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"Error: Unexpected error while loading {file}: {e}")
    return None


def main():
    """Main entry of the program."""
    print(load("test.csv"))


if __name__ == "__main__":
    main()
