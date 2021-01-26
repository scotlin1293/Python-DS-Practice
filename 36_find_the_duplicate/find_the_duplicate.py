
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """

def find_the_duplicate(nums):

  seen = set()

  seen_add = seen.add

  seen_twice = set( num for num in nums if num in seen or seen_add(num))
  
  if seen_twice:
    return list(seen_twice)
      
      
print(find_the_duplicate([6, 1, 9, 5, 3, 4, 9]))