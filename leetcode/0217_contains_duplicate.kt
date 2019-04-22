package leetcode

class Solution {
    fun containsDuplicate(nums: IntArray): Boolean {
        val seen = mutableSetOf<Int>()
        for (num in nums) {
            if (seen.contains(num)) {
                return true
            }

            seen.add(num)
        }

        return false
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    assert(solution.containsDuplicate(intArrayOf(1, 2, 3, 1)))
    assert(!solution.containsDuplicate(intArrayOf(1, 2, 3, 4)))
    assert(solution.containsDuplicate(intArrayOf(1, 1, 1, 3, 3, 4, 3, 2, 4, 2)))
}
