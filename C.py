import math
 
 
def print_element_row(base_list, multiply, element_width):
    row_string = ''
 
    for base in base_list:
        row_string += f'{base} x {multiply} = {base * multiply}'.ljust(element_width)
 
    print(row_string)
 
 
def print_row(base_list, multiply_list, element_width):
    for number in multiply_list:
        print_element_row(base_list, number, element_width)
 
    print()
 
 
def get_row_base_list(base_list, row, column_count):
    row_base_list = []
 
    for column in range(0, column_count):
        index = (row * column_count) + column
 
        if index < len(base_list):
            row_base_list.append(base_list[index])
        else:
            break
 
    return row_base_list
 
 
def print_multiplication_tables(base_list, multiply_list, screen_width, element_width):
    column_count = math.floor(screen_width / element_width)
    total_row = math.ceil(len(base_list) / column_count)
    row_base_list = []
    
    for row in range(0, total_row):
        row_base_list = get_row_base_list(base_list, row, column_count)
        print_row(row_base_list, multiply_list, element_width)
        row_base_list.clear()
 
 
화면_가로_길이 = 80
각_단_가로_길이 = 12
단_수_목록 = list(range(2, 10))
곱할_수_목록 = list(range(1, 10))
 
print_multiplication_tables(단_수_목록, 곱할_수_목록, 화면_가로_길이, 각_단_가로_길이)