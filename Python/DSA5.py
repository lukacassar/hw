class Stack:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        return f"Current stack contents: {self.items}"
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            print("Cannot pop an empty stack. Program will now terminate.")
            exit(1)
        else:
            return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            print("There are no elements in the stack")
        else:
            return self.items[-1]
    
    def is_empty(self):
        if self.size() == 0:
            return True
    
    def size(self):
        return len(self.items)
    
    
def eval(expression):
    contents = expression.split()

    if not contents:
        print("You did not input anything. Program will now terminate. ")
        exit(1)
    
    stack = Stack()
    operators = ['+', '-', 'x', '/']

    for i in contents:
        print(f"Evaluating {i}")
        try:
            i = float(i)
            stack.push(i)
        except ValueError:
            if i not in operators:
                print(f"Operator {i} is invalid. Program will now terminate")
                exit(1)
            elif i in operators:
                if stack.size() < 2:
                    print(f"Not enough numbers in the stack for operator {i}. Program will now terminate.")
                    exit(1)
                else:
                    b = stack.pop()
                    a = stack.pop()
                    if i == '+':
                        stack.push(a + b)
                    elif i == '-':
                        stack.push(a - b)
                    elif i == 'x':
                        stack.push(a * b)
                    elif i == '/':
                        if b == 0:
                            print("Cannot divide by zero. Program will now terminate.")
                            exit(1) 
                        stack.push(a / b)
        print(stack)

    if stack.size() != 1:
            print("There are still additional contents in the stack and not enough operators. Invalid RPN entry. Program will now terminate")
            exit(1)
    else: 
        print(f"The answer is {stack.peek()}")
    

entry = input("Enter a valid RPN expression, separated by a space to denote the next item in the stack \n")
eval(entry)


