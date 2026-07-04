import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def apply_gray_scale(image: np.ndarray) -> np.ndarray:
    """
    Apply luminosity method into the image.
    """
    gray = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
    gray = gray.astype(np.uint8)
    gray = gray[:, :, np.newaxis]
    print(f"New shape after slicing: {gray.shape} or {gray.shape[: 2]}")
    return gray


def rotate(path: str) -> np.ndarray:
    """
    Load image, crop a region, convert to grayscale, rotate and display.
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
        gray = apply_gray_scale(slicedImage)
        rotatedGray = gray.transpose(1, 0, 2)[::-1]
        print(rotatedGray)
        plt.imshow(rotatedGray, cmap='gray')
        plt.show()
        return rotatedGray
    except Exception as e:
        print(f"Error: {e}")


def main():
    """
    Program entry point.
    """
    rotate("animal.jpeg")


if __name__ == "__main__":
    main()
