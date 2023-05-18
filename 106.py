class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

def buildTree(inorder,postorder):
    node = TreeNode()
    root = postorder[-1]
    root_index = inorder.index(root)

    in_Left = inorder[0:root_index]
    i = 0
    for i in range(len(postorder)):
        if not postorder[i] in in_Left:
            break
    post_Left = postorder[0:i]
    in_right = inorder[root_index+1:len(inorder)]
    post_right = postorder[i:len(postorder)-1]

    node.val = root
    if in_Left != []:
        node.left = buildTree(in_Left,post_Left)
    if in_right != []:
        node.right = buildTree(in_right,post_right)
    return node

def printTree(tree):
    if tree.left == None:
        print('null')
    else:
        printTree(tree.left)
    print(tree.val)
    if tree.right == None:
        print('null')
    else:
        printTree(tree.right)
printTree(buildTree(inorder,postorder))