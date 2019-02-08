package leetcode

class Solution {
    val ROWS = arrayOf(
        setOf('Q', 'W', 'E', 'R', 'T', 'Y', 'I', 'U', 'O', 'P'),
        setOf('A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'),
        setOf('Z', 'X', 'C', 'V', 'B', 'N', 'M')
    )

    fun findWords(words: Array<String>): Array<String> {
        val result = mutableListOf<String>()

        for (word in words) {
            for (row in ROWS) {
                if (word.toUpperCase().all({ char -> row.contains(char) })) {
                    result.add(word)
                }
            }
        }

        return Array<String>(result.size, { i -> result[i] })
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    val words = arrayOf("Hello", "Alaska", "Dad", "Peace")

    val expected = arrayOf("Alaska", "Dad")
    val result = solution.findWords(words)

    assert(expected contentEquals result)
}
