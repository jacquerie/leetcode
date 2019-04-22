package leetcode

class Solution {
    fun isPowerOfFour(num: Int): Boolean {
        return (
            num == 1 ||
            num == 4 ||
            num == 16 ||
            num == 64 ||
            num == 256 ||
            num == 1024 ||
            num == 4096 ||
            num == 16384 ||
            num == 65536 ||
            num == 262144 ||
            num == 1048576 ||
            num == 4194304 ||
            num == 16777216 ||
            num == 67108864 ||
            num == 268435456 ||
            num == 1073741824
        )
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    assert(solution.isPowerOfFour(16))
    assert(!solution.isPowerOfFour(5))
}
