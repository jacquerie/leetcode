package leetcode

data class Email(val local_name: String, val domain_name: String)

class Solution {
    fun numUniqueEmails(emails: Array<String>): Int {
        val result = mutableSetOf<Email>()

        for (email in emails) {
            val (raw_local_name, domain_name) = email.split("@")
            val local_name = raw_local_name.replace(".", "").split("+")[0]
            result.add(Email(local_name, domain_name))
        }

        return result.size
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    assert(2 == solution.numUniqueEmails(arrayOf(
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com"
    )))
}
