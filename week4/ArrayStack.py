#python 
class ArrayStack :
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.capacity - 1

    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = e
        else:
            print("스택 포화 에러/ 해당 항목 :", e)
            pass
        
    def pop(self):
        if not self.isEmpty():  
            self.top -= 1
            return self.array[self.top + 1]
        else:
            print("스택 공백 에러")
            pass

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            print("스택 공백 에러")
            pass

    def __str__(self):
        return str(self.array[0:self.top+1])

    def display(self):
        print(f"[스택 항목의 수 = {self.top + 1}] ==> ", end="")
        print(self)


if __name__ == "__main__":
    stack = ArrayStack(2)
    print("test ArrayStack module")
    #test stack
    print("isEmpty:", stack.isEmpty())
    print("isFull:", stack.isFull())
    stack.display()
    #----------------------------
    stack.push(10)
    stack.push(20)
    print("peek:", stack.peek())
    print("pop:", stack.pop())
    stack.display()
    print("isEmpty:", stack.isEmpty())
    print("isFull:", stack.isFull())
    #----------------------------
    stack.pop()
    stack.display()
    stack.pop()
    stack.display()
    print("isEmpty:", stack.isEmpty())
    print("isFull:", stack.isFull())
    #----------------------------
    print("pop:", stack.pop())
    stack.display()
    print("isEmpty:", stack.isEmpty())
    print("isFull:", stack.isFull())
    print(stack)
    #----------------------------
    stack.push("사과")
    stack.push("배")
    stack.push("귤")
    stack.push("포도")
    stack.push("수박")
    print("isEmpty:", stack.isEmpty())
    print("isFull:", stack.isFull())
    stack.display()
    print(stack)