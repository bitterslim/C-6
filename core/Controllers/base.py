import jinja2

from core.settings import ROOT_PATH


class Controller:
    def __init__(self, request, response):
        self.request = request
        self.response = response
        self.builder = jinja2.Environment()

    def render_body(self, template_name, **ctx):
        template_path = ROOT_PATH + '/templates/' + template_name
        self.response.add_header('Content-Type', 'text/html')
        with open(template_path, 'r') as file:
            template_body = file.read()
            template = self.builder.from_string(template_body)
            return template.render(context=ctx)
