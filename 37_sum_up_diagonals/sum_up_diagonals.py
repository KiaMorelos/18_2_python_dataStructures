def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    summed  = 0

    for i in range(len(matrix)): #range goes from 0 to 3
        summed += matrix[i][i] #matrix m1 [0][0] is 1
        summed += matrix[i][-1 - i] #matrix m1 [0][-1] is 2, loop again until done
    
    return summed
