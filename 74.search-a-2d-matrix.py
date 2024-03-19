class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l < r:
            mid = (l + r) // 2
            if matrix[mid][0] == target:
                return True
            elif (
                matrix[mid][0] < target
                and mid + 1 < len(matrix)
                and matrix[mid + 1][0] > target
            ):
                l = r = mid
                break
            elif matrix[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1

        if l == r:
            i = l
            l, r = 0, len(matrix[i]) - 1
            while l <= r:
                mid = (l + r) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1

        return False
