#Basic Linked List structure in Python3

#Linked List Node Class - Has a value and pointer to next node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = next

#Linked List Class - holds all nodes and keeps track of first(head) and last(tail)
#nodes in the list. Also contains functions to add/remove nodes and to dislay the list
#List is empty when created, thus no "head" or "tail" nodes at this point
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    #Creates a node; if its the first, then set head to it. If a tail exists, update next pointer
    #to the new node. This keeps the nodes linked
    #Assign the new node to the tail node.
    def AddNode(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        
        if self.tail != None:
            self.tail.next = new_node
        
        self.tail = new_node

    #Iterate through the list to find the node to remove. 
    #Create pointers to keep track of the previous and current node
    #Once the node to remove is reached, the previous node "next" pointer is changed to 
    #skip the the current node and point to the current "next" instead.
    #If the Head node is removed, update the Head to be the "next" node.
    def RemoveNode(self, index):
        prev = None
        node = self.head
        i = 0

        while node != None and i < index:
            prev = node
            prev = node.next
            i += 1

        if prev == None:
            self.head = node.next
        else:
            prev.next = node.next
    
    #Start at the head pointer and traverse the list through each node's "next" pointer,
    #displaying its data member, until the node is no longer null.
    def PrintList(self):
        node = self.head

        while node:
            print (node.data)
            node = node.next
                
                
            

#Testing the code out
MyList = LinkedList()

MyList.AddNode(1)
MyList.AddNode(2)
MyList.AddNode(3)
MyList.AddNode(4)
MyList.PrintList()

MyList.RemoveNode(3)
MyList.PrintList()
