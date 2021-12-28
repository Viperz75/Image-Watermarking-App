from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
import PIL
from PIL import Image, ImageFont, ImageDraw


window = Tk()
window.title("Watermark")
window.minsize(230, 210)
window.resizable(0, 0)
window.iconbitmap("watermark.ico")


def open_file():
    try:
        image = fd.askopenfilename()
        image_to_watermark = PIL.Image.open(image)
        width = image_to_watermark.width
        height = image_to_watermark.height
        image_format = image_to_watermark.format

        def watermarked():
            # User inputs
            water_text = watermark.get()
            text_size = int(watermark_text_size.get())
            align = str(alignment.get())
            color = str(color_picking.get())
            title_text = water_text

            font = ImageFont.truetype("arial", text_size)
            image_editable = PIL.ImageDraw.Draw(image_to_watermark)

            # Watermark Alignments & Colors
            if align == "Top left corner":
                if color == "White":
                    image_editable.text((15, 15), title_text, (219, 219, 219), font=font)
                elif color == "Black":
                    image_editable.text((15, 15), title_text, (84, 84, 84), font=font)
            elif align == "Center":
                if color == "White":
                    image_editable.text(((width - text_size) / 2 - 100, (height - text_size) / 2),
                                        title_text, (219, 219, 219), font=font)
                elif color == "Black":
                    image_editable.text(((width - text_size) / 2 - 100, (height - text_size) / 2),
                                        title_text, (84, 84, 84), font=font)

            # Saving image by image format
            if image_format == "PNG":
                ask = fd.asksaveasfilename(filetypes=[("image file", "*.png")])
                image_to_watermark.save(f"{ask}.png")
                messagebox.showinfo(title="Saved", message="Image has been saved.")
            elif image_format == "JPG":
                ask = fd.asksaveasfilename(filetypes=[("image file", "*.jpeg")])
                image_to_watermark.save(f"{ask}.jpg")
                messagebox.showinfo(title="Saved", message="Image has been saved.")
            elif image_format == "JPEG":
                ask = fd.asksaveasfilename(filetypes=[("image file", "*.jpg")])
                image_to_watermark.save(f"{ask}.jpg")
                messagebox.showinfo(title="Saved", message="Image has been saved.")

        save_button = Button(window, image=save_button_image, width=30, command=watermarked, highlightthickness=0,
                             border=0)
        save_button.place(x=65, y=100)
        name_only = image.split("/")[2]
        image_label.config(text=f"{name_only}", font=("Arial", 5))

    except AttributeError:
        messagebox.showerror(title="Error", message="Please select an Image")


save_button_image = PhotoImage(file="images/save.png")

alignment = StringVar(window)
alignment.set("Center")
options = ttk.OptionMenu(window, alignment, "Center", "Center", "Top left corner")
options.place(x=20, y=140)

color_picking = StringVar(window)
color_picking.set("White")
color_options = ttk.OptionMenu(window, color_picking, "White", "White", "Black")
color_options.place(x=130, y=140)

image_label = Label(text="", fg="#0052e0")
image_label.place(x=20, y=175)

watermark = ttk.Entry(window)
watermark.insert(END, "Watermark Text")
watermark.place(x=50, y=60)

watermark_text_size = Scale(window, from_=0, to=80, orient="horizontal", highlightthickness=0, border=0)
watermark_text_size.place(x=50, y=0)

ask = PhotoImage(file="images/selection.png")
ask_button = Button(window, image=ask, width=30, command=open_file, highlightthickness=0, border=0)
ask_button.place(x=150, y=100)

window.mainloop()
