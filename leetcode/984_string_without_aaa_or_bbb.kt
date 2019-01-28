package leetcode

class Solution {
  fun strWithout3a3b(A: Int, B: Int): String {
    val result = StringBuilder()

    if (A >= 2 * B) {
      repeat(B) { result.append("aab") }
      repeat(A - 2 * B) { result.append("a") }
    } else if (A >= B) {
      repeat(A - B) { result.append("aab") }
      repeat(2 * B - A) { result.append("ab") }
    } else if (B >= 2 * A) {
      repeat(A) { result.append("bba") }
      repeat(B - 2 * A) { result.append("b") }
    } else {
      repeat(B - A) { result.append("bba") }
      repeat(2 * A - B) { result.append("ab") }
    }

    return result.toString()
  }
}

fun main(args: Array<String>) {
  val solution = Solution()

  assert("bba" == solution.strWithout3a3b(1, 2))
  assert("aabaa" == solution.strWithout3a3b(4, 1))
}
