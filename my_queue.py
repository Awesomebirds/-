class Item:
    def __init__(self, value):
        self._value = value
        self._next = None
    
    def get_value(self):
        return self._value
    
    def add_next(self, next: 'Item'):
        self._next = next
    
    def get_next(self):
        return self._next

class Queue:
    def __init__(self):
        self._front: Item = None
        self._rear: Item = None
    
    def is_empty(self):
        return self._fornt is None
    
    def enqueue(self, value): #Rear의 next에 value 추가 -> rear = value
        new_item = Item(value)
        if self.is_empty():
            self._rear = new_item
            self._front = self._rear
        else:
            self._rear.add_next(new_item)
            self._rear = new_item

    def dequeue(self): #Front 반환하고 삭제 -> front = value
        if self.is_empty(): print("The queue is empty!")
        else:
            print(self._front.get_value())
            self._front = self._front.get_next()
    
    def peek(self): #Front 반환
        print(self._front.get_value())
    
    def petrol(self):
        checking = self._front
        while checking != None:
            print(checking.get_value())
            checking = checking.get_next()

my_queue = Queue()

my_queue.enqueue("hello,")
my_queue.enqueue(" ")
my_queue.enqueue("world")
my_queue.enqueue("!")

my_queue.petrol()

