# Binary Gap Solution

This repository contains a Python solution for the [Binary Gap](https://leetcode.com/problems/binary-gap/) problem on LeetCode.

## Problem Description

Given a positive integer `n`, find and return the longest distance between any two adjacent 1's in the binary representation of `n`. If there are no two adjacent 1's, return 0.

## Solution

The solution converts the integer to its binary representation, iterates through the binary string, and calculates the distances between adjacent 1s. The maximum distance is then returned.

## Time and Space Complexity

*   **Time Complexity:** O(log n)
*   **Space Complexity:** O(log n)

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-github-username/binary-gap-solution.git
    ```
2.  Navigate to the repository directory:
    ```bash
    cd binary-gap-solution
    ```
3.  Install the required dependencies:
    ```bash
    pip install pytest
    ```

## Running Tests

Run the unit tests using pytest:

```bash
pytest tests
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is open source and licensed under the MIT License. Contributions are welcome!

## References

*   [LeetCode Binary Gap Problem](https://leetcode.com/problems/binary-gap/)
