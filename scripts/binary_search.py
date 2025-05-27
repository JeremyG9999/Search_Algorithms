class Binary_Search:
    @staticmethod
    def search(arr, target):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    @staticmethod
    def main():
        arr = [1, 3, 4, 5, 7, 9, 11]
        target = 5
        index = Binary_Search.search(arr, target)
        print(f"\nBinary Search Index of {target}: {index}")
