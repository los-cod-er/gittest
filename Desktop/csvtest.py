import sys
#导入内置包

input_file = sys.argv[1]
output_file = sys.argv[2]
#使用argv函数告诉命令行输入与输出的文件

with open(input_file, 'r', newline='') as filereader:   #将input_file作为一个只读文件filereader打开
    with open(output_file, 'w', newline='') as filewriter:  #with函数可以在语句结束后自动关闭文件，不需要再用close（）
        header = filereader.readline()  #用readline方法读入文件第一行数据 #将其作为字符串并赋值给header变量
        header = header.strip()         #格式处理
        header_list = header.split(',')
        print(header_list)
        filewriter.write(','.join(map(str, header_list)) + '\n')
        for row in filereader:
            row = row.strip()
            row_list = row.split(',')
            print(row_list)
            filewriter.write(','.join(map(str, row_list)) + '\n')
            