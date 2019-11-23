# -*- coding: utf-8 -*-


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findMode(self, root):
        def _findMode(current, previous, count, max_count, result):
            if current is None:
                return previous, count, max_count

            previous, count, max_count = _findMode(
                current.left, previous, count, max_count, result)

            if previous is not None:
                if previous.val == current.val:
                    count += 1
                else:
                    count = 1
            if count > max_count:
                max_count = count
                result[:] = []
                result.append(current.val)
            elif count == max_count:
                result.append(current.val)

            return _findMode(current.right, current, count, max_count, result)

        result = []
        if root is None:
            return result

        _findMode(root, None, 1, 0, result)

        return result


if __name__ == '__main__':
    solution = Solution()

    t0_0 = TreeNode(1)
    t0_1 = TreeNode(2)
    t0_2 = TreeNode(2)
    t0_1.left = t0_2
    t0_0.right = t0_1

    assert [2] == solution.findMode(t0_0)
