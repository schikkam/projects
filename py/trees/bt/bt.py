class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def insert(root, data):
    if root == None:
        return Node(data)
    if  data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    #we dont insert duplicates
    return root

def inorder(root):
    if root != None:
        inorder(root.left)
        print(root.data, end='')
        inorder(root.right)

def preorder(root):
    if root != None:
        print(root.data, end='')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root != None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end='')

def dfs(root):
    inorder(root)  # this uses implicit stack

def bfs(root):
    q = [root]
    while len(q) != 0:
        current = q.pop(0)
        print( current.data)
        if current.left != None:
            q.append(current.left)
        if current.right != None:
            q.append(current.right)

def bfs_spiral_order(root):
    """
        +------------< 11 <------------< START
        +-----> 6               19 >------------------+
    +------<4       8       17        43   <----------+
    +--->3     5   7  10   16   18   31   49 ->END

    """
    pq = [root]
    cq = []
    print(root.data)
    flag=-1
    while len(pq) != 0:
        current = pq.pop(0)
        if current.left != None:
            cq.append(current.left)
        if current.right != None:
            cq.append(current.right)
        if len(pq) == 0:
            flag *= -1  # flip the direction
            pq = cq[:]  # copy to parent queue
            cq = []
            toprint = [str(x.data) for x in pq]

            if flag==1:
                print("".join(toprint))
            else:
                print("".join(reversed(toprint)))

def count_leaves(root):
    if root:
        if root.left == None and root.right == None:
            return 1
        return count_leaves(root.left) + count_leaves(root.right)
    return 0

def count_internal_nodes(root):
    if root:
        if root.left == None and root.right == None:
            return 0
        return count_internal_nodes(root.left) + count_internal_nodes(root.right) + 1
    return 0

def count_nodes(root):
    if root:
        return count_nodes(root.left)+count_nodes(root.right)+1
    return 0

def find_nth_smallest(root, n):
    if root:
        l = find_nth_smallest(root.left, n)
        lc = count_nodes(root.left)
        if lc + 1 == n: return root

        rc = count_nodes(root.right)
        c = n
        if lc + rc + 1 >= n:
            c = n - (lc+1)
        r = find_nth_smallest(root.right, c)

        if l: return l
        return r

def find_nth_biggest(root, n):
    if root:
        r = find_nth_biggest(root.right, n)
        rc = count_nodes(root.right)
        if rc + 1 == n: return root

        lc = count_nodes(root.left)
        c = n
        if rc + lc + 1 >= n:
            c = n - (rc+1)
        l = find_nth_biggest(root.left, c)

        if r: return r
        return l

def height(root):
    if root:
        return max(
            height(root.left), \
            height(root.right)
        ) + 1
    return 0

def width(root): # same as bfs spiral order
    pq = [root]
    cq = []
    wid = 1
    while len(pq) != 0:
        current = pq.pop(0)
        if current.left != None:
            cq.append(current.left)
        if current.right != None:
            cq.append(current.right)
        if len(pq) == 0:
            pq = cq[:]  # copy to parent queue
            cq = []
            if wid < len(pq):
                wid = len(pq)
    return wid

def test():
    root = None
    data = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    for d in data:
        root = insert(root, d)

    print(count_internal_nodes(root))

    #bfs_spiral_order(root)
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    print(count_leaves(root))

def test_one():
    """
            4
    2               6
    1       3       5        7
    """


    root = None
    root = insert(root, 4)
    root = insert(root, 2)
    root = insert(root, 6)
    root = insert(root, 1)
    root = insert(root, 3)
    root = insert(root, 5)
    root = insert(root, 7)

    print(count_internal_nodes(root))


def test_two():
    root = None
    data = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    for d in data:
        root = insert(root, d)
    print(count_nodes(root))

def test_three():
    root = None
    wdata = [11, 6, 19, 4, 8, 17, 43, 3, 5, 7, 10, 16, 18, 31, 49]
    data = [4, 2, 6, 1, 3, 5, 7]
    for d in data:
        root = insert(root, d)

    data.sort()
    for i, n in enumerate(data):
        print("{} ".format(find_nth_smallest(root, i+1).data), end='')

    print("\n")

    i = len(data)
    while i > 0:
        print("{} ".format(find_nth_biggest(root, i).data), end='')
        i -= 1
    print("\n")
    print (height(root))

    print("\n")
    print(width(root))


test_three()