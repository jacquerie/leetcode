package leetcode

class Solution {
    fun fib(N: Int): Int {
        var current = 0
        var next = 1

        repeat(N) {
            val tmp = next
            next = current + next
            current = tmp
        }

        return current
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    assert(1 == solution.fib(2))
    assert(2 == solution.fib(3))
    assert(3 == solution.fib(4))
}
