def square(x):
    return x * x


def successor(x):
    return x + 1


def compose1(f, g):
    def h(x):
        return f(g(x))

    return h#h作为函数和返回值


def f(x):
    """Never called."""
    return -x


square_successor = compose1(square, successor)
result = square_successor(12)
print(result)