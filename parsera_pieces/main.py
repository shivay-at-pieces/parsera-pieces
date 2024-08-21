import asyncio



from parsera_pieces.engine.model import PiecesModel
from parsera_pieces.engine.simple_extractor import TabularExtractor
from parsera_pieces.page import fetch_page_content


class Parsera:
    def __init__(self, model: None):
        if model is None:
            self.model = PiecesModel()
        else:
            self.model = model

    async def _run(
        self, url: str, elements: dict, proxy_settings: dict | None = None
    ) -> dict:
        if proxy_settings:
            content = await fetch_page_content(url=url, proxy_settings=proxy_settings)
        else:
            content = await fetch_page_content(url=url)
        extractor = TabularExtractor(
            elements=elements, model=self.model, content=content
        )
        result = await extractor.run()
        return result

    def run(self, url: str, elements: dict, proxy_settings: dict | None = None) -> dict:
        return asyncio.run(
            self._run(url=url, elements=elements, proxy_settings=proxy_settings)
        )

    async def arun(
        self, url: str, elements: dict, proxy_settings: dict | None = None
    ) -> dict:
        return await self._run(
            url=url, elements=elements, proxy_settings=proxy_settings
        )
