class Node:
    def __init__(self,data):
        self.data=str(data)
        self.next=None

    def __str__(self):        return self.data
def addFirst(root,data):
    newnode=Node(data)
    if root.next==None:
        # print("One")
        newnode.next=None
        root.next=newnode
    else:
        # print("Two")
        newnode.next=root.next
        root.next=newnode
def traverse(root):
    while root.next!=None:
        print(f"{root.data}",end=",")
        root=root.next
        
root=Node("")
# print(root)
for i in range(10):
    addFirst(root,str(chr(-1+i+ord("A"))))
 
traverse(root)
print()