"""
Check if a string is palindrome
using recursion
"""

"""
Time Complexity: O(n)
Space Complexity: O(n) stack memory
"""

def checkPalindrome(s,start, end):
    if start > end:
        return True

    if s[start] != s[end]:
        return False

    return checkPalindrome(s,start+1,end-1)

if __name__ == "__main__":
    s = "MADAM"
    ans = checkPalindrome(s, 0, len(s) - 1)
    print(ans)