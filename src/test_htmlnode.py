import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def setUp(self):
        self.expected_tag = "a"
        self.expected_value = "This is a link"
        self.expected_props = {"href":"https://www.google.com"}

        self.html_node1 = HTMLNode(
            "p",
            "This is the body of a paragraph",
        )
        self.html_node2 = HTMLNode(
            "a",
            "This is a link",
            props = {"href":"https://www.google.com"}
        )
        self.html_node3 = HTMLNode(
            "h1",
            "This is some heading"
        )

    def test_props(self):
        self.assertEqual(self.html_node1.props, None, f"Props is not None")
        # self.html_node1.props

if __name__ == "__main__":
    unittest.main()