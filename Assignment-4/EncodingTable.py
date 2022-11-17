# COURSE CPSC 231 FALL 2021
# INSTRUCTOR: Jonathan Hudson
# Tutorial: T01, Wei
# Name: Jose Perales Rivera
# ID: 30143354
# Date: 12/10/2021
# Description: A class that is part of a text compression program that works by using huffman trees

import sys


class EncodingTable:
    """
    A class to represent an Encoding Table made from a Huffman Tree
    Attributes
    ----------
    encode : str
        The dictionary storing for each symbol "char" as binary bit string code "code"
    """

    def __init__(self, tree):
        """
        Constructs an EncodingTable using a HuffmanTree
        :param tree: The HuffmanTree to use to build the EncodingTable dictionary encode
        """
        # Create empty dictionary
        self.encode = {}
        # Launch recursive function to store values into self.encode dictionary
        self.recurse(tree, "")

    # PART 7 (recurse)
    def recurse(self, tree, code):

        if tree.bit is not None:  # in case there is no bit yet
            if tree.bit == 1:
                code += "1"
            if tree.bit == 0:
                code += "0"

        if (tree.left is None) and (tree.right is None):  # in case there arent any trees to the left or right
            self.encode[tree.char] = code

        elif (tree.left is not None) and (tree.right is None):  # in case there is only a tree to the right
            self.recurse(tree.left, code)

        elif (tree.left is None) and (tree.right is not None):  # in case there is only a tree to the left
            self.recurse(tree.right, code)

        elif (tree.left is not None) and (tree.right is not None):  # in case there are trees to the left and right
            self.recurse(tree.left, code)
            self.recurse(tree.right, code)

    # PART 6 (string)
    def __str__(self):
        myList = []
        myString = ""

        for element in self.encode:
            myList.append(element)  # appends every item on self.encode to myList

        myList = sorted(myList)  # sorts myList

        for j in myList:
            myString += f"{repr(j)}:{self.encode[j]}\n"  # modifies the string according to the sorted items in myList

        return myString

    def encode_text(self, text):
        """
        Encodes the provided text using the internal encoding dictionary (turns each character symbol into a bit string)
        :param text: The string text to encode
        :return: A bit string "000100" based on the internal encode dictionary
        """
        output_text = ""
        # Loop through characters
        for char in text:
            # If one matches then encode into bitstring
            if char in self.encode:
                output_text += self.encode[char]
            else:
                sys.exit(f"Can't encode symbol {char} as it isn't in the encoding table:\n{self}")
        return output_text

