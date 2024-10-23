from textnode import *
from htmlnode import *

def main():
    new_node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    new_node2 = HTMLNode("a", "This is a link", props={"href":"https://www.google.com"})
    new_node3 = LeafNode("a", "This is a link", props={"href":"https://www.google.com"})
    new_node4 = ParentNode("p", new_node3, {"href":"https://www.google.com", "href":"https://www.bing.com"})
    #print(new_node)
    #print(HTMLNode.props_to_html(new_node2.props))
    #print(new_node4.to_html())

if __name__ == "__main__":
    main()