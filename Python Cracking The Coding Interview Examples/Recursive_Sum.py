# Example of memory complexity
# This is be O(n) run-time and O(n) space
def recursive_summation(n: int) -> int:
    if n <= 0:
        return 0
    return n + recursive_summation(n - 1)


# examples
x: int = recursive_summation(3)  # 3 + 2 + 1 =  6
y: int = recursive_summation(10)  # 10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 55

# Concept: O(n) space complexity because each call
# adds to the stack, and in this case it's n times as
# it grows/scales with the number we submit
