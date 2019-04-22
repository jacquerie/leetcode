package leetcode

class Solution {
    fun isToeplitzMatrix(matrix: Array<IntArray>): Boolean {
        for (i in 1..matrix.size - 1) {
            for (j in 1..matrix[0].size - 1) {
                if (matrix[i - 1][j - 1] != matrix[i][j]) {
                    return false
                }
            }
        }

        return true
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    assert(
        solution.isToeplitzMatrix(
            arrayOf(
                intArrayOf(1, 2, 3, 4),
                intArrayOf(5, 1, 2, 3),
                intArrayOf(9, 5, 1, 2)
            )
        )
    )
    assert(
        !solution.isToeplitzMatrix(
            arrayOf(
                intArrayOf(1, 2),
                intArrayOf(2, 2)
            )
        )
    )
}
