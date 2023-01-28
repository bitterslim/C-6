from os import fstat

from requests import HTTPResponseCode, PROTOCOL


class Response:
    def __init__(self, file):
        self.file = file
        self.status = HTTPResponseCode.OK
        self.headers = []
        self.body = None
        self.file_body = None

    def set_status(self, status: HTTPResponseCode):
        self.status = status

    def send(self):
        headers = self._get_response_headers()
        self.file.write(headers)
        if self.body:
            self.file.write(self.body)
        elif self.file_body:
            self._write_file_body()

    def add_header(self, name, value):
        self.headers.append({'name': name, 'value': value})

    def set_body(self, body):
        self.body = body.encode()
        self.add_header('Content-Length', len(self.body))

    def set_file_body(self, file):
        self.file_body = file
        size = fstat(file.fileno()).st_size
        self.add_header('Content-Length', size)

    def _get_response_headers(self):
        status_line = self._set_status_line()
        headers = [status_line]
        for header in self.headers:
            headers.append(f"{header.get('name')}: {header.get('value')}")
        head_str = '\r\n'.join(headers)
        head_str += '\r\n\r\n'
        return head_str.encode()

    def _set_status_line(self):
        return f"{PROTOCOL} {self.status.code} {self.status.message}"

    def _write_file_body(self):
        while True:
            data = self.file_body.read(1024)
            if not data:
                break
            self.file.write(data)
