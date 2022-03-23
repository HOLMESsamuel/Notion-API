class Block:
    def __init__(self, block):
        self.id = block["id"]
        self.has_children = block["has_children"]
        self.type = block["type"]
