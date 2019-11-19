from mintersdk.minterapi import MinterAPI

from config import MINTER_NODE_API_URL, MINTER_NODE_API_HEADERS


class MinterAPIService(MinterAPI):
    request_headers = MINTER_NODE_API_HEADERS

    def _request(self, command, request_type='get', **kwargs):
        kwargs['headers'] = self.request_headers
        return super()._request(command, request_type=request_type, **kwargs)['result']


MinterNode = MinterAPIService(MINTER_NODE_API_URL)
