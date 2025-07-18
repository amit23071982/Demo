def solution(s):

    left = 0
    right = len(s) - 1
    matches = 0

    while left < right:
        if s[left] != s[right]:
            break
        matches += 1
        left += 1
        right -= 1
    return matches

    


