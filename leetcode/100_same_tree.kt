package leetcode

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun isSameTree(p: TreeNode?, q: TreeNode?): Boolean {
        if (p == null && q == null) {
            return true
        } else if (p == null || q == null) {
            return false
        } else {
            return (
                p.`val` == q.`val` &&
                isSameTree(p.left, q.left) &&
                isSameTree(p.right, q.right)
            )
        }
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    val t0_0 = TreeNode(1)
    val t0_1 = TreeNode(2)
    val t0_2 = TreeNode(3)
    t0_0.right = t0_2
    t0_0.left = t0_1

    val t1_0 = TreeNode(1)
    val t1_1 = TreeNode(2)
    val t1_2 = TreeNode(3)
    t1_0.right = t1_2
    t1_0.left = t1_1

    assert(solution.isSameTree(t0_0, t1_0))

    val t2_0 = TreeNode(1)
    val t2_1 = TreeNode(2)
    t2_0.left = t2_1

    val t3_0 = TreeNode(1)
    val t3_1 = TreeNode(2)
    t3_0.right = t3_1

    assert(!solution.isSameTree(t2_0, t3_0))

    val t4_0 = TreeNode(1)
    val t4_1 = TreeNode(2)
    val t4_2 = TreeNode(1)
    t4_0.right = t4_2
    t4_0.left = t4_1

    val t5_0 = TreeNode(1)
    val t5_1 = TreeNode(1)
    val t5_2 = TreeNode(2)
    t5_0.right = t5_2
    t5_0.left = t5_1

    assert(!solution.isSameTree(t4_0, t5_0))
}
