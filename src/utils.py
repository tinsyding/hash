import os
import hashlib
import csv
import time

# 十一位电话号码版本
def generate_numbers_null(prefix):
    for i in range(100000000, 1000000000):
        yield prefix + str(i)[1:]

# 加前缀0086版本
def generate_numbers_0086(prefix):
    for i in range(100000000, 1000000000):
        yield '0086' + prefix + str(i)[1:]
            
# 加前缀86版本
def generate_numbers_86(prefix):
    for i in range(100000000, 1000000000):
        yield '86' + prefix + str(i)[1:]
            
# 加前缀+86版本
def generate_numbers_plus86(prefix):
    for i in range(100000000, 1000000000):
        yield '+86' + prefix + str(i)[1:]

# 测试版本
def generate_numbers_test(prefix):
    for i in range(1000, 10000):
        yield prefix + str(i)[1:]
        
# 计算哈希值(sha256)
def get_sha256(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

# 计算哈希值(md5)
def get_md5(string):
    return hashlib.md5(string.encode('utf-8')).hexdigest()

# 查找原数值
def find_number(hash_value, csv_path):
    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[1] == hash_value:
                return row[0]
    return 'Not found'

# 生成csv文件
def generate_sha256_csv(prefix_list, tel_version):
    start_time = time.time()
    header = ['Number', 'sha256']

    for prefix in prefix_list:
        csv_folder = 'csv'
        if not os.path.exists(csv_folder):
            os.makedirs(csv_folder)

        csv_file_path = os.path.join(csv_folder, f'{prefix}.csv')

        with open(csv_file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(header)

            for number in tel_version(prefix):
                hash_value = get_sha256(number)
                csv_writer.writerow([number, hash_value])
                print(f'{number} {hash_value}')

        file_size = os.path.getsize(csv_file_path)
        print(f'{csv_file_path} 文件大小: {file_size / (1024 * 1024):.2f} MB')

    end_time = time.time()
    total_time = end_time - start_time
    print(f'完成，共耗时 {total_time:.2f} 秒')