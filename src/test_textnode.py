import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):

    def setUp(self):
        self.expected_type = "italics"
        self.expected_url = "https://www.google.com"
        
        self.text_node = TextNode("Type test", TextType.ITALICS, "https://www.google.com")

    def test_eq(self):
        node = self.text_node
        node2 = self.text_node
        self.assertEqual(node, node2)

    def test_type(self):
        self.assertEqual(self.text_node.text_type, self.expected_type, f"Text_type: {self.expected_type} does not match expected text_type: {self.text_node.text_type}." )

    def test_url(self):
        self.assertEqual(self.text_node.url, self.expected_url, f"URL: {self.expected_url} does not match expected text_type: {self.text_node.url}.")

if __name__ == "__main__":
    unittest.main()