from utils import get_sha256

def main():
    string = input("请输入字符串：")
    hash_value = get_sha256(string)
    print(f'{string} 的sha256值为：{hash_value}')

if __name__ == '__main__':
    main()