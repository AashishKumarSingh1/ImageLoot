import os
import json
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

class ImageLoot:
    def __init__(self, base_url, unique_name):
        self.base_url = base_url
        self.unique_name = unique_name or base_url

    def get_html(self):
        try:
            response = requests.get(self.base_url)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"[ERROR] HTML fetch failed: {e}")
            return None

    def get_images(self):
        html_content = self.get_html()
        if not html_content:
            return []

        soup = BeautifulSoup(html_content, 'html.parser')
        images = []
        seen_urls = set()

        for img in soup.find_all("img"):
            src = img.get("src")
            alt = img.get("alt", "")
            if not src:
                continue
            full_url = urljoin(self.base_url, src)
            if full_url not in seen_urls:
                seen_urls.add(full_url)
                images.append({"url": full_url, "alt": alt})

        return images

    def save_images(self):
        images = self.get_images()
        if not images:
            return False

        data = {
            "base_url": self.base_url,
            "unique_name": self.unique_name,
            "images": images
        }
        filename = f"{self.unique_name}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        return True

    def load_saved_images(self):
        filename = f"{self.unique_name}.json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data.get("images", [])

