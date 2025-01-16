from textnode import TextNode, TextType
from htmlnode import *
from inline_markdown import *
from block_markdown import *

def main():
    text = """1. test 1
2. test 2
3. test 3
4. test 4"""
    result = block_to_block_type(text)
    print(result)

if __name__ == "__main__":
    main()