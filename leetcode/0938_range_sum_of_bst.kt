package leetcode

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun rangeSumBST(root: TreeNode?, L: Int, R: Int): Int {
        if (root == null)
            return 0

        var result = 0

        if (L <= root.`val` && root.`val` <= R)
            result += root.`val`
        if (L <= root.`val`)
            result += rangeSumBST(root.left, L, R)
        if (root.`val` <= R)
            result += rangeSumBST(root.right, L, R)

        return result
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    val t0_0 = TreeNode(10)
    val t0_1 = TreeNode(5)
    val t0_2 = TreeNode(15)
    val t0_3 = TreeNode(3)
    val t0_4 = TreeNode(7)
    val t0_5 = TreeNode(18)
    t0_2.right = t0_5
    t0_1.right = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert(32 == solution.rangeSumBST(t0_0, 7, 15))

    val t1_0 = TreeNode(10)
    val t1_1 = TreeNode(5)
    val t1_2 = TreeNode(15)
    val t1_3 = TreeNode(3)
    val t1_4 = TreeNode(7)
    val t1_5 = TreeNode(13)
    val t1_6 = TreeNode(18)
    val t1_7 = TreeNode(1)
    val t1_8 = TreeNode(6)
    t1_4.left = t1_8
    t1_3.left = t1_7
    t1_2.right = t1_6
    t1_2.left = t1_5
    t1_1.right = t1_4
    t1_1.left = t1_3
    t1_0.right = t1_2
    t1_0.left = t1_1

    assert(23 == solution.rangeSumBST(t1_0, 6, 10))
}
