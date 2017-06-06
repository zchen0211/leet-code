"""
190. Reverse Bits (Easy)

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?
"""

class Solution:
  # @param n, an integer
  # @return an integer
  def reverseBits(self, n):
    # get binary first
    bit_ = [0] * 32
    for i in range(32):
      bit_[i] = n % 2
      n /= 2

    bit_ = bit_[::-1]
    result = 0
    base = 1
    for i in range(32):
      result += bit_[i] * base
      base *= 2
    return result


if __name__ == '__main__':
  a = Solution()
  print a.reverseBits(43261596)
