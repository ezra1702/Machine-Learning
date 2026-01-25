import cv2 as cv
import matplotlib.pyplot as plt
# 1. Membaca Gambar
img = cv.imread("/home/ezra/Desktop/Machine-learning/computer-vision/assets/img_1.jpeg")
cv.imshow("Gambar Asli", img) # ("Judul Jendela", Gambar)
# memberikan grid pada gambar 



# 2. Editing Gambar
# Mengubah Ukuran Gambar
img_resized = cv.resize(img, (400, 300))  # (width, height)
cv.imshow("Gambar Resized", img_resized) # ("Judul Jendela", Gambar)

# Memotong Gambar
img_cropped = img[50:200, 100:300] # img[y1:y2, x1:x2] y: baris, x: kolom
cv.imshow("Gambar Cropped", img_cropped) # ("Judul Jendela", Gambar)

# Flip Gambar
img_flipped = cv.flip(img, 1) # 0: Vertikal, 1: Horizontal, -1: Kedua Arah)
cv.imshow("Gambar Flipped", img_flipped) # ("Judul Jendela", Gambar)

# Grayscale
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gambar Grayscale", img_gray) # ("Judul Jendela", Gambar)

# Brightness and Contrast 
bright = cv.convertScaleAbs(img, alpha=1.2, beta=30) # alpha: contrast, beta: brightness
cv.imshow("Gambar Brightness and Contrast", bright) # ("Judul Jendela

# Blur
blurred = cv.GaussianBlur(img, (15, 15), 0) # (width, height), sigma
cv.imshow("Gambar Blurred", blurred) # ("Judul Jendela", Gambar)

# Edge Detection
edges = cv.Canny(img, 100, 200) # threshold1, threshold2
cv.imshow("Gambar Edge Detection", edges) # ("Judul Jendela", Gambar)

# Thresholding
_, thresh = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY) # threshold value, max value, threshold type
cv.imshow("Gambar Thresholding", thresh) # ("Judul Jendela", Gambar)


# 3. Menampilkan Gambar
cv.waitKey(0) 
