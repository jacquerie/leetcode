package leetcode

import kotlin.math.abs

class Solution {
    fun sortedSquares(A: IntArray): IntArray {
        var result = IntArray(A.size)

        var i = 0
        var j = A.size - 1
        var k = 0
        while (i <= j) {
            if (abs(A[i]) < abs(A[j])) {
                result[k] = A[j] * A[j]
                j--
            } else {
                result[k] = A[i] * A[i]
                i++
            }

            k++
        }

        result.reverse()

        return result
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    val A = intArrayOf(-4, -1, 0, 3, 10)

    val expected = intArrayOf(0, 1, 9, 16, 100)
    val result = solution.sortedSquares(A)

    assert(expected contentEquals result)
}
