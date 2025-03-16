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
        child._add_parent(self)
        self._right = child

    
class Tree:
    """Represents a binary search tree."""
    def __init__(self):
        """Initialize an empty tree"""
        self._root: Node | None = None
    
    def is_empty(self) -> bool:
        """Checks if the tree is empty"""
        return self._root is None

    def get_root_value(self) -> int:
        """
        Returns the value of the root node

        Raise:
            ValueError: if the tree is empty
        """
        if self._root is None: raise ValueError("The Tree is empty.")
        return self._root.get_value()
    
    def add_node(self, value: int, _node: Node = None):
        """
        Adds a node into the tree.

        Args:
            value: The value to add.
            _node: (Internal) The currunt node in the recursion
        
        Raises:
            TypeError: If the given value is not an int.
            ValueError: If the given value already exists.
        """
        if not isinstance(value, int): #숫자 아니면 종료
            raise TypeError("The value is not a int")

        if self.is_empty():
            self._root = Node(value) #트리가 비어있다면, 루트로 생성
            return
        
        if _node is None: _node = self._root #최초 실행(재귀 전)시 인수노드에 루트노드를 넣어줌

        if value < _node.get_value(): #넣을 값이 비교하는 노드보다 작으면 왼쪽으로
            if _node.get_left() is None:
                _node.add_left(value) #왼쪽이 비어있으면 왼쪽에 노드 추가
            else:
                self.add_node(value, _node.get_left()) 
        elif value > _node.get_value():
            if _node.get_right() is None:
                _node.add_right(value)
            else:
                self.add_node(value, _node.get_right())
        else:
            raise ValueError("The value is already exist: duplicates are not allowed")
    
    def search(self, value: int, _node: Node = None) -> bool:
        """
        이진탐색트리로 해당 값 찾는 함수
        루트부터 비교하여 찾는 값이 작으면 왼쪽, 크면 오른쪽 노드를 살펴봄.

        Args:
            value: The value to search for.
            _node: (Internal) Current node in the recursion.

        Return: True if the value exists in the tree, False otherwise.

        Raises:
            TypeError: If the value is not an Integer
        """

        if not isinstance(value, int):
            raise TypeError("The value is not an Integer")
        
        if self.is_empty():
            return False
        
        if _node is None:    #재귀 전(메소드최초실행) 루트노드 넣어주기
            _node = self._root

        if value < _node.get_value():
            if _node.get_left():
                return self.search(value, _node.get_left())
            else: return False
        elif value > _node.get_value():
            if _node.get_right():
                return self.search(value, _node.get_right())
            else: return False
        else:   #value == _node.get_value()
            return True
    
    def _inorder_traversal(self, node: Node):
        """Performs a in-order traversal of the tree.

        Args:
            node: The node to start traversal from.

        Returns:
            A list of values visited in in-order.
        """

        ordered = []

        if node.get_left():
            ordered.extend(self._inorder_traversal(node.get_left()))

        ordered.append(node.get_value())

        if node.get_right():
            ordered.extend(self._inorder_traversal(node.get_right()))

        return ordered

    def inorder(self):
        if self.is_empty():
            return []
        else:
            return self._inorder_traversal(self._root)

tree = Tree()
tree.add_node(5)
tree.add_node(3)
tree.add_node(35)
tree.add_node(62)
tree.add_node(644)
tree.add_node(1)
tree.add_node(2)
tree.add_node(7)

print(tree.inorder())