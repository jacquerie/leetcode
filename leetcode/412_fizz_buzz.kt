package leetcode

class Solution {
    fun fizzBuzz(n: Int): Array<String> {
        val result = Array<String>(n, { _ -> "" })

        for (i in 1..n) {
            if (i % 15 == 0) {
                result[i - 1] = "FizzBuzz"
            } else if (i % 5 == 0) {
                result[i - 1] = "Buzz"
            } else if (i % 3 == 0) {
                result[i - 1] = "Fizz"
            } else {
                result[i - 1] = i.toString()
            }
        }

        return result
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    val expected = arrayOf(
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    )
    val result = solution.fizzBuzz(15)

    assert(expected contentEquals result)
}
