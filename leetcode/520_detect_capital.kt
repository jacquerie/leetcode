package leetcode

class Solution {
    fun detectCapitalUse(word: String): Boolean {
        if (word.all({ char -> char.isUpperCase() })) {
            return true
        } else if (word.all({ char -> char.isLowerCase() })) {
            return true
        } else if (word[0].isUpperCase() && word.substring(1).all({ char -> char.isLowerCase() })) {
            return true
        } else {
            return false
        }
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    assert(solution.detectCapitalUse("USA"))
    assert(solution.detectCapitalUse("leetcode"))
    assert(solution.detectCapitalUse("Google"))
    assert(!solution.detectCapitalUse("FlaG"))
}
