package leetcode

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun maxDepth(root: TreeNode?): Int {
        if (root == null) {
            return 0
        } else {
            return 1 + maxOf(maxDepth(root.left), maxDepth(root.right))
        }
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    val t0_0 = TreeNode(3)
    val t0_1 = TreeNode(9)
    val t0_2 = TreeNode(20)
    val t0_3 = TreeNode(15)
    val t0_4 = TreeNode(7)
    t0_2.left = t0_3
    t0_2.right = t0_4
    t0_0.left = t0_1
    t0_0.right = t0_2

    assert(3 == solution.maxDepth(t0_0))
}
