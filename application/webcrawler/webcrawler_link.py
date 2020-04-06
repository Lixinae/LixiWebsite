class Link:
    def __init__(self, url, is_visited=False):
        self._url = url
        self._name = url.split('/').pop()
        self._isVisited = is_visited

    def __repr__(self) -> str:
        return '{url:' + self._url + ',name:' + self._name + ',isVisited:' + str(self._isVisited) + '}'

    def __str__(self) -> str:
        return 'Link(url=' + self._url + ', filename=' + str(self._name) + ', isVisited=' + str(self._isVisited) + ')'

    def set_visited(self):
        self._isVisited = True

    def is_visited(self) -> bool:
        return self._isVisited

    def get_name(self):
        return self._name

    def get_url(self):
        return self._url

    def as_json(self):
        return {'url': self._url, 'name': self._name, 'isVisited': self._isVisited}
