from core.errors import internal_server_error, not_found


class Router:
    def __init__(self):
        self.routes = {
            'get': [],
            'post': []
        }

    def add(self, http_method, url, ctrl, method):
        self.routes[http_method].append({
            'url': url,
            'ctrl': ctrl,
            'method': method
        })

    def get(self, *args):
        self.add('get', *args)

    def post(self, *args):
        self.add('post', *args)

    def run(self, request, response):
        http_method = request.method.lower()
        method_routes = self.routes.get(http_method)
        route = None
        for r in method_routes:
            if r['url'] == request.url:
                route = r
                break
        if not route:
            not_found(request, response)
        try:
            ctrl = route['ctrl'](request, response)
            getattr(ctrl, route['method'])()
        except BaseException as e:
            print(f'Тут у нас ошибка! {e.args}')
            internal_server_error(request, response, e)
