"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
       n = Element(new_element)
       if self.head:
           self.head.next = n
           self.head = n
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if self.head is None:
            return None
        n = self.head
        while n is not None:
            if n.value == position:
                return position.value
            n = n.next
        return None
       
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        if position is None :
            return None
        newn = Element(new_element)
        newn.next = position.next
        position.next = newn
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        h = self.head
        if(h is not None):
            if(h.value == value):
                self.head = h.next
                h = None
