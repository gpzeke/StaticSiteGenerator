from enum import Enum, auto

class NodeType(Enum):
    HTML = "html"
    LEAF = "leaf"
    TEXT = "text"

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALICS = "italics"
    CODE = "code"
    LINKS = "links"
    IMAGES = "images"

class TextNode():
    def __init__(self, text, text_type, url=None):
        if not isinstance(text_type, TextType):
            raise TypeError(f"{text_type} must be an instance of TextType Enum.")
        self.text = text
        self.text_type = text_type.value
        self.url = url

    def __eq__(self, other):
        if isinstance(other, TextNode):
            return (
                self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url
            )
        return False
    
    def __repr__(self) :
        return f"TextNode({self.text}, {self.text_type}, {self.url})"