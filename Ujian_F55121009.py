#muhammad waliyuddin F55121009

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np
from scipy.ndimage import gaussian_filter

# median processing
def median_filter(img):
    median_img = cv2.medianBlur(img, 5)
    return median_img
# differance image processing
def difference_image(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur_img = cv2.GaussianBlur(gray_img, (5, 5), 0)
    diff_img = cv2.absdiff(gray_img, blur_img)
    _, thresh_img = cv2.threshold(diff_img, 30, 255, cv2.THRESH_BINARY)
    return thresh_img
# grayscale processing
def grayscale(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray_img
# Fixing image with thresholding
def thresholding_correction(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, threshold_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return threshold_img
def sharpening(img):
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpened_img = cv2.filter2D(img, -1, kernel)
    return sharpened_img
def noise_reduction(img):
    denoised_img = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
    return denoised_img

# brightness correction
def brightness_correction(img):
    brightness = 50
    corrected_img = cv2.add(img, brightness)
    return corrected_img
# show image square
def show_image(img, x, y, title):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=img)
    label.image = img
    label.place(x=x, y=y)
    title_label = tk.Label(root, text=title)
    title_label.place(x=x, y=y-20)

# result processing image
def process_image(method):
    global original_img
    if method == 'grayscale':
        corrected_img = grayscale(original_img)
        show_image(corrected_img, 360, 170, 'Hasil Metode grayscale')
    elif method == 'thresholding_correction':
        corrected_img = thresholding_correction(original_img)
        show_image(corrected_img, 620, 170, 'Hasil Metode thresholding_correction')
    elif method == 'brightness':
        corrected_img = brightness_correction(original_img)
        show_image(corrected_img, 880, 170, 'Hasil Metode brightness_correction')
    elif method == 'difference_image':
        corrected_img = difference_image(original_img)
        show_image(corrected_img, 70, 450, 'Hasil Metode difference image')
    elif method == 'sharpening':
        corrected_img = sharpening(original_img)
        show_image(corrected_img, 360, 450, 'Hasil Metode sharpening image')
    elif method == 'noise_reduction':
        corrected_img = noise_reduction(original_img)
        show_image(corrected_img, 620, 450, 'Hasil Metode noise_reduction image')
    elif method == 'median_filter':
        corrected_img = median_filter(original_img)
        show_image(corrected_img, 880, 450, 'Hasil Metode median_filter image')
def show_creator():
    creator_label = tk.Label(root, text='NAMA : Muhammad Waliyuddin  | NIM : F55121009 ')
    creator_label.place(x=820, y=30)
# open image function
def open_image():
    global original_img
    file_path = filedialog.askopenfilename()
    if file_path:
        original_img = cv2.imread(file_path)
        original_img = cv2.resize(original_img, (250, 250))
        show_image(original_img, 70, 170, 'Gambar Original')
        size_label.config(format(original_img.shape[1], original_img.shape[0]))
# make a window
root = tk.Tk()
root.geometry('1400x900')
root.title('GUI  Aplikasi Pengolahan Citra')

title_label = tk.Label(root, text='Pilih gambar yang akan diperbaiki!')
title_label.place(x=550, y=20)
open_button = tk.Button(root, text='Pilih Gambar', command=open_image)
open_button.place(x=600, y=50)

correction_box = tk.LabelFrame(root, padx=5, pady=5)
correction_box.place(x=1170, y=100, width=200, height=650)
grayscale_button = tk.Button(correction_box, text='---- grayscale ----', command=lambda: process_image('grayscale'))
grayscale_button.pack(side=tk.TOP, pady=30)

thresholding_correction_button = tk.Button(correction_box, text='perbaikan threshold', command=lambda: process_image('thresholding_correction'))
thresholding_correction_button.pack(side=tk.TOP, pady=30)


brightness_button = tk.Button(correction_box, text='Peningkatan Kecerahan', command=lambda: process_image('brightness'))
brightness_button.pack(side=tk.TOP, pady=30)


difference_image_button = tk.Button(correction_box, text='perbedaan Gambar', command=lambda: process_image('difference_image'))
difference_image_button.pack(side=tk.TOP, pady=30)

sharpening_button = tk.Button(correction_box, text=' ---- Penajaman ----', command=lambda: process_image('sharpening'))
sharpening_button.pack(side=tk.TOP, pady=30)

noise_reduction_button = tk.Button(correction_box, text='mengurangi noise', command=lambda: process_image('noise_reduction'))
noise_reduction_button.pack(side=tk.TOP, pady=30)

median_filter_button = tk.Button(correction_box, text='--- median filter ---', command=lambda: process_image('median_filter'))
median_filter_button.pack(side=tk.TOP, pady=30)

result_box = tk.LabelFrame(root, padx=5, pady=5)
result_box.place(x=50, y=100, width=1100, height=650)

creator_box = tk.LabelFrame(root, text='Pembuat', padx=10, pady=5)
creator_box.place(x=800, y=10, width=315, height=60)

show_creator()

root.mainloop()