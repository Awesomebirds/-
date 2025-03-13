class Item:
    def __init__(self, value, prev: 'Item' = None):
        self._value = value
        self._prev = prev
    
    def get_value(self):
        return self._value
    
    def get_prev(self):
        return self._prev
    
    def add_prev(self, item):
        self._prev = item
    

class Stack:
    def __init__(self):
        self._top: Item = None

    def is_empty(self):
        if self._top == None:
            return True
        else:
            return False
    
    def push(self, item):
        new_item = Item(item)
        new_item.add_prev(self._top)
        self._top = new_item

    def pop(self):
        if self.is_empty():
            print("Nothing in Stack.")
        else: 
            print(self._top.get_value())
            self._top = self._top.get_prev()
    
    def peek(self):
        if self.is_empty():
            print("The Stack is empty.")
        else:
            print(self._top.get_value())

my_stack = Stack()
my_stack.push("hello, world!")
my_stack.push("hello, world!2")
my_stack.push("hello, world!3")

my_stack.peek()
my_stack.pop()
my_stack.peek()
my_stack.pop()
my_stack.peek()
my_stack.pop()
my_stack.pop()
my_stack.peek()
my_stack.pop()