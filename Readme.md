# ImageLoot (Your one-click gateway to web images and their tales)

## Overview
Welcome to ImageLoot - your ultimate visual web scraper designed to crawl, capture, and collect stunning images from any URL you throw at it. Transform URLs into a treasure trove of pixels, unlocking the beauty hidden within websites, one image at a time.

Whether you're looking to build an image dataset, gather visuals for a project, or simply explore the web's photographic gems, ImageLoot is your go-to tool for seamless image extraction.
[Watch the demo video](./imageLoot.mp4)
<video src="./imageLoot.mp4" autoplay muted playsinline></video>

## Features 
- **Easy Crawling** - Extract all images from any given webpage URL.
- **Detailed Capture** - Retrieve image sources `(src)` along with descriptive alternate text `(alt)`.
- **Clean output** - Get image data organized neatly in JSON format for easy use.
- **Tested on real sites** - Successfully tested on Wikipedia and NIT Patna's official website to ensure robustness and reliability.

## Sample Output 
```json
[
  {
    "src": "https://example.com/image1.jpg",
    "alt": "A cute puppy on the grass"
  },
  {
    "src": "https://example.com/image2.jpg",
    "alt": "Sunset over the mountains"
  }
]
```

## Installations
### Using Docker
```bash
docker build -t image_loot .
```
```bash
docker run image_loot
```

### Using Terminal 
1.Clone the repository:
```bash
clone the repository
```

2.Install Dependencies
```bash
pip install -r requirements.txt
```

3.Running up the application
```bash
python ImageLootGui.py
```

## Use Cases
- Build Datasets for machine learning or computer vision.
- collect images for content curation.
- Rapidly gather media for design inspiration.
- Education projects involving web scraping and data extraction.

## License 
This project is open-source and available under the MIT License.

