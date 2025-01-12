from textnode import TextNode, TextType
from htmlnode import *
from inline_markdown import *

def main():
    node = [TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev). Pretty neat, right?",
    TextType.TEXT,
    )]
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    match = extract_markdown_links(text)

    #img_alt, img_url = match[0]
    #print(match[0])

    #print(f'{img_alt} | {img_url}')

    print(split_nodes_link(node))

if __name__ == "__main__":
    main()