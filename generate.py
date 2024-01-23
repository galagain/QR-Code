import cv2
import qrcode
import numpy as np
from PIL import Image
import argparse

import os


def create_qrcode(link, color):
    """
    Generate a QR code with a specified color and a transparent background from a given link.

    The function creates a QR code for the provided URL, customizes its color, and saves two images:
    one with a white background ('qr_code_white.png') and another with a transparent background
    ('qr_code_transparent.png').

    Args:
        link (str): The URL to be converted into a QR code.
        color (str): The color for the QR code in 'R,G,B' format.

    Returns:
        bool: True if the QR code is generated successfully.

    Note:
        The function saves the QR code images in the current directory.
    """
    # Initialize QR code with specific parameters
    qr = qrcode.QRCode(
        version=1,  # QR Code version (size) from 1 (21x21) to 40
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction level
        box_size=10,  # Pixel size for each box in the QR code
    )

    # Add URL data to the QR code
    qr.add_data(link)
    qr.make(fit=True)

    # Convert the QR code to an RGB image
    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # Customize QR code color
    img = np.array(img)
    black_pixels = np.all(img == [0, 0, 0], axis=-1)
    img[black_pixels] = tuple(map(int, color.split(',')))

    if not os.path.exists("images/"):
        os.mkdir("images/")

    # Save the QR code with white background
    cv2.imwrite("images/qr_code_white.png", cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    # Prepare for creating a transparent background
    image_bgr = cv2.imread("images/qr_code_white.png")
    h, w, c = image_bgr.shape
    image_bgra = np.concatenate([image_bgr, np.full((h, w, 1), 255, dtype=np.uint8)], axis=-1)

    # Convert white pixels to transparent
    white_pixels = np.all(image_bgr == [255, 255, 255], axis=-1)
    image_bgra[white_pixels, -1] = 0

    # Save the QR code with a transparent background
    cv2.imwrite("images/qr_code_transparent.png", image_bgra)

    return True


def main():
    """
    Main function to handle command-line arguments and generate a QR code.

    Parses command-line arguments to get the URL and optional color for the QR code.
    Then, it calls `create_qrcode` to generate and save the QR code images.
    """
    parser = argparse.ArgumentParser(description="QR Code Generator")
    parser.add_argument("url", help="URL to be converted into a QR code")
    parser.add_argument("--color", default="255,0,0", help="Fill color for the QR code in 'R,G,B' format")
    args = parser.parse_args()

    create_qrcode(args.url, args.color)


if __name__ == "__main__":
    main()
