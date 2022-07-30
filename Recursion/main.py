def rreverse(word):
    """
    Reverse the string
    """
    if word == '':
        return word
    else:
        return rreverse(word[1:]) + word[0]


def revlist(lst):
    """
    Reverse list
    """
    if len(lst) == 0:
        return []
    else:
        return revlist(lst[1:]) + [lst[0]]


def rev_list_in_place(s, offset=0):
    """
    Reverse List In-Place. No return required since it is in-place.

    The entire logic for reversing a list is based on using the opposite directional two-pointer approach!
    So use two pointers, left and right.
    The left pointer points to the first index of the list and the right pointer points to the last index of the list.
    Now we swap the elements pointed to by these pointers. Then, we move the pointer to the next indices.
    The terminating condition of this would be when the left pointer equals or crosses over the right pointer.
    """
    if len(s) > offset * 2:  # Check whether the mid is crossed
        s[offset], s[-offset - 1] = s[-offset - 1], s[offset]  # Swap the values in list
        rev_list_in_place(s, offset + 1)  # Increment Offset


def check_sorted(arr):
    """
    Given an array, check whether array is sorted or not
    """
    if len(arr) == 1:
        return True
    else:
        return arr[0] <= arr[1] and check_sorted(arr[1:])
