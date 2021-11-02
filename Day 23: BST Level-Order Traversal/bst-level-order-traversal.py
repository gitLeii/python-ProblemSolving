

    def levelOrder(self,root):
        #Write your code here
        queue = [root] if root else []
        for node in filter(None, queue):
            print(node.data, end=' ')
            queue += [node.left, node.right]


