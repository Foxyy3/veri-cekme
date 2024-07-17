import tkinter as tk
from tkinter import ttk, scrolledtext
import requests
from bs4 import BeautifulSoup

class WebScraperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Web Scraping Uygulaması")
        self.root.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        # URL girişi
        self.url_label = ttk.Label(self.root, text="URL:", font=("Arial", 12))
        self.url_label.pack(pady=10)
        self.url_entry = ttk.Entry(self.root, width=70, font=("Arial", 12))
        self.url_entry.pack(pady=5)

        # Veri çek butonu
        self.scrape_button = ttk.Button(self.root, text="Veri Çek", command=self.scrape_data)
        self.scrape_button.pack(pady=10)

        # Sonuçları gösteren metin alanı
        self.result_text = scrolledtext.ScrolledText(self.root, width=100, height=20, wrap=tk.WORD, font=("Arial", 12))
        self.result_text.pack(padx=10, pady=10)

    def scrape_data(self):
        url = self.url_entry.get().strip()
        if not url:
            tk.messagebox.showerror("Hata", "Geçerli bir URL girin.")
            return

        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            data = ""

            # Örnek olarak başlık etiketlerini çekme
            titles = soup.find_all('h2')
            for title in titles:
                data += f"{title.text}\n\n"

            # Metin alanına sonuçları yazdırma
            self.result_text.delete('1.0', tk.END)
            self.result_text.insert(tk.END, data)
        except Exception as e:
            tk.messagebox.showerror("Hata", f"Veri çekme işlemi sırasında bir hata oluştu:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WebScraperApp(root)
    root.mainloop()
