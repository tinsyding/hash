import hashlib
import csv

# 计算哈希值
def get_sha256(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

# 查找原数值
def find_number(hash_value, csv_path):
    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[1] == hash_value:
                return row[0]
    return 'Not found'

def main():
    print(" 计算哈希值 or 查找原数值 ")
    print("1. 计算哈希值")
    print("2. 查找原数值")

    choice = input("请输入选项：")

    if choice == '1':
        string = input("请输入字符串：")
        print(f'{string} 的哈希值为：{get_sha256(string)}')
    elif choice == '2':
        hash_value = input("请输入哈希值：")
        csv_path = input("请输入csv文件路径：")
        print(f'{hash_value} 的原数值为：{find_number(hash_value, csv_path)}')
    else:
        print("输入有误")

if __name__ == '__main__':
    main()