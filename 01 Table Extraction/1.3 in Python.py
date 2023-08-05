import camelot

tables = camelot.read_pdf("/Users/sunyueqian/Desktop/Automation with Python/01 Table Extraction/foo.pdf",pages="1")

print(tables)

tables.export("/Users/sunyueqian/Desktop/Automation with Python/01 Table Extraction/foo.csv",f="csv",compress=False)
tables[0].to_csv("/Users/sunyueqian/Desktop/Automation with Python/01 Table Extraction/foo.csv")
#tables.export("/Users/sunyueqian/Desktop/Automation with Python/01 Table Extraction/foo.pdf",f="csv",compress=True): 这行代码将所有提取到的表格（存在tables列表中）输出到CSV文件中，并且将所有CSV文件压缩到一个zip文件中。这个zip文件被命名为foo.pdf并保存在指定的文件夹路径中。
#tables[0].to_csv("/Users/sunyueqian/Desktop/Automation with Python/01 Table Extraction/foo.pdf"): 这行代码将tables列表中的第一个表格（index为0）输出到CSV文件中。这个CSV文件被命名为foo.pdf并保存在指定的文件夹路径中。