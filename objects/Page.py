from objects.Block import Block


class Page:
    def __init__(self, json_page):
        results = json_page["results"]
        blocks = []
        for block in results:
            blocks.append(Block(block))
        self.blocks = blocks
