from textnode import TextType, TextNode
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