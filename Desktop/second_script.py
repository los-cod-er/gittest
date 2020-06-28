import sys

list = [[1,2,3] , [3,4,5] , [6,7,8]]

max_index = len(list)
output_file = sys.argv[1]
file_writer = open(output_file,'a')
for index_value in range(max_index):
    if index_value < (max_index - 1):
        file_writer.write(str(list[index_value]) + ',')
    else:
        file_writer.write(str(list[index_value]) + '\n')
file_writer.close()
print("out append to file")