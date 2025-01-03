class tree_node(object):
    def __init__(self, data=-1, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
class tree(object):
    def __init__(self):
        self.root = tree_node()
        self.Queuen = []
    def insert(self, data):
        new_node = tree_node(data)
        if self.root.data == -1:
            self.root = new_node
            self.Queuen.append(new_node)
        else:
            treenode=self.Queuen[0]
            if treenode.left==None:
                treenode.left=new_node
                self.Queuen.append(new_node)
            else:
                treenode.right=new_node
                self.Queuen.append(new_node)
                self.Queuen.pop(0)

    def preorder(self, root):
        if root == None:
            return
        print(root.data, end=" ")
        self.inorder(root.left)
        self.inorder(root.right)
    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)
    def postorder(self, root):
        if root == None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=" ")
    def levelorder(self, root):
        if root == None:
            return
        queue=[]
        queue.append(root)
        while queue:
            treenode=queue.pop(0)
            print(treenode.data, end=" ")
            if treenode.left:
                queue.append(treenode.left)
            if treenode.right:
                queue.append(treenode.right)


if __name__ == '__main__':
    t = tree()
    for i in range(10,0,-1):
        t.insert(i)
    print("层序遍历：")
    t.levelorder(t.root)
    print("\n前序遍历：")
    t.preorder(t.root)
    print("\n中序遍历：")
    t.inorder(t.root)
    print("\n后序遍历：")
    t.postorder(t.root)
