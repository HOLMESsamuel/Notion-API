import json

import constants
from NotionAPIClient import NotionAPIClient


class Block:
    def __init__(self, block):
        self.content = ""
        self.id = block["id"]
        self.has_children = block["has_children"]
        self.type = block["type"]

    def set_content(self, block):
        try:
            # TODO : possibilité de rich text à plus que un élément
            self.content = block[self.type]["rich_text"][0]["plain_text"]
        except IndexError:  # in case there is not content rich_text is empty
            pass


def append_blocks(blocks, results):
    for block in results:
        append_block(blocks, block)
    return blocks


def append_block(blocks, block):
    client = NotionAPIClient()
    block_type = block["type"]
    if block_type == constants.PARAGRAPH:
        block = Paragraph(block)
    elif block_type == constants.HEADING_2:
        block = Heading2(block)
    elif block_type == constants.TOGGLE:
        block = Toggle(block)
    elif block_type == constants.BULLETED_LIST_ITEM:
        block = BulletedListItem(block)
    else:
        block = Block(block)

    if block.has_children:
        response = client.retrieve_block(block.id)
        if response is not None:
            page_json_data = json.loads(response)
            results = page_json_data["results"]
            blocks.append(block)
            return append_blocks(blocks, results)
    return blocks.append(block)


class Paragraph(Block):
    def __init__(self, block):
        super().__init__(block)
        super().set_content(block)


class Heading2(Block):
    def __init__(self, block):
        super().__init__(block)
        super().set_content(block)


class Toggle(Block):
    def __init__(self, block):
        super().__init__(block)
        super().set_content(block)


class BulletedListItem(Block):
    def __init__(self, block):
        super().__init__(block)
        super().set_content(block)
