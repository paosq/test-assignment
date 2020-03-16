def rectangle_area(a, b):
    """
    Calculates the area of a rectangle given its side lengths

    :param a: first side of the rectangle
    :param b: second side of the rectangle
    :return: area of the rectangle
    :raises ValueError: if either number was negative
    """ 
    if a>0 and b>0:
      return a*b
    else: return "bład"
print(rectangle_area(-1,2))
