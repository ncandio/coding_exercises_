def moveElementToEnd(array, toMove):
    # Write your code here.
    return sorted(array, key=lambda x: x == toMove)