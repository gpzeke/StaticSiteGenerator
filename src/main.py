from textnode import TextNode, TextType
from htmlnode import *
from inline_markdown import *
from block_markdown import *

def main():
    text = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
    blocks = markdown_to_blocks(text)
    for item in blocks:
        print(f"{item}\n")

    print(f'{type(blocks)} of length: {len(blocks)}')

if __name__ == "__main__":
    main()