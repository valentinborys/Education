nums = [1, 2, 2, 3, 4, 4, 5]

def num_update(nums):
    new_numb = set()
    for i in nums:
        new_numb.add(i)
    return new_numb

print(num_update(nums))