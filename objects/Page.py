from objects.Block import append_block


class Page:
    def __init__(self, json_page):
        results = json_page["results"]
        blocks = []
        for block in results:
            append_block(blocks, block)
        self.blocks = blocks
