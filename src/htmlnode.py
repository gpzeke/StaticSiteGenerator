class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        # Child classes will override this method to render themselves as HTML
        raise NotImplementedError("Implement to_html method later.")
    
    def to_props(self):
        if self.props is None:
            return ""
        
        string = ""
        for prop in self.props:
            string += f" {prop}=\"{self.props[prop]}\""
        return string
    
    def __eq__(self, other):
        if isinstance(other, HTMLNode):
            return (
                self.tag == other.tag and
                self.value == other.value and
                self.children == other.children and
                self.props == other.props
            )
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if not self.value:
            raise ValueError("Value is required for leaf node")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.to_props()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag is required for a parent node")
        if not self.children:
            raise ValueError("Parent node must have children")
        
        child_string = ""
        for child in self.children:
            child_string += child.to_html()

        return f"<{self.tag}{self.to_props()}>{child_string}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
