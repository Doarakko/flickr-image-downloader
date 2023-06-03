# flickr image download

```text
data
├── cat.json
├── dog.json
├── images
│   ├── cat
│   │   ├── 33415747642.jpg
│   │   ├── 37204248186.jpg
│   │   ├── 38374394775.jpg
│   │   ├── 45591380462.jpg
│   │   └── 46106952034.jpg
│   └── dog
│       ├── 32996282558.jpg
│       ├── 33164281888.jpg
│       ├── 39731736542.jpg
│       ├── 40693090171.jpg
│       └── 45160323522.jpg
└── queries.txt
```

## Requirments

- Python 3.11
- flickr API Key

## Usage

### 1. Enter your API Key and number of images to download per query to `.env`

```bash
mv .env.sample .env
```

### 2. Enter search keywords in the `data/queries.txt` separated by line breaks

```bash
mv data/queries.txt.sample data/queries.txt
```

```txt
dog
cat
```

### 4. Install Python package

```bash
poetry install
```

### 5. Request to flickr and get image url

```bash
poetry run python get_image_url.py
```

### 6. Download image

```bash
poetry run python download_image.py
```

## Reference

- [flickr API](https://www.flickr.com/services/api/)
