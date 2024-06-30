import tkinter as tk
from tkinter import filedialog, messagebox

from convertor.img_to_dxf import convert_image_to_dxf


class ImageToDXFApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to DXF Converter")

        # Создаем и размещаем элементы интерфейса
        self.create_widgets()

    def create_widgets(self):
        # Метка и поле для ввода пути к изображению
        self.image_path_label = tk.Label(
            self.root,
            text="Image Path:"
            )
        self.image_path_label.grid(
            row=0,
            column=0,
            padx=10,
            pady=5,
            sticky=tk.W
            )

        self.image_path_entry = tk.Entry(
            self.root,
            width=50
            )
        self.image_path_entry.grid(
            row=0,
            column=1,
            padx=10,
            pady=5
            )

        self.browse_image_button = tk.Button(
            self.root,
            text="Browse",
            command=self.browse_image
            )
        self.browse_image_button.grid(
            row=0,
            column=2,
            padx=10,
            pady=5
            )

        # Метка и поле для ввода пути для сохранения DXF
        self.dxf_path_label = tk.Label(
            self.root,
            text="DXF Path:"
            )
        self.dxf_path_label.grid(
            row=1,
            column=0,
            padx=10,
            pady=5,
            sticky=tk.W
            )

        self.dxf_path_entry = tk.Entry(
            self.root,
            width=50
            )
        self.dxf_path_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=5
            )

        self.browse_dxf_button = tk.Button(
            self.root,
            text="Browse",
            command=self.browse_dxf
            )
        self.browse_dxf_button.grid(
            row=1,
            column=2,
            padx=10,
            pady=5
            )

        # Кнопка для запуска конвертации
        self.convert_button = tk.Button(
            self.root,
            text="Convert",
            command=self.convert
            )
        self.convert_button.grid(
            row=2,
            column=0,
            columnspan=3,
            pady=20
            )

    def browse_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp")]
            )
        if file_path:
            self.image_path_entry.delete(0, tk.END)
            self.image_path_entry.insert(0, file_path)

    def browse_dxf(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".dxf",
            filetypes=[("DXF files", "*.dxf")]
            )
        if file_path:
            self.dxf_path_entry.delete(0, tk.END)
            self.dxf_path_entry.insert(0, file_path)

    def convert(self):
        image_path = self.image_path_entry.get()
        dxf_path = self.dxf_path_entry.get()

        if not image_path or not dxf_path:
            messagebox.showerror(
                "Error",
                "Both image path and DXF path must be provided."
                )
            return

        try:
            convert_image_to_dxf(image_path, dxf_path)
            messagebox.showinfo(
                "Success",
                f"Successfully converted '{image_path}' to '{dxf_path}'."
                )
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Failed to convert '{image_path}' to DXF. {e}"
                )


if __name__ == '__main__':
    root = tk.Tk()
    app = ImageToDXFApp(root)
    root.mainloop()
