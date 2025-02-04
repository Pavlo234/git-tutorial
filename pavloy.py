def repair_sequence(sequence: list[int]) -> list[int]:

    if sequence[-1] % 2 == 0:
        for i in range(len(sequence)):
            if sequence[i] % 2 != 0:
                p = sequence [i +1] - 2
                sequence[i] = p
                return sequence
    else:
        for i in range(len(sequence)):
            if sequence[i] % 2 != 0:
                p = sequence [i - 1] + 2
                sequence[i] = p
                return sequence
        return sequence
        



print(repair_sequence([2, 4, 6, 8, 10, 11]))



# [2, 4, 6, 8, 15, 12] [2, 4, 6, 8, 10, 12])


# test.assert_equals(repair_sequence([5, 4, 6, 8, 10]), [2, 4, 6, 8, 10])

# test.assert_equals(repair_sequence([2, 4, 6, 8, 11]), [2, 4, 6, 8, 10])