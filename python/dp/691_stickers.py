"""
691. Stickers to Spell Word (Hard)

We are given N different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given target string by cutting individual letters from your collection of stickers and rearranging them.

You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

What is the minimum number of stickers that you need to spell out the target? If the task is impossible, return -1.

Example 1:

Input:

["with", "example", "science"], "thehat"
Output:

3
Explanation:

We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.
Example 2:

Input:

["notice", "possible"], "basicbasic"
Output:

-1
Explanation:

We can't form the target "basicbasic" from cutting letters from the given stickers.
Note:

stickers has length in the range [1, 50].
stickers consists of lowercase English words (without apostrophes).
target has length in the range [1, 15], and consists of lowercase English letters.
In all test cases, all words were chosen randomly from the 1000 most common US English words, and the target was chosen as a concatenation of two random words.
The time limit may be more challenging than usual. It is expected that a 50 sticker test case can be solved within 35ms on average.

"""


class Solution(object):
  def minStickers(self, stickers, target):
    """
    :type stickers: List[str]
    :type target: str
    :rtype: int
    """
    n = len(stickers)
    if n == 0: return -1

    st_enc = []
    for word in stickers:
      tmp = [0] * 26
      for c in word:
        idx = ord(c) - ord('a')
        tmp[idx] += 1
      st_enc.append(tmp)

    tgt_enc = [0] * 26
    for c in target:
      idx = ord(c) - ord('a')
      tgt_enc[idx] += 1
      # check do-able here
      max_idx = max([item[idx] for item in st_enc])
      if max_idx == 0: return -1
    print 'encoding', st_enc
    self.map_ = {} # save dp results
    res = self.dp(tgt_enc, st_enc)
    return res

  def dp(self, tgt_enc, st_enc):
    print 'here', tgt_enc
    # edge case I:
    if max(tgt_enc) == 0: return 0

    # edge case II: already found
    if tuple(tgt_enc) in self.map_: return self.map_[tuple(tgt_enc)]

    print 'not found'

    n = len(st_enc)
    matching = []
    for i in range(n):
      item = st_enc[i]
      flag = True
      for j in range(26):
        if tgt_enc[j] > item[j]:
          flag = False
          break
      if flag:
        print 'smaller than', item
        self.map_[tuple(tgt_enc)] = 1
        return 1
      else:
        match_ = [min(item[j], tgt_enc[j]) for j in range(26)]
        matching.append(match_)
    print 'not smaller'

    # dp
    result = sum(tgt_enc)
    for i in range(n):
      if sum(matching[i]) > 0:
        # try it
        new_target = [max(tgt_enc[j]-matching[i][j], 0) for j in range(26)]
        print new_target
        res = 1 + self.dp(new_target, st_enc)
        # update result
        result = min(result, res)
    self.map_[tuple(tgt_enc)] = result
    return result
    '''
    # greedy
    result = 0
    while max(tgt_enc) > 0:
      id_, max_ = -1, -1
      for i in range(n):
        item = st_enc[i]
        matching = [min(item[j], tgt_enc[j]) for j in range(26)]
        matching = sum(matching)
        print i, matching
        if matching >= max_:
          id_, max_ = i, matching
      print id_
      print stickers[id_], matching,
      # select it
      tgt_enc = [max(tgt_enc[i]-st_enc[id_][i], 0) for i in range(26)]
      print tgt_enc
      result += 1
    return result
    '''
if __name__ == "__main__":
  a = Solution()
  # print a.minStickers(["with", "example", "science"], "thehat")
  # print a.minStickers(["notice", "possible"], "basicbasic")
  # print a.minStickers(["these","guess","about","garden","him"], "atomher")
  '''
  arr = ["control","heart","interest","stream","sentence","soil","wonder","them","month","slip","table","miss","boat","speak","figure","no","perhaps","twenty","throw","rich","capital","save","method","store","meant","life","oil","string","song","food","am","who","fat","if","put","path","come","grow","box","great","word","object","stead","common","fresh","the","operate","where","road","mean"]
  target = "stoodcrease"
  '''
  arr = ["degree","set","old","help","crowd","supply","wall","certain","press","paper","result","any","low","material","scale","log","tire","section","offer","please","port","to","too","party","tell","choose","good","beauty","nature","company","after","tool","insect","said","hear","value","foot","come","property","room","lost","this","many","clear","drop","job","us","while","common","voice"]
  target = "dresspost"
  print a.minStickers(arr, target)
