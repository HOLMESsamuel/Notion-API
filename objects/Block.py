import constants


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


def append_block(blocks, block):
    block_type = block["type"]
    if block_type == constants.PARAGRAPH:
        block = Paragraph(block)
    elif block_type == constants.HEADING_2:
        block = Heading2(block)
    else:
        block = Block(block)
    return blocks.append(block)


class Paragraph(Block):
    def __init__(self, block):
        super().__init__(block)
        super().set_content(block)


class Heading2(Block):
    def __init__(self, block):
        super().__init__(block)
        super().set_content(block)
