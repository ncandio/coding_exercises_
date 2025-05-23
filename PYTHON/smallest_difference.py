def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.#
    smallest_diff = sorted([(x,y) for x in arrayOne for y in arrayTwo],
    key=lambda pair: (abs(pair[0] - pair[1]), pair[0], pair[1]))
    return smallest_diff[0]