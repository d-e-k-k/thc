from table import Table
import os
import sys
import errno

def main():
    try:
        file_name = sys.argv[1]
        if os.path.exists(file_name):
            print(os.path.basename(file_name))
            table = Table(file_name)
            table.print_table_summary()
        else:
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), file_name)
    except IndexError:
        print("Usage: " + os.path.basename(__file__) + " <file_path>")

if __name__ == "__main__":
    main()