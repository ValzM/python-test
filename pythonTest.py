def isLeapYear(year):
    """
    Check if the year is Leap

    @param(int) : the year
    @return(bool) : A boolean to tell if the year is leap
    """
    if year%4 == 0 and year%100 != 0:
        return True
    elif year%400 == 0:
        return True
    return False

print(isLeapYear(2004))
