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

    def test_tags(self):
        self.assertEqual(self.html_node1.tag, "p", f"""Node1 tag is not a paragraph tag: "p""")
        self.assertEqual(self.html_node2.tag, "a", f"""Node2 tag is not a link tag: "a""")
        self.assertEqual(self.html_node3.tag, "h1", f"""Node3 tag is not a header 1 tag: "h1""")

    def test_value(self):
        self.assertEqual(type(self.html_node1.value), str or None, "Node1 value is not a string or type of None" )
        self.assertEqual(type(self.html_node2.value), str or None, "Node2 value is not a string or type of None" )
        self.assertEqual(type(self.html_node3.value), str or None, "Node3 value is not a string or type of None" )

    def test_props(self):
        self.assertEqual(self.html_node1.props, None, f"Props is not of type None")
        self.assertEqual(isinstance(self.html_node2.props, dict), True, f"Props are not a dictionary")
        self.assertEqual(self.html_node3.props, None, f"Props is not of type None")

if __name__ == "__main__":
    unittest.main()