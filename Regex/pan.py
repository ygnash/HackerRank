############################################################################
#    PAN number validation
"""
The equivalent of SSN in India is a PAN number, which is unique to each of its citizens.
 In any of the country's official documents, the PAN number is listed as follows

<char><char><char><char><char><digit><digit><digit><digit><char>

Your task is to figure out if the PAN number is valid or not.
A valid PAN number will have all its letters in uppercase and digits in the same order as listed above.
"""
#---------------------------------------------------------------------------
import re

regex = re.compile(r'^[A-Z]{5}\d{4}[A-Z]$')
print(*['YES' if regex.fullmatch(input()) else 'NO' for _ in range(int(input()))], sep = '\n')

#---------------------------------------------------------------------------
