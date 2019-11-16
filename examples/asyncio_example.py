from time import time

import aiohttp
import asyncio

from requests import get


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = [
        'https://minter-scoring.space/api/Mx1d2111ef33c0735ae6d97a8a7948a43cca3a4bd1',
        'https://explorer-api.apps.minter.network/api/v1/addresses/Mx1d2111ef33c0735ae6d97a8a7948a43cca3a4bd1',
        'https://minter-scoring.space/api/Mx1d2111ef33c0735ae6d97a8a7948a43cca3a4bd1',
        'https://explorer-api.apps.minter.network/api/v1/addresses/Mx1d2111ef33c0735ae6d97a8a7948a43cca3a4bd1',
        'https://minter-scoring.space/api/Mx1d2111ef33c0735ae6d97a8a7948a43cca3a4bd1',
        # 'https://explorer-api.apps.minter.network/api/v1/addresses/Mx1d2111ef33c0735ae6d97a8a7948a43cca3a4bd1',
        # 'https://minter-scoring.space/api/Mx1d2111ef33c0735ae6d97a8a7948a43cca3a4bd1',
        # 'https://explorer-api.apps.minter.network/api/v1/addresses/Mx1d2111ef33c0735ae6d97a8a7948a43cca3a4bd1',
        # 'https://minterscan.pro/addresses/Mx1d2111ef33c0735ae6d97a8a7948a43cca3a4bd1/icon'
    ]
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch(session, url))
        responses = await asyncio.gather(*tasks)
        # for r in responses:
        #     print(r)


def sync():
    r1 = get('https://minter-scoring.space/api/Mx1d2111ef33c0735ae6d97a8a7948a43cca3a4bd1')
    r2 = get('https://explorer-api.apps.minter.network/api/v1/addresses/Mx1d2111ef33c0735ae6d97a8a7948a43cca3a4bd1')
    r3 = get('https://minter-scoring.space/api/Mx1d2111ef33c0735ae6d97a8a7948a43cca3a4bd1')
    r4 = get('https://explorer-api.apps.minter.network/api/v1/addresses/Mx1d2111ef33c0735ae6d97a8a7948a43cca3a4bd1')
    r5 = get('https://minter-scoring.space/api/Mx1d2111ef33c0735ae6d97a8a7948a43cca3a4bd1')
    # r6 = get('https://explorer-api.apps.minter.network/api/v1/addresses/Mx1d2111ef33c0735ae6d97a8a7948a43cca3a4bd1')
    # r7 = get('https://minter-scoring.space/api/Mx1d2111ef33c0735ae6d97a8a7948a43cca3a4bd1')
    # r8 = get('https://explorer-api.apps.minter.network/api/v1/addresses/Mx1d2111ef33c0735ae6d97a8a7948a43cca3a4bd1')
    # r3 = get('https://minterscan.pro/addresses/Mx1d2111ef33c0735ae6d97a8a7948a43cca3a4bd1/icon')
    # print(r1.json())
    # print(r2.json())
    # print(r3.json())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    t = time()
    loop.run_until_complete(main())
    dt = time() - t
    print('--------- done in', dt, 'seconds')

    t = time()
    sync()
    dt = time() - t
    print('--------- done in', dt, 'seconds')
