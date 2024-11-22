"""
You are given an m x n binary matrix matrix.

You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

Return the maximum number of rows that have all values equal after some number of flips.

 

Example 1:

Input: matrix = [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.
Example 2:

Input: matrix = [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.
Example 3:

Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.
"""

from collections import Counter

def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
    # convert each row into tuple, where each value is the continuous num of either 1 or 0 
    def get_pattern(row):
        pattern = []
        current = row[0]
        count = 0
        for value in row:
            if value == current:
                count += 1
            else:
                pattern.append(count)
                current = value
                count = 1
        pattern.append(count)
        return tuple(pattern)

    patterns = [get_pattern(row) for row in matrix]
    return max(Counter(patterns).values())

testCases = [
[[1,0,0,0,0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1,1,1,1,0]],
[[1,1],[0,1],[1,0],[0,0],[1,0],[1,0],[0,1],[1,0],[0,0],[1,0]],
[[0,0,0],[0,1,0],[0,0,1],[0,0,0],[0,0,0],[1,1,0],[1,1,1],[1,1,1],[1,1,1],[1,0,1]],
]

for case in testCases:
    pritn(maxEqualRowsAfterFlips(testCases))