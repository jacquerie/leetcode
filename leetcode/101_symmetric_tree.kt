package leetcode

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun isSymmetric(root: TreeNode?): Boolean {
        if (root == null) {
            return true
        } else {
            return _isSymmetric(root.left, root.right)
        }
    }

    fun _isSymmetric(left: TreeNode?, right: TreeNode?): Boolean {
        if (left == null || right == null) {
            return left == null && right == null
        } else {
            return (
                left.`val` == right.`val` &&
                _isSymmetric(left.left, right.right) &&
                _isSymmetric(left.right, right.left)
            )
        }
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    val t0_0 = TreeNode(1)
    val t0_1 = TreeNode(2)
    val t0_2 = TreeNode(2)
    val t0_3 = TreeNode(3)
    val t0_4 = TreeNode(4)
    val t0_5 = TreeNode(4)
    val t0_6 = TreeNode(3)
    t0_2.left = t0_5
    t0_2.right = t0_6
    t0_1.left = t0_3
    t0_1.right = t0_4
    t0_0.left = t0_1
    t0_0.right = t0_2

    assert(solution.isSymmetric(t0_0))

    val t1_0 = TreeNode(1)
    val t1_1 = TreeNode(2)
    val t1_2 = TreeNode(2)
    val t1_3 = TreeNode(3)
    val t1_4 = TreeNode(3)
    t1_2.right = t1_4
    t1_1.right = t1_3
    t1_0.left = t1_1
    t1_0.right = t1_2

    assert(!solution.isSymmetric(t1_0))
}
