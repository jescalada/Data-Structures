def insertion_sort(A):
    """Sort list of comparable elements in non-decreasing order."""
    for k in range(1, len(A)):  # From 1 to n-1
        current = A[k]  # Current element to be inserted
        j = k  # Find correct index j for current
        while j > 0 and A[j - 1] > current:  # Element A[j-1] must be after current
            A[j] = A[j-1]
            j -= 1
        A[j] = current  # current is now in the right place
