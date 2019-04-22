package leetcode

class Solution {
    fun hammingDistance(x: Int, y: Int): Int {
        val xs = x.toString(2).padStart(32, '0')
        val ys = y.toString(2).padStart(32, '0')

        return (xs.zip(ys) { xc, yc -> xc != yc }).count({ zb -> zb })
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    assert(2 == solution.hammingDistance(1, 4))
}
