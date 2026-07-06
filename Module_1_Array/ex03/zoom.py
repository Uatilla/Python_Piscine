import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def apply_grey_scale(image: np.ndarray) -> np.ndarray:
    """
    Apply luminosity method into the image.
    """
    grey = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
    grey = grey.astype(np.uint8)
    grey = grey[:, :, np.newaxis]
    print(f"New shape after slicing: {grey.shape} or {grey.shape[: 2]}")
    return grey


def zoom(path: str) -> np.ndarray:
    """
    Load image, crop a region, convert to greyscale and display.
    """
    try:
        arr = ft_load(path)
        if arr.size == 0:
            print("Error: Failed to load the image")
            return np.ndarray([])
        print(arr)
        slicedImage = arr[100:500, 450:850]
        if slicedImage.size == 0:
            print("Error: Sliced region is empty.")
            return np.ndarray([])
        grey = apply_grey_scale(slicedImage)
        print(grey)
        plt.imshow(grey, cmap='grey')
        plt.show()
        return grey
    except Exception as e:
        print(f"Error: {e}")


def main():
    """
    Program entry point.
    """
    zoom("animal.jpeg")


if __name__ == "__main__":
    main()
