import sys
"""
import sys
input_file = sys.argv[1]

print("output #144:")
with open(input_file,'r',newline = '') as filereader:
    for row in filereader:
        print(row.strip())
"""

my_letter = ['a','b','c','d','e','f','g','h','i','j']
max_index = len(my_letter)
output_file = sys.argv[1]
file_writer = open(output_file,'w')
for index_value in range(len(my_letter)):
    if index_value < (max_index - 1):
        file_writer.write(my_letter[index_value] + '\t')
    else:
        file_writer.write(my_letter[index_value] + '\n')
file_writer.close()
print("output written to file")

my_number = [0,1,2,3,4,5,6,7,8,9]
max_index = len(my_number)
output_file = sys.argv[1]
file_writer = open(output_file,'a')
for index_value in range(max_index):
    if index_value < (max_index - 1):
        file_writer.write(str(my_number[index_value]) + ',')
    else:
        file_writer.write(str(my_number[index_value]) + '\n')
file_writer.close()
print("out append to file")