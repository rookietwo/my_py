import sys


def read_file(file_path):
    f = open(file_path, 'w+', encoding='utf-8')
    f.write("This is a sample text file.\n")
    f.close()


if __name__ == '__main__':
    read_file(sys.argv[1])
