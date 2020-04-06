import enum


# Enumeration pour indiquer quel type de lien on a visité
class LinkEnum(enum.Enum):
    AHref = 0
    Img = 1


class Link:
    def __init__(self,
                 url: str,
                 type_link: LinkEnum = LinkEnum.AHref,
                 is_visited: bool = False):
        self._url = url
        self._name = url.split('/').pop()
        self._isVisited = is_visited
        self.type_link = type_link

    def __repr__(self) -> str:
        return '{url:' + self._url + \
               ', name:' + self._name + \
               ', isVisited:' + str(self._isVisited) + \
               ', LinkEnum:' + str(self.type_link) + '}'

    def __str__(self) -> str:
        return 'Link(url=' + self._url \
               + ', filename=' + str(self._name) \
               + ', isVisited=' + str(self._isVisited) \
               + ', LinkEnum:' + str(self.type_link) + ')'

    def set_visited(self):
        self._isVisited = True

    def is_visited(self) -> bool:
        return self._isVisited

    def get_name(self) -> str:
        return self._name

    def get_url(self) -> str:
        return self._url

    def as_json(self):
        return {'url': self._url, 'name': self._name, 'isVisited': self._isVisited}

    def is_img(self) -> bool:
        return self.type_link == LinkEnum.Img

    def is_ahref(self) -> bool:
        return self.type_link == LinkEnum.AHref
