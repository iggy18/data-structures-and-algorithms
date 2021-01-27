def add_matrix(arr):
    if not arr:
        return 0
    products = []
    for list in arr:
        products.append(sum(list))
    return products
