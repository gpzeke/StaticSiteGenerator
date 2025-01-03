from textnode import TextNode, TextType
from htmlnode import *

def main():
    test_text_node = TextNode("This is a text node", TextType.ITALIC, "http://google.com")
    html_node = HTMLNode.text_node_to_html_node(test_text_node)
    print(test_text_node)
    #node = ParentNode(
    #"p",
    #[
    #    LeafNode("b", "Bold text"),
    #    LeafNode(None, "Normal text"),
    #    LeafNode("i", "italic text"),
    #    LeafNode(None, "Normal text"),
    #],
#)
    #print(node.to_html())

if __name__ == "__main__":
    main()