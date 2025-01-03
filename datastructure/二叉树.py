# 学生 屠浩天
# 2025年01月02日14时08分13秒
class Node(object):
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
    def __init__(self):
        self.root = Node()
        self.myQueue = []
    def add(self, elem):

        node = Node(elem)
        if self.root.elem == -1:  # 如果树是空的，则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]  # 此结点的子树还没有齐。
            if treeNode.lchild == None:
                treeNode.lchild = node
                self.myQueue.append(treeNode.lchild)
            else:
                treeNode.rchild = node
                self.myQueue.append(treeNode.rchild)
                self.myQueue.pop(0)  # 如果该结点存在右子树，将此结点

    def front_digui(self, root):
        """利用递归实现树的先序遍历"""
        if root == None:
            return
        print(root.elem, end="")
        self.front_digui(root.lchild)
        self.front_digui(root.rchild)

    def middle_digui(self, root):
        """利用递归实现树的中序遍历"""
        if root == None:
            return
        self.middle_digui(root.lchild)
        print(root.elem, end="")
        self.middle_digui(root.rchild)

    def later_digui(self, root):
        if root == None:
            return
        self.later_digui(root.lchild)
        self.later_digui(root.rchild)
        print(root.elem, end="")

    def level_queue(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.elem, end="")
            if node.lchild != None:
                myQueue.append(node.lchild)
            if node.rchild != None:
                myQueue.append(node.rchild)

if __name__ == '__main__':
    """主函数"""
elems = range(10)  # 生成十个数据作为树节点
tree = Tree()  # 新建一个树对象
for elem in elems:
    tree.add(elem)  # 逐个添加树的节点

print('队列实现层次遍历:')
tree.level_queue(tree.root)
# print('\n\n 递归实现先序遍历:')
# tree.front_digui(tree.root)
# print('\n 递归实现中序遍历:')
# tree.middle_digui(tree.root)
# print('\n 递归实现后序遍历:')
# tree.later_digui(tree.root)
