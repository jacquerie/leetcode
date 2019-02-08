package leetcode

class Interval(var start: Int = 0, var end: Int = 0)

class Solution {
    fun intervalIntersection(A: Array<Interval>, B: Array<Interval>): Array<Interval> {
        val result = mutableListOf<Interval>()

        var i = 0
        var j = 0
        while (i < A.size && j < B.size) {
            if (A[i].end < B[j].start) {
                i++
            } else if (B[j].end < A[i].start) {
                j++
            } else {
                result.add(
                    Interval(
                        maxOf(A[i].start, B[j].start),
                        minOf(A[i].end, B[j].end)
                    )
                )

                if (A[i].end < B[j].end) {
                    i++
                } else {
                    j++
                }
            }
        }

        return Array<Interval>(result.size, { i -> result[i] })
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    val A = arrayOf(
        Interval(0, 2),
        Interval(5, 10),
        Interval(13, 23),
        Interval(24, 25)
    )
    val B = arrayOf(
        Interval(1, 5),
        Interval(8, 12),
        Interval(15, 24),
        Interval(25, 26)
    )

    val expected = arrayOf(
        Interval(1, 2),
        Interval(5, 5),
        Interval(8, 10),
        Interval(15, 23),
        Interval(24, 24),
        Interval(25, 25)
    )
    val result = solution.intervalIntersection(A, B)

    assert(expected contentEquals result)
}
