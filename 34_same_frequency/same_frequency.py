
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
def same_frequency(num1, num2):

  if sorted(str(num1)) == sorted(str(num2)):
    return True
  else:
    return False
  
print(same_frequency(321142, 3212215))