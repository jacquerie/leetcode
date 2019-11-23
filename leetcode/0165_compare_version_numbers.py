# -*- coding: utf-8 -*-


class Solution(object):
    def versionStringToList(self, version):
        result = list(map(int, version.split('.')))
        while result and result[-1] == 0:
            result.pop()
        return result

    def compareVersion(self, version1, version2):
        version1_list = self.versionStringToList(version1)
        version2_list = self.versionStringToList(version2)

        if version1_list < version2_list:
            return -1
        elif version1_list > version2_list:
            return 1
        return 0


if __name__ == '__main__':
    solution = Solution()

    assert -1 == solution.compareVersion('0.1', '1.1')
    assert 1 == solution.compareVersion('1.0.1', '1')
    assert -1 == solution.compareVersion('7.5.2.4', '7.5.3')
    assert 0 == solution.compareVersion('1', '1.0')
