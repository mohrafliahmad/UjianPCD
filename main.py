import cv2
import tkinter as tk
from tkinter import filedialog


def open_image():
    global img
    filename = filedialog.askopenfilename(initialdir="/", title="Select a file",
                                          filetypes=[("Image files", ".jpg;.jpeg;*.png")])
    img = cv2.imread(filename)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def contrast_image():
    global img
    alpha = 1.5  # Menentukan nilai kontras
    beta = 0  # Menentukan nilai kecerahan
    img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    cv2.imshow("Contrast Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def flip_image():
    global img
    img = cv2.flip(img, 1)
    cv2.imshow("Flipped Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def save_image():
    global img
    filename = filedialog.asksaveasfilename(initialdir="/", title="Save as",
                                            filetypes=[("Image files", ".jpg;.jpeg;*.png")])
    cv2.imwrite(filename, img)


root = tk.Tk()
root.title("Image Processing")
root.geometry("300x100")

open_button = tk.Button(root, text="Open", command=open_image)
open_button.pack(side="left", padx=5, pady=5)

contrast_button = tk.Button(root, text="Contrast", command=contrast_image)
contrast_button.pack(side="left", padx=5, pady=5)

save_button = tk.Button(root, text="Save", command=save_image)
save_button.pack(side="left", padx=5, pady=5)

flip_button = tk.Button(root, text="Flip", command=flip_image)
flip_button.pack(side="left", padx=5, pady=5)

root.mainloop()