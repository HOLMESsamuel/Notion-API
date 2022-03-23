# Define all methods to print objects

def print_blocks(blocks):
    for block in blocks:
        print_block(block)


def print_block(block):
    print(block.id)
    print(block.has_children)
    print(block.type)

    print("\n")
