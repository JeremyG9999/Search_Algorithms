class Binary_Recursive:
    @staticmethod
    def recursive_search(arr, target):
        if not arr or target not in arr:
            return -1
        mid = len(arr) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return Binary_Recursive(arr[:mid], target)
        else:
            return mid + Binary_Recursive(arr[mid+1:], target)
    
    @staticmethod
    def main():
        arr = [1, 3, 4, 5, 7, 9, 11]
        target = 5
        index = Binary_Recursive.recursive_search(arr, target)
        print(f"\n{index}") 