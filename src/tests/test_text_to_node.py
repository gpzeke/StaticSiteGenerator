import unittest

from inline_markdown import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_simple_text_split(self):
        old_nodes = [TextNode("This is text with a `code block` word", TextType.TEXT),]
        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        expected_result = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_result)

    def test_multiple_text_split(self):
        old_nodes = [
            TextNode("The first example of **bold** words", TextType.TEXT),
            TextNode("**Bold** example number two", TextType.TEXT),
            TextNode("This does not have any bold text",TextType.TEXT),
            TextNode("Last bold example to test in this list of **nodes**", TextType.TEXT),
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        expected_result = [
            TextNode("The first example of ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" words", TextType.TEXT),
            TextNode("Bold", TextType.BOLD),
            TextNode(" example number two", TextType.TEXT),
            TextNode("This does not have any bold text", TextType.TEXT),
            TextNode("Last bold example to test in this list of ", TextType.TEXT),
            TextNode("nodes", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, expected_result)

    def test_mutiple_non_text(self):
        old_nodes = [
            TextNode("Bold text", TextType.BOLD),
            TextNode("Text that contains **bold** text", TextType.TEXT),
            TextNode("Italics text", TextType.ITALIC),
            TextNode("Text that contains code block", TextType.CODE),
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        expected_result = [
            TextNode("Bold text", TextType.BOLD),
            TextNode("Text that contains ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT),
            TextNode("Italics text", TextType.ITALIC),
            TextNode("Text that contains code block", TextType.CODE),
        ]
        self.assertEqual(new_nodes, expected_result)

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and *italic*", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )
