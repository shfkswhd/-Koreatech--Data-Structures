#infix to postfix converter
from ArrayStack import *

def evalPostfix( expr ):
    s = ArrayStack(100)
    for token in expr:
        if token in "+-*/": # 연산자이면
            val2 = s.pop()
            val1 = s.pop()
            if token == '+': s.push(val1 + val2)
            elif token == '-': s.push(val1 - val2)
            elif token == '*': s.push(val1 * val2)
            elif token == '/': s.push(val1 / float(val2))
        else: # 피연산자이면
            s.push( float(token) )

    return s.pop()

def infix2postfix( expr ):
    s = ArrayStack(100)
    postfix = []
    prec = { '*':3, '/':3, '+':2, '-':2, '(':1 } # 우선순위
    for token in expr:
        if token in "+-*/": # 연산자이면
            while (not s.isEmpty()) and (prec[s.peek()] >= prec[token]):
                postfix.append( s.pop() )
            s.push(token)
        elif token == '(': # 여는 괄호이면
            s.push(token)
        elif token == ')': # 닫는 괄호이면
            topToken = s.pop()
            while topToken != '(': # 여는 괄호가 나올 때까지
                postfix.append(topToken)
                topToken = s.pop()
        else: # 피연산자이면
            postfix.append(token)

    while not s.isEmpty(): # 스택에 남아있는 연산자 pop
        postfix.append( s.pop() )

    return postfix

if __name__ == "__main__":

    expr = input("입력 수식(공백문자로 분리) = ").split(" ")
    print(f"중위표기: {expr}")
    print(f"후위표기식: {infix2postfix(expr)}")
    print(f"계산결과: {evalPostfix(infix2postfix(expr))}")