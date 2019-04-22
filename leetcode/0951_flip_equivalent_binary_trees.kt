package leetcode

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun flipEquiv(root1: TreeNode?, root2: TreeNode?): Boolean {
        if (root1 == null && root2 == null) {
            return true
        } else if (root1 == null || root2 == null) {
            return false
        } else {
            return (
                root1.`val` == root2.`val` && (
                    (flipEquiv(root1.left, root2.left) && flipEquiv(root1.right, root2.right)) ||
                    (flipEquiv(root1.left, root2.right) && flipEquiv(root1.right, root2.left))
                )
            )
        }
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    val t0_0 = TreeNode(1)
    val t0_1 = TreeNode(2)
    val t0_2 = TreeNode(3)
    val t0_3 = TreeNode(4)
    val t0_4 = TreeNode(5)
    val t0_5 = TreeNode(6)
    val t0_6 = TreeNode(7)
    val t0_7 = TreeNode(8)
    t0_4.right = t0_7
    t0_4.left = t0_6
    t0_2.left = t0_5
    t0_1.right = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    val t1_0 = TreeNode(1)
    val t1_1 = TreeNode(3)
    val t1_2 = TreeNode(2)
    val t1_3 = TreeNode(6)
    val t1_4 = TreeNode(4)
    val t1_5 = TreeNode(5)
    val t1_6 = TreeNode(8)
    val t1_7 = TreeNode(7)
    t1_5.right = t1_7
    t1_5.left = t1_6
    t1_2.right = t1_5
    t1_2.left = t1_4
    t1_1.right = t1_3
    t1_0.right = t1_2
    t1_0.left = t1_1

    assert(solution.flipEquiv(t0_0, t1_0))
}
