import numpy as np



def calculate(numbers):
    # check if list has 9 elements
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    if len(numbers) >9:
        raise ValueError("List must contain only nine numbers.")  

    # change list to 3x3 array
    matrix = np.array(numbers).reshape(3, 3)

    # create a dictionary to hold the results
    calculations = {}

    # mean
    mean_rows = matrix.mean(axis=0).tolist()
    mean_cols = matrix.mean(axis=1).tolist()
    mean_all = matrix.mean()
    calculations['mean'] = [mean_rows, mean_cols, mean_all]

    # variance
    var_rows = matrix.var(axis=0).tolist()
    var_cols = matrix.var(axis=1).tolist()
    var_all = matrix.var()
    calculations['variance'] = [var_rows, var_cols, var_all]

    # standard deviation
    std_rows = matrix.std(axis=0).tolist()
    std_cols = matrix.std(axis=1).tolist()
    std_all = matrix.std()
    calculations['standard deviation'] = [std_rows, std_cols, std_all]

    # max
    max_rows = matrix.max(axis=0).tolist()
    max_cols = matrix.max(axis=1).tolist()
    max_all = matrix.max()
    calculations['max'] = [max_rows, max_cols, max_all]

    # min
    min_rows = matrix.min(axis=0).tolist()
    min_cols = matrix.min(axis=1).tolist()
    min_all = matrix.min()
    calculations['min'] = [min_rows, min_cols, min_all]

    # sum
    sum_rows = matrix.sum(axis=0).tolist()
    sum_cols = matrix.sum(axis=1).tolist()
    sum_all = matrix.sum()
    calculations['sum'] = [sum_rows, sum_cols, sum_all]

    return calculations




