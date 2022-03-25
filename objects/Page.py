from objects.Block import append_blocks


class Page:
    def __init__(self, json_page):
        results = json_page["results"]
        blocks = []
        append_blocks(blocks, results)
        self.blocks = blocks
