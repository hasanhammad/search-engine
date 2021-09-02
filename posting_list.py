# The Node class acts as a node for each word,
# by storing the pageId of the word.

class Node:
    def __init__(self, pageId=None):
        self.pageId = pageId
        self.nextval = None


class SlinkedList:
    def __init__(self, head=None):
        self.head = head

    # to print the posting list
    def __str__(self):

        # defining a blank res variable
        res = " "
        # initializing ptr to head
        ptr = self.head
        ptr = ptr.nextval
        # traversing and adding it to res
        while ptr:
            res += str(ptr.pageId) + ", "
            ptr = ptr.nextval

        # removing trailing commas
        res = res.strip(", ")

        # chen checking if
        # anything is present in res or not
        if len(res):
            return "[" + res + "]"
        else:
            return "[]"
