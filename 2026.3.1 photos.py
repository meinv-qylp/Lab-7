import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO
import random


def load_image(): # 点击按钮时调用的函数
    try:
        button.config(text="loading...", state=tk.DISABLED)
        root.update()

        categories = ["neko", "waifu", "husbando", "kitsune", 
                      "shinobu", "kanna", "cosplay", "nekopara"]
        category = random.choice(categories) # 获取图片

        response = requests.get(f"https://nekos.best/api/v2/{category}", timeout=10)
        data = response.json()
        img_url = data['results'][0]['url'] # 下载图片
        print(img_url)

        img_response = requests.get(img_url, timeout=10)
        img = Image.open(BytesIO(img_response.content))
        img.thumbnail((500, 500)) # 显示图片
        
        photo = ImageTk.PhotoImage(img)
        label.config(image=photo)
        label.image = photo

    except Exception as e:
        label.config(text=f"error: {e}")

    finally:
        button.config(text="change", state=tk.NORMAL)


root = tk.Tk()
root.title("random picture")
root.geometry("600x600")


label = tk.Label(root, text="click to get an image", font=("Arial", 16))
label.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)


button = tk.Button(root, text="change", command=load_image, 
                   font=("Arial", 14), padx=20, pady=10)
button.pack(pady=20)


root.mainloop()