'''class Node:
    def __init__(self,data=None):
        self.data = data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top=new_node
    def pop(self):
        if self.top is not None:
            popped_data = self.top.data
            self.top=self.top.next
            return popped_data
        else:
            return None
    def display(self):
        current =self.top
        while current:
            print('current data: ',end =' ')
            current = current.next
        print()


stack1 = Stack()
stack1.push(1)
stack1.push(3)
stack1.push(5)
stack1.push(6)
print('stack elements are ',end=' ')
stack1.display()
stack1.pop()
stack1.pop()
print('stack elements',end=' ')
stack1.display()
stack1.push(9)
stack1.push(8)
print("Stack elements are:", end=' ')
stack1.display()

'''

stack = [1, 3, 5, 6]

print("Stack elements are:", stack)

# Remove 2 elements from the stack
stack.pop()
stack.pop()

print("Stack elements are:", stack)

# Input 2 more elements
stack.extend([9, 8])

print("Stack elements are:", stack)