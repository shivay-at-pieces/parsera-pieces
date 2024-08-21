from parsera_pieces import Parsera

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