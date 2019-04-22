package leetcode

class Solution {
    fun largestPerimeter(A: IntArray): Int {
        A.sortDescending()
        for (i in 0..A.size - 3) {
            if (A[i + 2] + A[i + 1] > A[i]) {
                return A[i + 2] + A[i + 1] + A[i]
            }
        }
        return 0
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    assert(5 == solution.largestPerimeter(intArrayOf(2, 1, 2)))
    assert(0 == solution.largestPerimeter(intArrayOf(1, 2, 1)))
    assert(10 == solution.largestPerimeter(intArrayOf(3, 2, 3, 4)))
    assert(8 == solution.largestPerimeter(intArrayOf(3, 6, 2, 3)))
}
