package leetcode

class Solution {
    fun repeatedNTimes(A: IntArray): Int {
        var result = 0

        val seen = mutableSetOf<Int>()
        for (el in A) {
            if (seen.contains(el)) {
                result = el
            }

            seen.add(el)
        }

        return result
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    assert(3 == solution.repeatedNTimes(intArrayOf(1, 2, 3, 3)))
    assert(2 == solution.repeatedNTimes(intArrayOf(2, 1, 2, 5, 3, 2)))
    assert(5 == solution.repeatedNTimes(intArrayOf(5, 1, 5, 2, 5, 3, 5, 4)))
}
