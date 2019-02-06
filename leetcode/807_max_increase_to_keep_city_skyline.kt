package leetcode

class Solution {
    fun maxIncreaseKeepingSkyline(grid: Array<IntArray>): Int {
        val row_max = IntArray(grid.size, { _ -> 0 })
        val col_max = IntArray(grid[0].size, { _ -> 0 })

        for (i in 0..grid.size - 1) {
            for (j in 0..grid[0].size - 1) {
                row_max[i] = maxOf(row_max[i], grid[i][j])
                col_max[j] = maxOf(col_max[j], grid[i][j])
            }
        }

        var result = 0

        for (i in 0..grid.size - 1) {
            for (j in 0..grid[0].size - 1) {
                val local_max = minOf(row_max[i], col_max[j])
                result += local_max - grid[i][j]
            }
        }

        return result
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    val grid = arrayOf(
        intArrayOf(3, 0, 8, 4),
        intArrayOf(2, 4, 5, 7),
        intArrayOf(9, 2, 6, 3),
        intArrayOf(0, 3, 1, 0)
    )

    assert(35 == solution.maxIncreaseKeepingSkyline(grid))
}
