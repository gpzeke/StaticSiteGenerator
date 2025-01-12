from textnode import TextType, TextNode
import re

def text_to_textnodes(text):
    text_nodes = [TextNode(text, TextType.TEXT),]
    
    text_nodes = split_nodes_delimiter(text_nodes, "**", TextType.BOLD)
    text_nodes = split_nodes_delimiter(text_nodes, "*", TextType.ITALIC)
    text_nodes = split_nodes_delimiter(text_nodes, "`", TextType.CODE)
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)
    
    return text_nodes

# For the time being this will not support nested markdown
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    text_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            text_nodes.append(node)
            continue

        split_text = node.text.split(delimiter)

        if len(split_text) % 2 == 0:
            raise ValueError("Missing delimiter.")
        
        split_node = []

        for i in range(len(split_text)):
            if split_text[i] == '':
                continue

            if i % 2 == 0:
                split_node.append(TextNode(split_text[i], TextType.TEXT))
            else:
                split_node.append(TextNode(split_text[i], text_type))

        text_nodes.extend(split_node)

    return text_nodes

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def split_nodes_image(old_nodes):
    text_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            text_nodes.append(node)
            continue

        remaining_text = node.text
        while True:
            matches = extract_markdown_images(remaining_text)
            if not matches:
                if remaining_text:
                    text_nodes.append(TextNode(remaining_text, TextType.TEXT))
                break
            
            alt_text, link_url = matches[0]
            parts = remaining_text.split(f'![{alt_text}]({link_url})', 1)
            
            if parts[0]:
                text_nodes.append(TextNode(parts[0], TextType.TEXT))
            
            if alt_text and link_url:
                text_nodes.append(TextNode(alt_text, TextType.IMAGE, link_url))
                
            remaining_text = parts[1]

    return text_nodes

def split_nodes_link(old_nodes):
    text_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            text_nodes.append(node)
            continue

        remaining_text = node.text
        while True:
            matches = extract_markdown_links(remaining_text)
            if not matches:
                if remaining_text:
                    text_nodes.append(TextNode(remaining_text, TextType.TEXT))
                break
            
            link_text, link_url = matches[0]
            parts = remaining_text.split(f'[{link_text}]({link_url})', 1)
            
            if parts[0]:
                text_nodes.append(TextNode(parts[0], TextType.TEXT))
            
            if link_text and link_url:
                text_nodes.append(TextNode(link_text, TextType.LINK, link_url))

            remaining_text = parts[1]

    return text_nodes