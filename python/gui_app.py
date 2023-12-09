import os
import tkinter as tk
from tkinter import PhotoImage
import pystray
from pystray import MenuItem as item
from PIL import Image

def show_image():
    image_label.config(image=crystal_sword)

# Tkinterウィンドウの作成
root = tk.Tk()
root.title("Azure GUI")
root.geometry("960x540")  # 幅300ピクセル、高さ200ピクセル

# 画像の読み込み
azure = PhotoImage(file="python/assets/azure.png")
crystal_sword = PhotoImage(file="python/assets/crystal_sword.png")

# アイコンを設定
root.iconbitmap(default="python/assets/icon.ico")

# 画像を表示するためのラベル
image_label = tk.Label(root, image=azure)
image_label.pack()

# 画像を表示するボタン
show_button = tk.Button(root, text="Show Image", command=show_image)
show_button.pack()

root.mainloop()