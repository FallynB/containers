def range(a, b=None, c=None):
    if b is not None:
        begin = a 
        end = b 
    else:
        begin = 0 
        end = a 
    if c is not None:
        skip = c 
    if c is None:
        skip = 1 
    i = begin
    while (skip > 0 and i < end) or (skip < 0 and i > end):
        yield i
        i += skip

