package leetcode

class Solution {
    fun lengthOfLastWord(s: String): Int {
        var j = s.length - 1
        while (j >= 0 && s[j] == ' ')
            j--

        var i = j
        while (i >= 0 && s[i] != ' ')
            i--

        return j - i
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    assert(5 == solution.lengthOfLastWord("Hello World"))
    assert(1 == solution.lengthOfLastWord("a"))
    assert(1 == solution.lengthOfLastWord("a "))
}
