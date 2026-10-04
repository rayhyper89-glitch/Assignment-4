"""
Data Structures Showdown - Practice Problems
"""

# Problem 1: Duplicate Tracker
# A set is the best fit because it stores only unique product IDs and gives average O(1)
# membership checks and insertions. We scan the list once, so the overall expected runtime
# is O(n), with O(n) extra space in the worst case for the set.
def has_duplicates(product_ids):
    seen = set()

    for product_id in product_ids:
        if product_id in seen:
            return True
        seen.add(product_id)

    return False


# Problem 2: Order Manager
# A deque is appropriate because a queue needs fast insertion at the back and removal from
# the front. append() and popleft() are both O(1) operations, so each task operation is O(1).
from collections import deque


class TaskQueue:
    def __init__(self):
        self.tasks = deque()

    def add_task(self, task):
        self.tasks.append(task)

    def remove_oldest_task(self):
        if not self.tasks:
            return None
        return self.tasks.popleft()


# Problem 3: Unique Value Counter
# A set is ideal because it automatically keeps only unique values and provides average O(1)
# insertion and membership operations. add() is expected O(1), and get_unique_count() is O(1)
# because len() does not require scanning the set.
class UniqueTracker:
    def __init__(self):
        self.values = set()

    def add(self, value):
        self.values.add(value)

    def get_unique_count(self):
        return len(self.values)


# Basic tests
if __name__ == "__main__":
    print("Problem 1:")
    print(has_duplicates([10, 20, 30, 20, 40]))  # True
    print(has_duplicates([1, 2, 3, 4, 5]))       # False
    print(has_duplicates([]))                     # False

    print("\nProblem 2:")
    task_queue = TaskQueue()
    task_queue.add_task("Email follow-up")
    task_queue.add_task("Code review")
    print(task_queue.remove_oldest_task())        # Email follow-up
    print(task_queue.remove_oldest_task())        # Code review
    print(task_queue.remove_oldest_task())        # None

    print("\nProblem 3:")
    tracker = UniqueTracker()
    tracker.add(10)
    tracker.add(20)
    tracker.add(10)
    print(tracker.get_unique_count())             # 2
    tracker.add(30)
    print(tracker.get_unique_count())             # 3
