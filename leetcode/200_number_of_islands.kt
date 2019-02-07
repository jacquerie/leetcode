package leetcode

import java.util.Deque
import java.util.LinkedList

class Solution {
    fun numIslands(grid: Array<CharArray>): Int {
        var result = 0

        for (i in 0..grid.size - 1) {
            for (j in 0..grid[0].size - 1) {
                if (grid[i][j] == '1') {
                    deleteIsland(grid, i, j)
                    result++
                }
            }
        }

        return result
    }

    fun deleteIsland(grid: Array<CharArray>, i: Int, j: Int) {
        val stack: Deque<Pair<Int, Int>> = LinkedList()
        stack.addLast(Pair(i, j))

        while (stack.size > 0) {
            val (x, y) = stack.removeLast()

            grid[x][y] = '0'
            if (0 < x && grid[x - 1][y] == '1')
                stack.addLast(Pair(x - 1, y))
            if (0 < y && grid[x][y - 1] == '1')
                stack.addLast(Pair(x, y - 1))
            if (x < grid.size - 1 && grid[x + 1][y] == '1')
                stack.addLast(Pair(x + 1, y))
            if (y < grid[0].size - 1 && grid[x][y + 1] == '1')
                stack.addLast(Pair(x, y + 1))
        }
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    assert(1 == solution.numIslands(
        arrayOf(
            charArrayOf('1', '1', '1', '1', '0'),
            charArrayOf('1', '1', '0', '1', '0'),
            charArrayOf('1', '1', '0', '0', '0'),
            charArrayOf('0', '0', '0', '0', '0')
        )
    ))
    assert(3 == solution.numIslands(
        arrayOf(
            charArrayOf('1', '1', '0', '0', '0'),
            charArrayOf('1', '1', '0', '0', '0'),
            charArrayOf('0', '0', '1', '0', '0'),
            charArrayOf('0', '0', '0', '1', '1')
        )
    ))
}
