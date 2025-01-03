import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_default_behavior(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_to_props(self):
        node = HTMLNode("a", "link", None, {
            "href":"https://www.food.gpzeke.com",
            "target":"_blank",
            "hreflang":"en",
            "type":"web app",
        })
        self.assertEqual(
            node.to_props(),
            " href=\"https://www.food.gpzeke.com\" target=\"_blank\" hreflang=\"en\" type=\"web app\""
        )

    def test_eq_false(self):
        node = HTMLNode("a", "link", None, {
            "href":"https://www.food.gpzeke.com",
            "target":"_blank",
            "hreflang":"en",
            "type":"web app",
        })
        node2 = HTMLNode("p", "This paragraph will contain a child link", node)
        self.assertNotEqual(node, node2)

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    ###################
    # LeafNode Tests: #
    ###################

    def test_leaf_init(self):
        node = LeafNode("a", "link", {"href":"https://www.food.gpzeke.com"})
        self.assertEqual(node, LeafNode("a", "link", props={"href":"https://www.food.gpzeke.com"}))

    def test_no_tag(self):
        node = LeafNode("", "random text")
        self.assertEqual(node.to_html(), "random text")

    def test_no_value(self):
        node = LeafNode("a", "", {"href":"https://www.food.gpzeke.com"})
        self.assertRaises(ValueError)

    def test_repr(self):
        node = LeafNode("a", "link", {"href":"https://www.food.gpzeke.com"})
        self.assertEqual(
            node.__repr__(),
            "LeafNode(a, link, children: None, {'href': 'https://www.food.gpzeke.com'})"
        )

    ####################
    # ParentNode tests #
    ####################

    def test_parent_init(self):
        child1 = LeafNode("p", value="This is an LeafNode")
        child2 = LeafNode("p", value="This is a LeafNode2")
        node = ParentNode(
            "a",
            [child1, child2],
        )
        self.assertEqual(
            node,
            ParentNode("a", children=[child1, child2])
        )

    def test_challenge_code(self):
        node = ParentNode(
        "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node,
            ParentNode(
            "p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )       
        )
    
    def test_nested_parents(self):
        node = ParentNode(
            "p",
            [
                ParentNode(
                    "code",
                    [
                        LeafNode("b", "Bold text at the end of a nested Parent node."),
                        LeafNode("i", "Italics text at the end of a nested Parent node, after bold text."),

                    ]
                ),
                LeafNode("b", "Bold text in the top level Parent node."),
                LeafNode("i", "Italics text after bold text in the top level Parent node.")
            ],
            {"href":"https://www.google.com"},
        )
        node_html = node.to_html()
        raw_html = '<p href="https://www.google.com"><code><b>Bold text at the end of a nested Parent node.</b><i>Italics text at the end of a nested Parent node, after bold text.</i></code><b>Bold text in the top level Parent node.</b><i>Italics text after bold text in the top level Parent node.</i></p>'
        self.assertEqual(node_html, raw_html)

    def test_parent_no_tag(self):
        node = ParentNode(tag = "", children = 
            [
                LeafNode("b", "This bold should fail"),
                LeafNode("i", "As should this italics")
            ]
        )
        with self.assertRaises(ValueError) as cm:
            node.to_html()

        self.assertEqual(str(cm.exception), "Tag is required for a parent node")

    def test_parent_no_children(self):
        node = ParentNode("b", [])

        with self.assertRaises(ValueError) as cm:
            node.to_html()

        self.assertEqual(str(cm.exception), "Parent node must have children")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()