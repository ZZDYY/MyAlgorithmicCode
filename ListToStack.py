
class Stack(object):
    '''栈先进后出'''
    def __init__(self):
        self.array = [[], []]
 
    def l_push(self, data):
        self.array[0].append(data)
 
    def l_pop(self):
        if len(self.array[0]) == 0:
            print('Stack left is empty')
        else:
            self.array[0].pop()
 
    def r_push(self, data):
        self.array[1].append(data)
 
    def r_pop(self):
        if len(self.array[1]) == 0:
            print('Stack right is empty')
        else:
            self.array[1].pop()
 
    def show(self):
        if len(self.array[0]) == 0:
            print('Stack left is empty')
        else:
            print('Stack left:', self.array[0])
        if len(self.array[1]) == 0:
            print('Stack right is empty')
        else:
            print('Stack right:',self.array[1])

if __name__ == '__main__':
    stack = Stack()
    # 左边入栈
    stack.l_push(1)
    stack.show()
    stack.l_push(2)
    # 左边出栈
    stack.l_pop()
    stack.show()
    # 右边入栈
    stack.r_push(3)
    stack.show()
    # 右边出栈
    stack.r_pop()
    stack.show()