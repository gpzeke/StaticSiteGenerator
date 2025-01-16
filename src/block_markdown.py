import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")

    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    
    return filtered_blocks

def block_to_block_type(block):
    leading_character = block[0]
    
    # process headings
    if leading_character == '#':
        lead_number = len(block) - len(block.lstrip(leading_character))
        if lead_number <= 6:
            return block_type_heading
            #return f'<h{lead_number}>'
    
    # process code blocks
    if leading_character == '`':
        if block[:3] == '```':
            if block[-3:] == '```':
                return block_type_code
                #return '<code>'
    
    # process blockquotes
    if leading_character == '>':
        lines = block.splitlines()
        valid_quote = []
        for line in lines:
            valid_quote.append(line[0] == '>')

        result = all(valid_quote)
        if result:
            return block_type_quote
            #return '<blockquote>'
    
    # process unordered lists
    ul_characters = ['-', '*']
    if leading_character in ul_characters:
        lines = block.splitlines(ul_characters)
        valid_list_items = []
        for line in lines:
            valid_list_items.append(line[0] in ul_characters)
        
        result = all(valid_list_items)
        if result:
            return block_type_ulist
            #return '<ul>'
    
    # process ordered lists
    regex = r'\d+\.+ '
    
    if bool(re.match(regex, block)):
        lines = block.splitlines()
        valid_list_items = []
        for line in lines:
            valid_list_items.append(bool(re.match(regex, line)))
        
        result = all(valid_list_items)
        if result:
            return block_type_olist
            #return '<ol>'

    return block_type_paragraph
    #return '<p>'