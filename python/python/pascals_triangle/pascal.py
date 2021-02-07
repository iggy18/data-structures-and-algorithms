def pascal_triangle(n):
    trow = [1]
    y = [0]
    results = [[1]]
    for x in range(max(n,0)):
        trow=[l+r for l,r in zip(trow+y, y+trow)]
        results.append(trow)
    return results
