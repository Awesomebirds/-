class Node:
    def __init__(self, value: int):
        self._value: int | None = value
        self._left: Node | None = None
        self._right: Node | None = None
        self._parent: Node | None = None
    
    def get_value(self):
        return self._value
    
    def get_left(self):
        return self._left
    
    def get_right(self):
        return self._right
    
    def get_parent(self):
        return self._parent
    
    def _add_parent(self, parent: 'Node'):
        self._parent = parent
    
    def add_left(self, value):
        child = Node(value)
        child._add_parent(self)
        self._left = child

    def add_right(self, value):
        child = Node(value)
        child._add_parent = self
        self._right = child

    
class Tree:
    def __init__(self):
        self._root: Node | None = None
    
    def is_empty(self):
        if self._root == None: return True
        else: return False

    def get_root_value(self):
        return self._root.get_value()
    
    def add_node(self, value: int, _node: Node = None):
        if value != int: #숫자 아니면 종료
            raise TypeError("The value is not a int")
        elif not self.is_empty() & value == self.get_root_value():
            raise ValueError("The value is already exist: duplicates are not allowed")
        
        new_node = Node(value)
        
        if self.is_empty(): self._root = new_node #트리가 비어있다면, 루트로 생성
        
### 1. (루트)노드와 밸류넣기. 2. 노드 보기 3. 넣을 값과 노드 값 비교. 4. 값이 작으면 왼쪽 노드를 봄. 크면 오른쪽 노드를 봄. 5. 노드가 비었다면 넣고 끝. 5.1. 노드가 비어있지 않다면 해당 노드를 1번에 넣음.