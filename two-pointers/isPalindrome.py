def isPalindrome(s):

    # Removes all whitespaces, special characters like comma, colon, exclamation etc.
    new_str = ''.join(char.lower() for char in s if char.isalnum())

    left = 0  
    right = len(new_str) - 1

    # Two pointer approach
    while left < right:
        if new_str[left] != new_str[right]:
            return False
        left += 1
        right -= 1

    return True

