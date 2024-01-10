from utils import generate_numbers_null, generate_numbers_test, generate_sha256_csv

prefixes = ['134', '135', '136', '137', '138', '139', '144', '147', '148', '150', '151', '152', '157', '158', '159', '172', '178', '182', '183', '184', '187', '188', '195', '197', '198', '130', '131', '132', '145', '155', '156', '166', '167', '171', '175', '176', '185', '186', '196', '133', '149', '153', '173', '177', '180', '181', '189', '190', '191', '193', '199', '192']

test = ['999']

def main():
    # generate_sha256(test, generate_numbers_test)
    generate_sha256_csv(prefixes, generate_numbers_null)
    # 一个号段大概生成 65.3G 的csv文件，生成时间大概在 30000 秒左右

if __name__ == '__main__':
    main()