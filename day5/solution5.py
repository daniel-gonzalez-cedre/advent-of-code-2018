from __future__ import print_function

class Node():
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

def reacts(x, y):
    return (abs(ord(x) - ord(y)) - 32) == 0

def equiv(x, y):
    return reacts(x, y) or x == y

def part_one(string, remove=' '):
    #CREATE A DOUBLY-LINKED LIST OF THE INPUT DATA
    head = Node()
    curr = head
    for char in string:
        if not equiv(char, remove):
            curr.next = Node(char)
            curr.next.prev = curr
            curr = curr.next
    #ANNEAL THE LIST
    curr = head.next
    while curr != None:
        if curr.data == None:
            curr = curr.next
        if curr.next == None:
            break
        elif reacts(curr.data, curr.next.data):
            curr = curr.prev
            curr.next = curr.next.next.next
            if curr.next != None:
                curr.next.prev = curr
        else:
            curr = curr.next
    #COMPUTE LENGTH
    length = 0
    curr = head.next
    while curr != None:
        length += 1
        curr = curr.next
    return length

def part_two(string):
    return min([part_one(string, remove=chr(x)) for x in range(65, 91)])

#READ THE INPUT
with open('./input.txt') as f_input:
    for line in f_input:
        string = line.strip()

#SOLUTION TO PART 1
print(part_one(string))

#SOLUTION TO PART 2
print(part_two(string))
