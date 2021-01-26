
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """
def three_odd_numbers(nums):
  
    temp = (nums for num in range(len(nums) - 3 + 1)) 

    res = any(sum(el % 2 for el in temps) % 3 == 0 for temps in temp)
    
    return res
  

  
print(three_odd_numbers([1, 2, 3, 4, 5]))