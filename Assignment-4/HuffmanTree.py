# COURSE CPSC 231 FALL 2021
# INSTRUCTOR: Jonathan Hudson
# Tutorial: T01, Wei
# Name: Jose Perales Rivera
# ID: 30143354
# Date: 12/10/2021
# Description: A class that is part of a text compression program that works by using huffman trees

class HuffmanTree:
    """
    A class to represent an Huffman Tree
    Attributes
    ----------
    char : str
        The characters represented by this tree
    count : int
        The count of how many times char occurred in the text
    left : HuffmanTree/None
        The left HuffmanTree below this one
    right : HuffmanTree/None
        The right HuffmanTree below this one
    bit : bool
        The bit symbol used to reach this HuffmanTree (either True/False for 1/0)


    General Structure
                         HuffmanTree (char,count,bit)
                          /    \
                      left    right
                        /        \
                HuffmanTree      HuffmanTree

    Default Structure
                         HuffmanTree (char,count,None)
                          /    \
                      left    right
                        /        \
                     None         None
    """

    # PART1 (constructor)
    def __init__(self, char, count, left=None, right=None, bit=None):
        # constructor function, gets the input from the user to construct huffman trees
        # only requires two arguments to be entered
        self.char = char
        self.count = count
        self.left = left
        self.right = right
        self.bit = bit

    # PART2 (order)
    def __lt__(self, other):
        if self.count > other.count:  # in case the count of self is greater than that of other
            return True
        elif self.count < other.count:  # in case the count of other is greater than that of self
            return False
        else:  # in case both counts are the same
            if self.char > other.char:  # if the character of self is greater than other's character
                return True
            else:  # if the character of other is greater than self's character
                return False

    # PART3 (string)
    def __str__(self):
        # returns a string with all the instance variables stored in a huffman tree
        return f"({self.char}, {str(self.count)}, {self.left}, {self.right}, {self.bit})"

    # PART3 (representation)
    def __repr__(self):
        # returns a descriptive string containing all the instance variables in a huffman tree
        return "HuffmanTree(" + repr(self.char) + ", " + repr(self.count) + ", " + repr(self.left) + ", " + repr(self.right) + ", " + repr(self.bit) + ")"

    # PART5 (equality)
    def __eq__(self, other):

        if other is None:  # in case self is being compared to something that does not exist
            return False

        # equality will only return true is the character, left and right of two huffman trees are the same
        if (self.char == other.char) and (self.left == other.left) and (self.right == other.right):
            return True
        else:  # if all 3 are not the same it will return false
            return False


# PART1 (make_trees)
def make_trees(dictionary):
    treesList = []

    for char in dictionary:  # going through each item in the dictionary passed in as an argument
        count = dictionary[char]  # sets up the values of each key as the count variable

        tree = HuffmanTree(char, count)  # creating a huffman tree for each character in the dictionary with its count
        treesList.append(tree)  # appending the huffman tree to the empty list

    return treesList  # returns the list once it has all the trees in it


# PART4 (merge)
def merge(t1, t2):

    char = t1.char + t2.char  # adding the characters of each tree to make the character of the new tree
    count = t1.count + t2.count  # adding the count of each tree to make the count of the new tree

    if t1 < t2:  # in case the first tree is less than the second tree according to the __lt__ function
        A = t2  # set A == the first tree
        B = t1  # set B == the second tree
        t1.bit = 1
        t2.bit = 0
    else:  # in case the first tree is greater than the second tree according to the __lt__ function
        A = t1  # set A == the second tree
        B = t2  # set B == the first tree
        t1.bit = 0
        t2.bit = 1

    return HuffmanTree(char, count, A, B, None)  # return the merged huffman tree
