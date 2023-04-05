import os

initial_path = os.getcwd()
text_dz_3_name = 'text_dz_3'
file_name_1, file_name_2, file_name_3, file_name_4 = 'txt_1.txt', 'txt_2.txt', 'txt_3.txt', 'txt_4.txt'

full_path_1 = os.path.join(initial_path, text_dz_3_name, file_name_1)
full_path_2 = os.path.join(initial_path, text_dz_3_name, file_name_2)
full_path_3 = os.path.join(initial_path, text_dz_3_name, file_name_3)

full_path_4 = os.path.join(initial_path, text_dz_3_name, file_name_4)

counter_lines_txt_1 = 0
read_file_1 = []
with open(full_path_1, encoding='UTF-8') as file_1:
    read_file_1 = file_1.readlines()
    for line in read_file_1:
        counter_lines_txt_1 += 1



counter_lines_txt_2 = 0
read_file_2 = []
with open(full_path_2, encoding='UTF-8') as file_2:
    read_file_2 = file_2.readlines()
    for line in read_file_2:
        counter_lines_txt_2 += 1


counter_lines_txt_3 = 0
read_file_3 = []
with open(full_path_3, encoding='UTF-8') as file_3:
    read_file_3 = file_3.readlines()
    for line in read_file_3:
        counter_lines_txt_3 += 1


lines_sorted = sorted([counter_lines_txt_1, counter_lines_txt_2, counter_lines_txt_3])

with open(full_path_4, 'w', encoding='UTF-8') as file_4:
    if counter_lines_txt_2 == lines_sorted[0]:
        file_4.write(f"{file_name_2}\n {counter_lines_txt_2}\n{''.join(read_file_2)}\n")
    elif counter_lines_txt_1 == lines_sorted[0]:
        file_4.write(f"{file_name_1} \n {counter_lines_txt_1}\n{''.join(read_file_1)}\n")
    elif counter_lines_txt_3 == lines_sorted[0]:
        file_4.write(f"{file_name_3} \n {counter_lines_txt_3}\n{''.join(read_file_3)}\n")

    if counter_lines_txt_1 == lines_sorted[1]:
        file_4.write(f"{file_name_1} \n {counter_lines_txt_1}\n{''.join(read_file_1)}\n")
    elif counter_lines_txt_2 == lines_sorted[1]:
        file_4.write(f"{file_name_2}\n {counter_lines_txt_2}\n{''.join(read_file_2)}\n")
    elif counter_lines_txt_3 == lines_sorted[1]:
        file_4.write(f"{file_name_3} \n {counter_lines_txt_3}\n{''.join(read_file_3)}\n")

    if counter_lines_txt_1 == lines_sorted[2]:
        file_4.write(f"{file_name_1} \n {counter_lines_txt_1}\n{''.join(read_file_1)}\n")
    elif counter_lines_txt_2 == lines_sorted[2]:
        file_4.write(f"{file_name_2}\n {counter_lines_txt_2}\n{''.join(read_file_2)}\n")
    elif counter_lines_txt_3 == lines_sorted[2]:
        file_4.write(f"{file_name_3} \n {counter_lines_txt_3}\n{''.join(read_file_3)}\n")