from textnode import TextType, TextNode
import re
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
    matches = re.findall(r"\!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
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
                break
            
            alt_text, link_url = matches[0]
            parts = remaining_text.split(f'![{alt_text}]({link_url})', 1)
            
            if parts[0] == '':
                pass
            else:
                text_nodes.append(TextNode(parts[0], TextType.TEXT))
            
            if alt_text == '' or link_url == '':
                pass
            else:
                text_nodes.append(TextNode(alt_text, TextType.IMAGE, link_url))
                
            remaining_text = parts[1]

    if remaining_text == '':
        pass
    else: 
        text_nodes.append(TextNode(remaining_text, TextType.TEXT))

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
                break
            
            link_text, link_url = matches[0]
            parts = remaining_text.split(f'[{link_text}]({link_url})', 1)
            
            if parts[0] == '':
                pass
            else:
                text_nodes.append(TextNode(parts[0], TextType.TEXT))
            
            if link_text == '' or link_url == '':
                pass
            else:
                text_nodes.append(TextNode(link_text, TextType.LINK, link_url))

            remaining_text = parts[1]

    if remaining_text == '':
        pass
    else: 
        text_nodes.append(TextNode(remaining_text, TextType.TEXT))

    return text_nodes