package leetcode

class TreeNode(var `val`: Int = 0) {
    var left: TreeNode? = null
    var right: TreeNode? = null
}

class Solution {
    fun maxPathSum(root: TreeNode?): Int {
        val (_, result) = _maxPathSum(root)
        return result
    }

    fun _maxPathSum(root: TreeNode?): Pair<Int, Int> {
        if (root == null) {
            return Pair(0, Int.MIN_VALUE)
        } else {
            val (leftMaxPathSum, leftResult) = _maxPathSum(root.left)
            val (rightMaxPathSum, rightResult) = _maxPathSum(root.right)

            val maxPathSum = maxOf(
                maxOf(leftMaxPathSum, rightMaxPathSum) + root.`val`, 0)
            val result = maxOf(
                leftResult, leftMaxPathSum + root.`val` + rightMaxPathSum, rightResult)

            return Pair(maxPathSum, result)
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

    assert(6 == solution.maxPathSum(t0_0))

    val t1_0 = TreeNode(-10)
    val t1_1 = TreeNode(9)
    val t1_2 = TreeNode(20)
    val t1_3 = TreeNode(15)
    val t1_4 = TreeNode(7)
    t1_2.right = t1_4
    t1_2.left = t1_3
    t1_0.right = t1_2
    t1_0.left = t1_1

    assert(42 == solution.maxPathSum(t1_0))

    val t2_0 = TreeNode(-3)

    assert(-3 == solution.maxPathSum(t2_0))

    val t3_0 = TreeNode(5)
    val t3_1 = TreeNode(4)
    val t3_2 = TreeNode(8)
    val t3_3 = TreeNode(11)
    val t3_4 = TreeNode(13)
    val t3_5 = TreeNode(4)
    val t3_6 = TreeNode(7)
    val t3_7 = TreeNode(2)
    val t3_8 = TreeNode(1)
    t3_5.right = t3_8
    t3_3.right = t3_7
    t3_3.left = t3_6
    t3_2.right = t3_5
    t3_2.left = t3_4
    t3_1.left = t3_3
    t3_0.right = t3_2
    t3_0.left = t3_1

    assert(48 == solution.maxPathSum(t3_0))

    val t4_0 = TreeNode(2)
    val t4_1 = TreeNode(-1)
    t4_0.left = t4_1

    assert(2 == solution.maxPathSum(t4_0))
}
