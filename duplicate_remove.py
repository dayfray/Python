# this function will remove duplicate integers from a list by putting the contents of given list, represented by the argument "double"
# and placing all of its contents into a new list, aptly called "newList", but if a number is already in newList, then it is not
# appended into newList more than once

def remove_duplicates(double):
    newlist = []
    for i in double:
        if i not in newlist:
            newlist.append(i)
    return newlist