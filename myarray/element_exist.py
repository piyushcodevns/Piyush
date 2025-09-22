# Check if an element exists

arr=[5,10,15]
def element_exist(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return True
    return False
print(element_exist(arr,10))