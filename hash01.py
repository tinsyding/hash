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

# 生成csv文件
def generate_sha256(prefix_list, tel_version):
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
                hash_value = hashlib.sha256(number.encode('utf-8')).hexdigest()
                csv_writer.writerow([number, hash_value])

        file_size = os.path.getsize(csv_file_path)
        print(f'{csv_file_path} 文件大小: {file_size / (1024 * 1024):.2f} MB')

    end_time = time.time()
    total_time = end_time - start_time
    print(f'完成，共耗时 {total_time:.2f} 秒')



prefixes = ['134', '135', '136', '137', '138', '139', '144', '147', '148', '150', '151', '152', '157', '158', '159', '172', '178', '182', '183', '184', '187', '188', '195', '197', '198', '130', '131', '132', '145', '155', '156', '166', '167', '171', '175', '176', '185', '186', '196', '133', '149', '153', '173', '177', '180', '181', '189', '190', '191', '193', '199', '192']

test = ['000', '001']


def main():
    generate_sha256(test, generate_numbers_test)
    # generate_sha256(prefixes, generate_numbers_null)

if __name__ == '__main__':
    main()