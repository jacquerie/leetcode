package leetcode

class Solution {
    fun findComplement(num: Int): Int {
        return num.toString(2).map({ digit ->
            if (digit == '0') '1' else '0'
        }).joinToString("").toInt(2)
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    assert(2 == solution.findComplement(5))
    assert(0 == solution.findComplement(1))
}
