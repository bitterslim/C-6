import json
import random

from core.Controllers.base import Controller
from core.db import Database
from core.errors import not_found
from requests import HTTPResponseCode


class MakesController(Controller):
    def makes(self, pk=None):
        makes_db = Database.makes
        if not pk:
            body = self.render_body('makes.html', **{'makes': makes_db})
            self.response.set_body(body)
            return
        make = Database.get_make_by_pk(pk)
        if make:
            body = self.render_body('makes.html', **{'make': make})
            self.response.set_body(body)
        else:
            not_found(self.request, self.response)

    def add_make(self):
        body = self.render_body('add_makes.html')
        self.response.set_body(body)

    def add(self):
        print(self.request.body)
        makes = {
            'id': Database.id + 1,
            'make': self.request.body.get('make')[0],
            'year': int(self.request.body.get('year')[0]),
            'price': int(self.request.body.get('price')[0]),
            'image': self.request.body.get('image')[0],
            'description': self.request.body.get('description')[0],
            'contacts': self.request.body.get('contacts')[0]
        }
        Database.add(makes)
        self.response.set_status(HTTPResponseCode.MOVED_PERMANENTLY)
        self.response.add_header('location', '/')