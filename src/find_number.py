from utils import find_number

def main():
    hash_value = input("请输入哈希值：")
    csv_path = input("请输入csv文件路径：")
    try:
        return find_number(hash_value, csv_path)
    except FileNotFoundError:
        return 'Not found csv file'
    except TypeError:
        return 'Not found hash value'
    
if __name__ == '__main__':
    main()