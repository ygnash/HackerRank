############################################################################
#    ginortS
"""
You are given a string S. It contains alphanumeric characters only.
Sort the string such that,
    All sorted lowercase letters are ahead of uppercase letters.
    All sorted uppercase letters are ahead of digits.
    All sorted odd digits are ahead of sorted even digits.

    Sample IP --> Sorting1234
    Sample OP --> ginortS1324
"""
#---------------------------------------------------------------------------
#SOLUTION 1
def sort_string(s):
    u,l,o,e = ['','','','']

    for c in s:
        if ord(c) >= 65 and ord(c) <= 90:
            u += c
        elif ord(c) >= 97 and ord(c) <= 122:
            l += c
        elif ord(c) in [49,51,53,55,57]:
            o += c
        else:
            e += c

    print(''.join(sorted(l)+sorted(u)+sorted(o)+sorted(e)))

# SOLUTION 2 - REGEX
import re

def sort_string_regex(s):
    string = ''.join(sorted(s))
    l = re.search(r'[a-z]+',string).group(0)
    u = re.search(r'[A-Z]+', string).group(0)
    o = ''.join(re.findall(r'[13579]+',string))
    e = ''.join(re.findall(r'[24680]+', string))
    print(l+u+o+e)



if __name__ == "__main__":
    # sort_string(input().strip())
    sort_string_regex(input())

#---------------------------------------------------------------------------
