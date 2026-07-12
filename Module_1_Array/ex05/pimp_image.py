import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load
import array


def render_image(array: np.ndarray) -> None:
    """Renders the image received"""
    plt.imshow(array)
    plt.show()


def ft_invert(array) -> array:
    """Inverts the color of the image received."""
    try:
        if array.size == 0:
            print("Error: Failed to load the image")
            return np.ndarray([])
        inverted = 255 - array
        render_image(inverted)
        return inverted
    except Exception as e:
        print(f"Error: {e}")


def ft_red(array) -> array:
    """Display only the red channel of an image"""
    try:
        if array.size == 0:
            print("Error: Failed to load the image")
            return np.ndarray([])
        red_arr = array.copy()
        red_arr[:, :, 1] = 0
        red_arr[:, :, 2] = 0
        render_image(red_arr)
        return red_arr
    except Exception as e:
        print(f"Error: {e}")


def ft_green(array) -> array:
    """Display only the green channel of an image"""
    try:
        if array.size == 0:
            print("Error: Failed to load the image")
            return np.ndarray([])
        red_arr = array.copy()
        red_arr[:, :, 0] = 0
        red_arr[:, :, 2] = 0
        render_image(red_arr)
        return red_arr
    except Exception as e:
        print(f"Error: {e}")


def ft_blue(array) -> array:
    """Display only the blue channel of an image"""
    try:
        if array.size == 0:
            print("Error: Failed to load the image")
            return np.ndarray([])
        red_arr = array.copy()
        red_arr[:, :, 0] = 0
        red_arr[:, :, 1] = 0
        render_image(red_arr)
        return red_arr
    except Exception as e:
        print(f"Error: {e}")


def ft_grey(array) -> array:
    """
    Display the image in a grey scale.
    """
    grey_arr = np.dot(array[..., :3], [0.2989, 0.5870, 0.1140])
    grey_arr = grey_arr.astype(np.uint8)
    grey_arr = grey_arr[:, :, np.newaxis]
    plt.imshow(grey_arr, cmap='grey')
    plt.show()
    return grey_arr


def main():
    """
    Program entry point.
    """
    arr = ft_load("landscape.jpg")
    render_image(arr)
    ft_invert(arr)
    ft_red(arr)
    ft_green(arr)
    ft_blue(arr)
    ft_grey(arr)


if __name__ == "__main__":
    main()
