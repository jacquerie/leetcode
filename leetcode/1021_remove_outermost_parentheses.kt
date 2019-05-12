package leetcode

class Solution {
    fun removeOuterParentheses(S: String): String {
        val result = mutableListOf<Char>()

        var count = 0
        for (c in S) {
            if (c == '(') {
                if (count > 0) {
                    result.add(c)
                }

                count++
            } else if (c == ')') {
                if (count > 1) {
                    result.add(c)
                }

                count--
            }
        }

        return result.joinToString("")
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    assert("()()()" == solution.removeOuterParentheses("(()())(())"))
    assert("()()()()(())" == solution.removeOuterParentheses("(()())(())(()(()))"))
    assert("" == solution.removeOuterParentheses("()()"))
}
