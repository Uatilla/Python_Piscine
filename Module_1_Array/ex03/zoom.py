import numpy as np
from load_image import ft_load
import matplotlib
matplotlib.use('qtagg')
import matplotlib.pyplot as plt


def zoom(path: str) -> np.ndarray:
    try:
        arr = ft_load(path)
        print(arr)
        plt.imshow(arr[100:500, 450:850])
        plt.show()
    except Exception as e:
        print(f"Error: {e}")

def main():
    zoom("animal.jpeg")

if __name__== "__main__":
    main()