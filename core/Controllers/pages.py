from core.Controllers.base import Controller


class PagesController(Controller):
    def home(self):
        body = self.render_body('home.html')
        self.response.set_body(body)

    def about(self):
        self.response.set_body('<h1>This is about page</h1>')
