package leetcode

class Solution {
    fun distributeCandies(candies: IntArray): Int {
        return minOf(candies.size / 2, candies.toSet().size)
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    assert(3 == solution.distributeCandies(intArrayOf(1, 1, 2, 2, 3, 3)))
    assert(2 == solution.distributeCandies(intArrayOf(1, 1, 2, 3)))
}
