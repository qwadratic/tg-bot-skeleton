from threading import Thread
import requests
import time

urls = [
    'https://explorer-api.apps.minter.network/api/v1/addresses/Mx1d2111ef33c0735ae6d97a8a7948a43cca3a4bd1',
    'https://explorer-api.apps.minter.network/api/v1/addresses/Mxad04920bcce213feb275a7c68f81b67e66af71c1',
    'https://explorer-api.apps.minter.network/api/v1/addresses/Mxb595ff97464f2e7513b44b7209357ae3e9ce21a7',
]


class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return


def fetch_url(url):
    r = requests.get(url)
    print("{} fetched in {}".format(url, time.time() - start))
    return r.json()


start = time.time()
threads = []
for url in urls:
    threads.append(ThreadWithReturnValue(target=fetch_url, args=(url,)))

results = []
for thread in threads:
    thread.start()
for thread in threads:
    results.append(thread.join())

print(results)
print("Elapsed Time: {}".format(time.time() - start))

