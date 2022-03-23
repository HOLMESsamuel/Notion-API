class Block:
    def __init__(self, block):
        self.id = block["id"]
        self.has_children = block["has_children"]
        self.type = block["type"]


def append_block(blocks, block):
    if block["type"] == "paragraph":
        block = Paragraph(block)
    else:
        block = Block(block)
    return blocks.append(block)


class Paragraph(Block):
    def __init__(self, block):
        super().__init__(block)
        try:
            # TODO : possibilité de rich text à plus que un élément
            self.content = block["paragraph"]["rich_text"][0]["plain_text"]
        except IndexError:
            self.content = ""
