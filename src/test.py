from utils import generate_numbers_test, generate_sha256_csv

test = ['888', '999']

def main():
    generate_sha256_csv(test, generate_numbers_test)

if __name__ == '__main__':
    main()