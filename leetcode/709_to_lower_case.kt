package leetcode

class Solution {
  fun toLowerCase(str: String): String {
    return str.toLowerCase();
  }
}

fun main(args: Array<String>) {
  val solution = Solution()

  assert("hello" == solution.toLowerCase("Hello"))
  assert("here" == solution.toLowerCase("here"))
  assert("lovely" == solution.toLowerCase("LOVELY"))
}
