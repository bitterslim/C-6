import os.path
from glob import glob

from core.settings import STATIC_URL
from requests.request import Request
from requests.response import Response


class StaticResponder:
    def __init__(self, request: Request, response: Response):
        self.request = request
        self.response = response
        self.static_dir = STATIC_URL
        self.file = None
        self._check_file()

    def _check_file(self):
        # /www/media/avatar/user/1/example.png
        file_url = self.request.url.replace('..', '')
        path = './' + self.static_dir + file_url
        files = glob(path)
        if len(files) > 0 and os.path.isfile(files[0]):
            self.file = files[0]

    def prepare_response(self):
        if self.file:
            file = open(self.file, 'rb')
            self.response.set_file_body(file)
