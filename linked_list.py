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
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        pos = 1
        if self.head:
            while current.next != None:
                if pos == position:
                    return current
                else:
                    pos += 1
                    current = current.next
            if current.next == None:
                if pos == position:
                    return current
        else:
            return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        previous = self.head
        pos = 1
        if self.head:
            while current.next != None:
                if pos == position:
                    previous.next = new_element
                    new_element.next = current
                else:
                    pos += 1
                    previous = current
                    current = current.next
            if pos == position:
                previous.next = new_element
                new_element.next = current
        else:
            pass

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = self.head
        if self.head:
            while current.next != None:
                # first element matching the value
                # print(current.value, previous.value, value)
                if current.value == value and current.value == previous.value:
                    print('entering first condition')
                    current = current.next
                    print(current.value)
                    current.next = self.head
                    print('head', self.head.value)
                    print('after changing head', current.value, previous.value)
                    break
                # if the value is one of the middle elements
                elif current.value == value and current.value != previous:
                    print('entering second condition')
                    previous.next = current.next
                    current.next = None
                    current = previous
                    break
                else:
                    previous = current
                    current = current.next
            # if the value is the last element in the linked list
            if current.next == None:
                print('entering final if')
                if current.value == value:
                    print('value found')
                    current.value = previous.value
                    previous.next = None
                else:
                    print('else')
        else:
            pass


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4, 3)
# Should print 4 now
print(ll.get_position(3).value)
#
# Test delete
ll.delete(3)
# Should print 2 now
print('position 1')
print(ll.get_position(1).value)
# Should print 4 now
print('position 2')
print(ll.get_position(2).value)
# Should print 3 now
print('position 3')
print(ll.get_position(3).value)
# Should print 4 now
print('position 4')
print(ll.get_position(4).value)
