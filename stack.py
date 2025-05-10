import string


class Stack:
    def __init__(self) -> None:
        self.stack = []

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        return self.stack[-1]

    def size(self) -> int:
        return len(self.stack)

    def pop(self):
        return self.stack.pop()


def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index += 1

    if balanced and s.is_empty():
        return True
    return False


def devide_by_2(dec_number):
    remstack = Stack()

    while dec_number > 0:
        rem = dec_number % 2
        remstack.push(rem)
        dec_number = dec_number // 2

    bin_str = ""
    while not remstack.is_empty():
        bin_str += str(remstack.pop())

    return bin_str


def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while dec_number > 0:
        rem = dec_number % base
        remstack.push(rem)
        dec_number //= base

    new_str = ""
    while not remstack.is_empty():
        new_str += digits[remstack.pop()]

    return new_str

def infix_to_postfix(infix_expr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    op_stack = Stack()
    postfix_list = []

    token_list = infix_expr.split()

    for token in token_list:
        if token in string.ascii_uppercase:
            postfix_list.append(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and \
                (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)
    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return " ".join(postfix_list)
