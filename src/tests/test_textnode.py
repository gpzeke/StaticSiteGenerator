import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_none_url(self):
        node = TextNode("Node to test url value is None", TextType.ITALIC)
        self.assertIsNone(node.url)

    def test_dif_text_type(self):
        node = TextNode("Node with images text type", TextType.IMAGE, url="/assets/test_image1.jpg")
        node2 = TextNode("Node with a code text type", TextType.CODE)
        self.assertNotEqual(node.text_type, node2.text_type)
    
    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )

    #########################
    # TextNodeToHTML Tests: #
    #########################

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text_to_html(self):
        node = TextNode("This should be a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertIsNone(html_node.tag)
        self.assertEqual(html_node.value, "This should be a text node")

    def test_bold_to_html(self):
        node = TextNode("This should be a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This should be a bold text node")

    def test_italic_to_html(self):
        node =  TextNode("This should be an italics text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This should be an italics text node")

    def test_code_to_html(self):
        node = TextNode("This should be a code block text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This should be a code block text node")

    def test_link_to_html(self):
        node = TextNode("This should be a link text node", TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This should be a link text node")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})

    def test_image_to_html(self):
        node = TextNode("This should be an image text node", TextType.IMAGE, "https://www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertIsNone(html_node.value)
        self.assertEqual(html_node.props, {"src": "https://www.google.com", "alt":"This should be an image text node"})

    # This won't work because the enum should fail. Not sure how I'd test this.
    # I'll have to ask somebody if this is just extra checking or unnecessary If.
    # it is necessary, I'll need to figure out how to test properly.
    #def test_default_case(self):
    #    node = TextNode("Broken node", TextType.FAKE)
    #    html_node = text_node_to_html_node(node)
    #    with self.assertRaises as cm:
    #        text_node_to_html_node(node)
    #    self.assertEqual(str(cm.exception), "type object 'TextType' has no attribute 'FAKE'")

if __name__ == "__main__":
    unittest.main()