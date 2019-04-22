package leetcode

import java.util.Deque
import java.util.LinkedList

class Solution {
    fun isValid(s: String): Boolean {
        val stack: Deque<Char> = LinkedList()

        for (c in s) {
            if (c == '(') {
                stack.addLast(')')
            } else if (c == '[') {
                stack.addLast(']')
            } else if (c == '{') {
                stack.addLast('}')
            } else {
                val top = stack.pollLast()
                if (top == null || top != c) {
                    return false
                }
            }
        }

        return stack.size == 0
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    assert(solution.isValid("()"))
    assert(solution.isValid("()[]{}"))
    assert(!solution.isValid("(]"))
    assert(!solution.isValid("([)]"))
    assert(solution.isValid("{[]}"))
    assert(!solution.isValid("]"))
    assert(!solution.isValid("["))
}
