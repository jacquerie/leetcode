package leetcode

class Solution {
  fun checkPerfectNumber(num: Int): Boolean {
    return (
        num == 6 ||
        num == 28 ||
        num == 496 ||
        num == 8128 ||
        num == 33550336
    )
  }
}

fun main(args: Array<String>) {
  val solution = Solution()

  assert(solution.checkPerfectNumber(28))
}
