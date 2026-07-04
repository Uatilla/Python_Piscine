from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the given path and return it as a NumPy RGB array.

    Supports JPG and JPEG formats as required by the exercise.
    Prints the shape of the image in the format:
        "The shape of image is: (H, W, 3)"

    Args:
        path (str): Path to the image file.

    Returns:
        np.ndarray: The image as a 3D NumPy array
                    (height, width, 3) in RGB format.
                    Returns empty array on error.

    Raises / Prints:
        Clear error messages for unsupported formats, missing files, etc.
    """
    try:
        if not path.lower().endswith((".jpg", ".jpeg")):
            raise AssertionError("Unsupported image format.")
        arr = np.array(Image.open(path))
        print(f"The shape of image is: {arr.shape}")
        return arr
    except FileNotFoundError:
        print(f"Error: could not find '{path}'")
        return np.array([])
    except Exception as e:
        print(f"Error: {e}")
        return np.array([])


def main():
    """Main function including its own tester."""
    print(ft_load("animal.jpeg"))
    print(ft_load("invalid.format"))
    print(ft_load("IdontExist.jpg"))


if __name__ == "__main__":
    main()
