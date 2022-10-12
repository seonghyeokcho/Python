#### Binary Search Tree(이진 탐색 트리) ####

## Time Complexity ##
# find(t): O(logn)
# insert(t): O(logn)
# delete(t): O(logn)

#트리를 구성하는 노드 클래스
class Node:
    """노드 생성자"""
    def __init__(self, key, value):
        self.key = key  # 키
        self.value = value # 값: 서브트리의 크기, 자신의 높이 혹은 높이의 차(왼쪽 서브트리의 높이 - 오른쪽 서브트리의 높이)
        self.pointers()
    def pointers(self):
        self.left = None # 왼쪽 자식 참조
        self.right = None # 오른쪽 자식 참조
        self.parent = None  # 부모 참조

# binary search tree(이진 탐색 트리) - 직접 구현해본 이진 탐색 트리
class BinarySearchTree():
    def __init__(self):
        self.root = None  # 루트 설정
    
    # 노드 검색
    def search(self, t):  # -> int or None or str
        '''
        루트에서 시작하여 찾고자 하는 키의 대소 관계를 판단한 결과에 따라
        노드 x에 대해 key(x) > t이면 왼쪽 or key(x) < t이면 오른쪽 서브트리를
        따라가면서 수행한다.
        '''
        node = self.root
        while node is not None:  # 더이상 진행할 수 없을때까지 반복
            if t == node.key:  # 검색 성공
                return node
            else:
                node.parent = node
                if t < node.key:
                    node = node.left  # 왼쪽으로 진행
                else:
                    node = node.right  # 오른쪽으로 진행
        return None
                
    # 노드 삽입(추가)
    #### TODO: 배열 전체를 입력으로 받아 처리하기, 임의의 값 k를 설정하고 해당 현재 노드의 key보다 k만큼 작거나 큰 값만 삽입하기
    def insert(self, t, value):  # -> bool
        '''
        노드 삽입시 트리의 형태가 이진 탐색 트리의 조건을 유지해야 한다는
        전제 조건이 있다. 따라서 노드 삽입 시에는 먼저 탐색을 통해
        삽입할 위치를 찾아낸 뒤에 수행한다.
        알고리즘은 다음과 같다.
            1. root가 있는지 파악한다.
                - root가 없으면 생성(삽입)
                - root가 있으면 root부터 삽입할 위치 검색 시작
            2. (root가 이미 존재한다는 전제) root -> 현재 노드 x로 지정하고,
            삽입하려는 값 k와 현재 노드의 key를 비교한다.
                - t < key(x)일 때, left(x) is None -> 그 자리에 삽입
                left(x) is not None -> current(x) = left(x)
                - t > key(x)일 때, right(x) is None -> 그 자리에 삽입
                right(x) is not None -> current(x) = right(x)
            3. 2번 과정을 더이상 진행할 수 없을때까지 반복한다.
        '''
        new = Node(t, value)
        if self.root is None:
            self.root = new
        else:
            node = self.root
            while True:
                # if key == node.key:  # 중복 불허
                #     return False
                if t < node.key:
                    # 왼쪽으로
                    if node.left is None:
                        node.left = new
                        new.parent = node
                        break
                    node = node.left
                else:
                    # 오른쪽으로
                    if node.right is None:
                        node.right = new
                        new.parent = node
                        break
                    node = node.right
        return True
            
    # 노드 삭제
    def delete(self, t):  # -> bool
        '''
        삭제 또한 삽입과 마찬가지로 
        알고리즘은 다음과 같다.
            1. root -> 현재 노드 x로 지정
            2. 삭제하려는 key = t와 각 노드의 키 = key(x)를 비교한다.
                - t == key(x) -> 삭제할 key를 찾았으므로 비교 종료
                - t < key(x) -> x = left(x)
                - t > key(x) -> x = right(x)
            3. 2번에서 삭제할 키를 찾았다면 케이스를 다음과 같이 나눈다.
                3-1. 단말(leaf) 노드를 삭제하는 경우
                3-2. 1개의 자식만을 가진 노드를 삭제하는 경우
                3-3. 2개 자식을 모두 가진 노드를 삭제하는 경우
            4. 3번에 따라서 각각 다른 방법으로 진행한다.
        3번에서 언급한 각각의 케이스에 대해 살펴보면,
            3-1 -> 단말(leaf) 노드를 삭제하는 경우
                if x == left(parent(x)):
                    left(parent) = None
                else:
                    right(parent) = None
                이 경우는 따로 로직을 짤 필요 없이 아래 두 번째 경우에서 자연스럽게 걸러진다.
            3-2 -> 1개의 자식만을 가진 노드를 삭제하는 경우
                delete(x) & x = child(x), 그렇게 하면 child(x)를 루트로 하는
                서브트리의 모든 노드 y에 대해 x == right(parent(x))이면
                key(y) > key(parent(x))를, x == left(parent(x))이면
                key(y) < key(parent(x))를 만족한다.
                    - x == left(parent(x)) -> left(parent(x)) = child(x)
                    - x == right(parent(x)) -> right(parent(x)) = child(x)
            3-3 -> 2개 자식을 모두 가진 노드를 삭제하는 경우
                왼쪽 서브트리에서 가장 큰 노드로 대체 or 오른쪽 서브트리에서 가장 작은
                노드로 대체한다.(여기서는 왼쪽 서브트리에서 찾는다.)
                이후, 부모 노드의 왼쪽 참조를, 대체한 노드로 지정한다.
                그리고 대체한 노드는 원래 위치에서 3-1, 3-2의 경우 중 한가지에 해당될 수
                있기 때문에 그에 따라 또한 적용시켜 처리한다.
        '''
        node = self.root
        is_left_child = True
        
        # 삭제할 노드 탐색
        while node is not None:
            if t == node.key:
                break
            else:
                node.parent = node
                if t < node.key:
                    node = node.left
                    is_left_child = True
                else:
                    node = node.right
                    is_left_child = False
        else:
            return False
        
        # case 1 or 2
        if node.left is None:
            if node is self.root:
                self.root = node.right
            elif is_left_child:
                node.parent.left = node.right
            else:
                node.parent.right = node.right
        elif node.right is None:
            if node is self.root:
                self.root = node.left
            elif is_left_child:
                node.parent.left = node.left
            else:
                node.parent.right = node.left
        else:  # case 3
            node.parent = node
            node_left_max = node.left
            is_left_child = True
            
            while node_left_max.right is not None:
                node.parent = node_left_max
                node_left_max = node_left_max.right
                is_left_child = False
            
            # 삭제할 노드를 대체 노드로 변경(= 삭제)
            node.key = node_left_max.key
            node.value = node_left_max.value
            
            if is_left_child:  # 이 경우가 성립된다면 삭제할 노드의 왼쪽 자식은 오른쪽 자식이 없다.
                node.parent.left = node_left_max.left
            else:
                node.parent.right = node_left_max.left
        return True
    
    #### 출력부 ####
    # ---------------------------------------------------
    # 전위 순회: 루트 -> 왼쪽 서브트리 -> 오른쪽 서브트리
    def pre_order_traversal(self):
        def subtree_iter(node):
            if node is not None:
                yield node.key
                yield from subtree_iter(node.left)
                yield from subtree_iter(node.right)
            
        if self.root is None:
            print("<empty tree>")
        else:
            return list(subtree_iter(self.root))
    
    # 정위(중위) 순회: 왼쪽 서브트리 -> 루트 -> 오른쪽 서브트리
    def in_order_traversal(self):
        def subtree_iter(node):
            if node is not None:
                yield from subtree_iter(node.left)
                yield node.key
                yield from subtree_iter(node.right)
            
        if self.root is None:
            print("<empty tree>")
        else:
            return list(subtree_iter(self.root))
    
    # 후위 순회: 왼쪽 서브트리 -> 오른쪽 서브트리 -> 루트
    def post_order_traversal(self):
        def subtree_iter(node):
            if node is not None:
                yield from subtree_iter(node.left)
                yield from subtree_iter(node.right)
                yield node.key
            
        if self.root is None:
            print("<empty tree>")
        else:
            return list(subtree_iter(self.root))
    
    # 레벨 순회: 루트부터 깊이 순 & 왼쪽 서브트리 -> 오른쪽 서브트리
    def level_order_traversal(self):
        if self.root is None:
            print("<empty tree>")
        else:
            temp = []
            queue = [self.root]
            while queue:
                root = queue[0]
                queue = queue[1:]
                if root is not None:
                    temp.append(root.key)
                    if root.left:
                        queue.append(root.left)
                    if root.right:
                        queue.append(root.right)
            return temp
    # ---------------------------------------------------

# test
if __name__ == "__main__":
    array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]
    bst = BinarySearchTree()
    for i, k in enumerate(array):
        bst.insert(k, i)
    print(bst.in_order_traversal())
    # bst.pre_order_traversal()
    # bst.post_order_traversal()
    # bst.level_order_traversal()
    print(bst.delete(49))  # 5번만에 찾음. 정렬된 리스트에서 찾았다면 10번의 step이 필요했을 것
    print(bst.in_order_traversal())