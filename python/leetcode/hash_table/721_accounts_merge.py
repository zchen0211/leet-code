"""
721. Accounts Merge (Medium)

Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account, in sorted order.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the format they were given: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation: 
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
"""

class Solution(object):
  def accountsMerge(self, accounts):
    """
    :type accounts: List[List[str]]
    :rtype: List[List[str]]
    """
    n = len(accounts)
    par_map = [-1] * n

    em_2_id = {}
    for i in range(n):
      account = accounts[i]
      for email in account[1:]:
        if email not in em_2_id:
          em_2_id[email] = i
        else:
          id1 = em_2_id[email]
          id2 = i
          while par_map[id1] != -1:
            id1 = par_map[id1]
          while par_map[id2] != -1:
            id2 = par_map[id2]
          if id1 != id2:
            id1, id2 = min(id1, id2), max(id1, id2)
            par_map[id2] = id1
      print em_2_id
      print par_map

    ret = {}
    for email in em_2_id.keys():
      id_ = em_2_id[email]
      while par_map[id_] != -1:
        id_ = par_map[id_]
      if id_ not in ret:
        ret[id_] = []
      ret[id_].append(email)
    print ret

    result = []
    for k in ret.keys():
      tmp = []
      tmp.append(accounts[k][0])
      ret[k].sort()
      for item in ret[k]:
        tmp.append(item)
      result.append(tmp)

    # finally tackle empty accounts
    for account in accounts:
      if len(account) == 1:
        result.append(account)

    return result

if __name__ == "__main__":
  a = Solution()
  accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"], ['X']]
  print a.accountsMerge(accounts)
