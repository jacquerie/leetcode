package leetcode

class TreeNode(var `val`: Int) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun searchBST(root: TreeNode?, `val`: Int): TreeNode? {
        if (root == null || root.`val` == `val`) {
            return root
        } else if (root.`val` > `val`) {
            return searchBST(root.left, `val`)
        } else {
            return searchBST(root.right, `val`)
        }
    }
}

fun main(args: Array<String>) {
    val solution = Solution()

    val t0_0 = TreeNode(4)
    val t0_1 = TreeNode(2)
    val t0_2 = TreeNode(7)
    val t0_3 = TreeNode(1)
    val t0_4 = TreeNode(3)
    t0_1.right = t0_4
    t0_1.left = t0_3
    t0_0.right = t0_2
    t0_0.left = t0_1

    assert(t0_1 === solution.searchBST(t0_0, 2))
}
