package leetcode

class Solution {
    fun sumEvenAfterQueries(A: IntArray, queries: Array<IntArray>): IntArray {
        val result = IntArray(queries.size)

        var sumEven = 0
        for (el in A) {
            if (el % 2 == 0) {
                sumEven += el
            }
        }

        for ((i, query) in queries.withIndex()) {
            val (`val`, j) = query

            A[j] += `val`
            if (A[j] % 2 == 0 && `val` % 2 == 0) {
                sumEven += `val`
            } else if (A[j] % 2 == 0 && `val` % 2 != 0) {
                sumEven += A[j]
            } else if (A[j] % 2 != 0 && `val` % 2 != 0) {
                sumEven -= A[j] - `val`
            }

            result[i] = sumEven
        }

        return result
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    val A = intArrayOf(1, 2, 3, 4)
    val queries = arrayOf(
        intArrayOf(1, 0),
        intArrayOf(-3, 1),
        intArrayOf(-4, 0),
        intArrayOf(2, 3)
    )

    val expected = intArrayOf(8, 6, 2, 4)
    val result = solution.sumEvenAfterQueries(A, queries)

    assert(expected contentEquals result)
}
