package leetcode

class Solution {
    fun reverseString(s: CharArray): Unit { // ktlint-disable no-unit-return
        var i = 0
        var j = s.size - 1
        while (i < j) {
            val tmp = s[j]
            s[j] = s[i]
            s[i] = tmp

            i++
            j--
        }
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    var s = charArrayOf('h', 'e', 'l', 'l', 'o')

    solution.reverseString(s)

    val expected = charArrayOf('o', 'l', 'l', 'e', 'h')
    val result = s

    assert(expected contentEquals result)
}
