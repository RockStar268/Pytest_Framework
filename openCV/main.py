import cv2
import numpy as np

img = cv2.imread("../openCV/photo/CryptiasX.png")
height, width = img.shape[:2]
center = (width / 2, height / 2)


# cv2.imwrite("photo/output.jpg", img)
# print(img.shape)
# print("Height: ", img.shape[0])
# print("Width: ", img.shape[1])
def Rotate_Image():
    rotate_image = cv2.getRotationMatrix2D(center=center, angle=70, scale=0.5)
    final_image = cv2.warpAffine(src=img, M=rotate_image, dsize=(width, height))
    cv2.imshow("Rotated Image", final_image)


def Transpose_Image():
    transpose_image = cv2.transpose(img)
    cv2.imshow("Transpose Image", transpose_image)


def Capture_Video():
    video = cv2.VideoCapture(0)  # 0 = webcam access ; for accessing CCTV footage, replace 0 with rtsp url

    while True:
        check, frame = video.read()
        cv2.imshow("frame", frame)


def crop_image():
    start_row, start_col = int(height * .15), int(width * .15)
    end_row, end_col = int(height * .65), int(width * .65)

    cropped_image = img[start_row: end_row, start_col: end_col]

    cv2.imshow("Cropped Image", cropped_image)

def blur_image():
    kernel = np.ones((7, 7), np.float32) / 49
    blurred_image = cv2.filter2D(img, -1, kernel)
    cv2.imshow("Blurred Image", blurred_image)

cv2.imshow("Original Image", img)
Rotate_Image()
Transpose_Image()
# Capture_Video()
crop_image()
blur_image()

cv2.waitKey(0)
