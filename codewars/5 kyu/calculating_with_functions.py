def identity(x): return x

def zero(func=identity): return func(0)
def one(func=identity): return func(1)
def two(func=identity): return func(2)
def three(func=identity): return func(3)
def four(func=identity): return func(4)
def five(func=identity): return func(5)
def six(func=identity): return func(6)
def seven(func=identity): return func(7)
def eight(func=identity): return func(8)
def nine(func=identity): return func(9)

def plus(b): return lambda a: a + b
def minus(b): return lambda a: a - b
def times(b): return lambda a: a * b
def divided_by(b): return lambda a: a // b