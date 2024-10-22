from textnode import *
from htmlnode import *

def main():
    new_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    new_node2 = HTMLNode("a", "This is a link", props={"href":"https://www.google.com"})
    print(new_node)
    print(HTMLNode.props_to_html(new_node2.props))

if __name__ == "__main__":
    main()