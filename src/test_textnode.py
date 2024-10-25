import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import *

class TestTextNode(unittest.TestCase):

    def setUp(self):
        self.expected_type = "italic"
        self.expected_url = "https://www.google.com"
        
        self.text_node = TextNode("Type test", TextType.ITALIC, "https://www.google.com")

    def test_eq(self):
        node = self.text_node
        node2 = self.text_node
        self.assertEqual(node, node2)

    def test_type(self):
        self.assertEqual(self.text_node.text_type, self.expected_type, f"Text_type: {self.expected_type} does not match expected text_type: {self.text_node.text_type}." )

    def test_url(self):
        self.assertEqual(self.text_node.url, self.expected_url, f"URL: {self.expected_url} does not match expected text_type: {self.text_node.url}.")

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_node_to_html_node(self):
        text_node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(html_node.tag, None, "TEXT TextType is improperly handled")
        self.assertEqual(html_node.value, "This is a text node", "TEXT TextType is improperly handled")
        self.assertEqual(html_node, LeafNode(None, "This is a text node", None))

    def test_bold_node(self):
        bold_node = TextNode("this is a bold node.", TextType.BOLD, "www.fuck.com")
        html_node = text_node_to_html_node(bold_node)
        self.assertEqual(html_node, LeafNode("b", "this is a bold node.", None))

    def test_italic_node(self):
        italic_node = TextNode("This is an italics node.", TextType.ITALIC, "www.italics.com")
        html_node = text_node_to_html_node(italic_node)
        self.assertEqual(html_node, LeafNode("i", "This is an italics node.", None))

    def test_code_node(self):
        code_node = TextNode("This is a code node.", TextType.CODE, "www.code.com")
        html_node = text_node_to_html_node(code_node)
        self.assertEqual(html_node, LeafNode("code", "This is a code node.", None))

    def test_link_node(self):
        link_node = TextNode("This is a link node.", TextType.LINK, "www.link.com")
        html_node = text_node_to_html_node(link_node)
        self.assertEqual(html_node, LeafNode("a", "This is a link node.", {"href":"www.link.com"}))

    def test_image_node(self):
        image_node = TextNode("This is an image node.", TextType.IMAGE, "www.image.com")
        html_node = text_node_to_html_node(image_node)
        self.assertEqual(
            html_node,
            LeafNode(
                "img",
                "",
                {
                    "src":"www.image.com",
                    "alt":"This is an image node."
                }
            )
        )

if __name__ == "__main__":
    unittest.main()