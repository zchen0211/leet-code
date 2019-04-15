class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        self.stat = {1: False, 2: True, 3: False}

        def helper(m):
            for i in range(1, m // 2 + 1):
                if m % i == 0:
                    if (m-i) in self.stat and self.stat[m-i] == False:
                        self.stat[m] = True
                        return True
                    if (m-i) not in self.stat and helper(m-i) == False:
                        self.stat[m] = True
                        return True
            self.stat[m] = False
            return False

        helper(N)
        print(self.stat)
        return self.stat[N]


if __name__ == "__main__":
    a = Solution()
    print(a.divisorGame(6))