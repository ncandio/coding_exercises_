def fourNumberSum(array, targetSum):
    # Write your code here.
    return [(x,y,z,w) for x in array
                      for y in array
                      for z in array
                      for w in array
                      if (x+y+z+w == targetSum) 
                      and x<y<z<w]