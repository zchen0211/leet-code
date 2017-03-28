'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
'''

class Solution(object):
  def compareVersion(self, version1, version2):
    v1_list = version1.split('.')
    v2_list = version2.split('.')

    v1_n = len(v1_list)
    v2_n = len(v2_list)

    for i in range(min(v1_n, v2_n)):
      if int(v1_list[i]) > int(v2_list[i]):
        return 1
      elif int(v1_list[i]) < int(v2_list[i]):
        return -1

    # go through remaining
    if v1_n > v2_n:
      for i in range(v2_n, v1_n):
        if int(v1_list[i]) > 0:
          return 1
    elif v2_n > v1_n:
      for i in range(v1_n, v2_n):
        if int(v2_list[i]) > 0:
          return -1
      
    return 0

