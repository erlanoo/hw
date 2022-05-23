def get_list() -> list:
    return list(range(0, 100000000, 2))


class Solution:

    def find_target(self, list, target):
        left = 0
        right = len(list) - 1

        while left <= right:
            middle = int((left + right)) // 2
            guess = list[middle]

            if guess == target:
                return middle
            if guess > target:
                right = middle - 1
            else:
                left = middle + 1
        return [left, right]


print(Solution().find_target(get_list(), 150000))