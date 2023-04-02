
################################################################
# example fibonacci number code;
# you do not have to modify this code in any way
##############################################################


def fibs(n):
    fibs = []
    fibs.append(1)
    if n == 1:
        return fibs
    fibs.append(1)
    while len(fibs) < n:
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


def fib_bad(n):
    return fibs(n)[-1]


def fib(n):
    if n < 2:
        return 1
    f0 = 1
    f1 = 1
    for i in range(n - 1):
        f2 = f1 + f0
        f0 = f1
        f1 = f2
    return f2


##########################################################
# fibonacci number code using generators;
# you will need to implement the functions below
################################################################


class Fib:
    '''
    This class represents all the fibonacci numbers,
    but uses O(1) memory to do so.

    >>> list(Fib(5))
    [1, 1, 2, 3, 5]
    '''
    def __init__(self, n=None):
        self.n = n

    def __iter__(self):
        return FibIter(self.n)

    def __repr__(self):
        if self.n:
            return 'Fib(' + str(self.n) + ')'
        else:
            return 'Fib()'


class FibIter:
    '''
    This is the iterator helper class for the Fib class.
    '''

    def __init__(self, n=None):
        self.n = n
        self.i = 0   # iterator
        self.i1 = 0  # index0
        self.i2 = 1  # index1

    def __next__(self):
        if self.n is not None and self.n <= self.i:
            raise StopIteration
        else:
            self.i += 1
            self.i1, self.i2 = self.i2, (self.i2 + self.i1)
            return self.i1


def fib_yield(n=None):
    '''
    This function returns a generator that
    computes the first n fibonacci numbers.
    If n is none, then the generator is infinite.
    '''
    i1 = 0
    i2 = 1
    if n is None:
        while True:
            i1, i2 = i2, (i2 + i1)
            yield i1
    else:
        for i in range(n):
            i1, i2 = i2, (i2 + i1)
            yield i1
