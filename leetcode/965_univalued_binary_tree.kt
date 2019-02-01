package leetcode

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun isUnivalTree(root: TreeNode?): Boolean {
        if (root == null) {
            return true
        } else {
            return _isUnivalTree(root, root.`val`)
        }
    }

    fun _isUnivalTree(root: TreeNode, `val`: Int): Boolean {
        var result = root.`val` == `val`

        val left = root.left
        if (left != null)
            result = result && _isUnivalTree(left, `val`)

        val right = root.right
        if (right != null)
            result = result && _isUnivalTree(right, `val`)

        return result
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    var t0_0 = TreeNode(1)
    var t0_1 = TreeNode(1)
    var t0_2 = TreeNode(1)
    var t0_3 = TreeNode(1)
    var t0_4 = TreeNode(1)
    var t0_5 = TreeNode(1)
    t0_2.right = t0_5
    t0_1.right = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert(solution.isUnivalTree(t0_0))

    var t1_0 = TreeNode(2)
    var t1_1 = TreeNode(2)
    var t1_2 = TreeNode(2)
    var t1_3 = TreeNode(5)
    var t1_4 = TreeNode(2)
    t1_1.right = t1_4
    t1_1.left = t1_3
    t1_0.right = t1_2
    t1_0.left = t1_1

    assert(!solution.isUnivalTree(t1_0))
}
