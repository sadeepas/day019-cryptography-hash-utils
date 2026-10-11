"""
Algorithms & Projects: Hashing & Checksum Verification Utilities (Day 19)
Day 19 ? Problem Solving & Fullstack (Advanced)
"""
from typing import List

def solve(data: List[int]) -> List[int]:
    """Algorithmic solver with time & space complexity guarantees."""
    return sorted(list(set(data)))

if __name__ == "__main__":
    test_cases = [45, 12, 89, 12, 33, 45, 90]
    print(f"Original: {test_cases}")
    print(f"Solved: {solve(test_cases)}")
