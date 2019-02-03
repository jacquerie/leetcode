package leetcode

class Solution {
    fun reverseOnlyLetters(S: String): String {
        val result = S.toCharArray()

        var i = 0
        var j = S.length - 1
        while (i <= j) {
            if (!result[i].isLetter()) {
                i++
            } else if (!result[j].isLetter()) {
                j--
            } else {
                val tmp = result[j]
                result[j] = result[i]
                result[i] = tmp

                i++
                j--
            }
        }

        return result.joinToString("")
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    assert("dc-ba" == solution.reverseOnlyLetters("ab-cd"))
    assert("j-Ih-gfE-dCba" == solution.reverseOnlyLetters("a-bC-dEf-ghIj"))
    assert("Qedo1ct-eeLg=ntse-T!" == solution.reverseOnlyLetters("Test1ng-Leet=code-Q!"))
}
