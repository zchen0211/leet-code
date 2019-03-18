"""
657. Judge Route Circle (Easy)

Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
"""


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        n = len(moves)
        if n == 0:
            return True
        if n % 2 == 1:
            return False
        record = [0, 0]
        for i in range(len(moves)):
            if moves[i] == "L":
                record[0] -= 1
            elif moves[i] == "R":
                record[0] += 1
            elif moves[i] == "U":
                record[1] -= 1
            else:
                record[1] += 1
        if record[0] == 0 and record[1] == 0:
            return True
        else:
            return False
