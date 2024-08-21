# 📦 Parsera with Pieces

Fork of Parsera - Lightweight Python library for scraping websites with LLMs, specifically using Pieces QGPT endpoint.  

## Why Parsera with Pieces?
Because it's simple and lightweight, with minimal token use which boosts speed and reduces expenses.

## Installation

```shell
pip install parsera-pieces
playwright install
```

## Basic usage

You can do this from python with:
```python
from parsera.main import Parsera

async def main():
       url = "https://code.pieces.app/blog"
       elements = {
           "Blog Title": "Title of the blog",
           "Blog Author": "Author of the specific blog post",
           "Published Date": "Date when the project was published",
       }

       scraper = Parsera(None)
       result = await scraper.arun(url=url, elements=elements)
       print(result)

if __name__ == "__main__":
       import asyncio
       asyncio.run(main())
```
