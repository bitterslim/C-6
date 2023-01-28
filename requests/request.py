from typing import BinaryIO
from urllib.parse import parse_qs


class Request:
    def __init__(self, file: BinaryIO):
        self.file = file
        self.method = ''
        self.url = ''
        self.protocol = ''
        self.headers = {}
        self.body = None
        self.parse_request_line()
        self.parse_headers()
        self.parse_body()

    def parse_body(self):
        content_length = self.headers.get("Content-Length")
        if content_length:
            self.body = self.file.read(int(content_length)).decode()
        self._parse_sprecific_body()

    def _parse_sprecific_body(self):
        if 'Content-Type' in self.headers and self.headers.get('Content-Type') == 'application/x-www-form-urlencoded':
            self.body = parse_qs(self.body)

    def parse_request_line(self):
        request_line = self.read_line()
        self.method, self.url, self.protocol = request_line.split()
        if self.protocol != 'HTTP/1.1':
            raise ValueError('Error, wrong protocol')

    def parse_headers(self):
        while True:
            header = self.read_line()
            if header == '':
                break
            name, value = header.split(': ')
            self.headers[name] = value

    def read_line(self):
        return self.file.readline().decode().strip()
