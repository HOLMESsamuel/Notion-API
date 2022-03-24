# Define all methods to print objects
import constants


def print_blocks(blocks):
    for block in blocks:
        print_block(block)


def print_block(block):
    print(block.id)
    print(block.has_children)
    print(block.type)
    if block.type in constants.BLOCK_TYPES:
        print(block.content)

    print("\n")
