class HTMLNode:
    def __init__(
        self,
        tag: str = None,
        value: str = None,
        children: list = None,
        props: dict = None,
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        p = ""
        for k in self.props:
            if self.props[k]:
                p += f' {k}="{self.props[k]}"'
        return p

    def __repr__(self):
        print(self.tag, self.value, self.children, self.props)
