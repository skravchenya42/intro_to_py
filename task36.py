operation = lambda i, j: i*j
def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        nums = []
        for j in range(1, num_columns + 1):
            num = operation(i, j)
            nums.append(num)
        print('\t'.join([str(x) for x in nums]))

print_operation_table(operation, num_rows=6, num_columns=6)
# 4 раза пересмотрела тот момент, где объясняете смысл этой задачи, но так и не поняла, что значит это: 
# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 

# в условии количество строк и столбцов задано прямо в самом первом предложении задачи, их по 6. 
