# notice set(a) < set(b) to judge subset!

class Solution(object):
  def findWords(self, words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    dict_list = []
    dict_list.append(set(['q','w','e','r','t','y','u','i','o','p']))
    dict_list.append(set(['a','s','d','f','g','h','j','k','l']))
    dict_list.append(set(['z','x','c','v','b','n','m']))
    result = []
    for item in words:
      item_list = list(item.lower())
      tmp_ = False
      for i in range(3):
        if set(item_list) <= dict_list[i]:
          tmp_ = True
          break
      if tmp_:
        result.append(item)
    return result


if __name__ == '__main__':
  a = Solution()
  print a.findWords(['hello', 'Alaska', 'dad', 'peace'])
