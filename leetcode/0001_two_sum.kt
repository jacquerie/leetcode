package leetcode

class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val result = IntArray(2)

        val seen = mutableMapOf<Int, Int>()
        nums.forEachIndexed { i, num ->
            val j = seen.get(target - num)
            if (j != null) {
                result[0] = j
                result[1] = i
            }

            seen.put(num, i)
        }

        return result
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    val nums = intArrayOf(2, 7, 11, 15)

    val expected = intArrayOf(0, 1)
    val result = solution.twoSum(nums, 9)

    assert(expected contentEquals result)
}
