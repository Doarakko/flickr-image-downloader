# flickr image download

```
data
├── cat
│   ├── cat.json
│   ├── cat_0.jpg
│   ├── cat_1.jpg
│   ├── cat_2.jpg
│   ├── cat_3.jpg
│   └── cat_4.jpg
├── dog
│   ├── dog.json
│   ├── dog_0.jpg
│   ├── dog_1.jpg
│   ├── dog_2.jpg
│   ├── dog_3.jpg
│   └── dog_4.jpg
└── queries.txt
```

## Requirments

- Python 3.8
- Poetry
- flickr API Key

## Usage

1. Enter your API Key to .env

```bash
mv .env.sample .env
```

2. Enter search keywords in the `data/queries.txt` separated by line breaks

```txt
dog
cat
```

3. Enter the number of images for each query to `get_image_url.py` 

```python
N = 5
```

4. Install Python package

```bash
poetry install
```

5. Request to flickr and get image url

```bash
poetry run python get_image_url.py
```

6. Download image

```bash
poetry run python download_image.py
```

## Reference

- [flickr API](https://www.flickr.com/services/api/)
