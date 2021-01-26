
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
def titleize(phrase):
  
  return phrase.title()

print(titleize('oNLy cAPITALIZe fIRSt'))