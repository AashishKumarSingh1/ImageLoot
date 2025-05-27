import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from template import ImageLoot

class ImageLootGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ImageLoot")
        self.root.geometry("800x600")
        self.root.config(bg="#f8f8f8")

        self.images = []

        self.setup_ui()

    def setup_ui(self):
        ttk.Label(self.root, text="Enter URL:", font=("Arial", 12)).pack(pady=(10, 0))
        self.url_entry = ttk.Entry(self.root, width=80)
        self.url_entry.pack(pady=5)

        ttk.Label(self.root, text="Unique Name:", font=("Arial", 12)).pack(pady=(10, 0))
        self.name_entry = ttk.Entry(self.root, width=40)
        self.name_entry.pack(pady=5)

        btn_frame = ttk.Frame(self.root)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Scrape Images", command=self.scrape_images).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Save to JSON", command=self.save_images).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Load Saved", command=self.load_saved_images).pack(side="left", padx=5)

        self.image_list = scrolledtext.ScrolledText(self.root, width=100, height=20, wrap=tk.WORD)
        self.image_list.pack(pady=10)

    def scrape_images(self):
        url = self.url_entry.get().strip()
        name = self.name_entry.get().strip()
        if not url or not name:
            messagebox.showerror("Input Error", "Please provide both URL and a unique name.")
            return

        self.loot = ImageLoot(url, name)
        self.images = self.loot.get_images()
        self.display_images()

    def save_images(self):
        if not hasattr(self, "loot"):
            messagebox.showwarning("Warning", "Scrape images before saving.")
            return
        success = self.loot.save_images()
        if success:
            messagebox.showinfo("Saved", "Images saved to JSON.")
        else:
            messagebox.showerror("Save Error", "No images to save.")

    def load_saved_images(self):
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror("Input Error", "Please enter the unique name to load.")
            return
        self.loot = ImageLoot("", name)
        self.images = self.loot.load_saved_images()
        self.display_images()

    def display_images(self):
        self.image_list.delete(1.0, tk.END)
        if not self.images:
            self.image_list.insert(tk.END, "No images found.\n")
            return
        for idx, img in enumerate(self.images, 1):
            self.image_list.insert(tk.END, f"{idx}. URL: {img['url']}\n")
            self.image_list.insert(tk.END, f"   Alt: {img['alt'] or 'N/A'}\n\n")
        self.image_list.insert(tk.END, f"\n Total Images Found: {len(self.images)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageLootGUI(root)
    root.mainloop()
