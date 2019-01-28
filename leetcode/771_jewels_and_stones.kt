package leetcode

class Solution {
    fun numJewelsInStones(J: String, S: String): Int {
        var result = 0

        for (c in S) {
            if (J.indexOf(c) != -1) {
                result++
            }
        }

        return result
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    assert(3 == solution.numJewelsInStones("aA", "aAAbbbb"))
    assert(0 == solution.numJewelsInStones("z", "ZZ"))
}
