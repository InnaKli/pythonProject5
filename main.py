from typing import List


def foo(nums: List[int]) -> List[int]:
    result = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if i != j:
                product *= nums[j]
        result.append(product)
        print(result)
