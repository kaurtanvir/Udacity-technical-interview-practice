"""
Question 1
Given two strings s and t, determine whether some anagram of t is a substring
of s. For example: if s = "udacity" and t = "ad", then the function returns
True. Your function definition should look like: question1(s, t) and return a
boolean True or False.
"""

# Helper function to check if two strings are anagram of each other
def anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def question1(s, t):
    t_len = len(t)
    s_len = len(s)
    t_sort = sorted(t)
    for i in range(s_len - t_len + 1):
        if anagram(s[i: i+t_len], t_sort):
            return True
    return False


# Case 1: ("udacity", "ad") 
print question1("udacity","ad")
# True

# Case 2: ("udacity", "")
print question1("udacity","")
# True

# Case 3: ("ad", "udacity" ) 
print question1("ad","udacity")
# False

# Case 4 : ("1987652034","10")
print question1("1987651034","10")
# True

"""
Question 2
Given a string a, find the longest palindromic substring contained in a. Your function definition should look like question2(a), and return a string.
"""
def question2(a):
    max_length = 1
    length = len(a)
    beginIndex = 0
    table = [[False for x in range(length)] for y in range(length)]
    for i in range(length):
        table[i][i] = True
    for i in range(length-1):
        if a[i] == a[i+1]:
            table[i][i+1] = True
            max_length = 2
            beginIndex = i

    curr_len = 3
    while curr_len <= length:
        for i in range(length-curr_len+1):
            j = i+curr_len-1
            if (table[i+1][j-1] and a[i] == a[j]):
                table[i][j] = True
                max_length = curr_len
                beginIndex = i
        curr_len+=1

    return a[beginIndex:beginIndex+max_length]

# Case 1:  
print question2("bananas")
# anana

# Case 2:
print question2("")
#

# Case 3: 
print question2("babad")
# aba






