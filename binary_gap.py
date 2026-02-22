def binaryGap(n):
    """Finds the longest binary gap in the binary representation of n.

    Args:
        n: A positive integer.

    Returns:
        The longest binary gap, or 0 if no adjacent 1s are found.
    """
    binary_string = bin(n)[2:]  # Convert to binary and remove '0b' prefix
    max_gap = 0
    current_gap = 0
    found_first_one = False

    for bit in binary_string:
        if bit == '1':
            if found_first_one:
                max_gap = max(max_gap, current_gap)
                current_gap = 0
            else:
                found_first_one = True
        elif found_first_one:
            current_gap += 1

    return max_gap
