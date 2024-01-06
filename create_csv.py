import pandas as pd
import numpy as np
import argparse


def create_sample_csv(file_name, num_rows, num_columns, range_start, range_end):
    data = {
        f'Column_{i}': np.random.randint(range_start, range_end, num_rows)
        for i in range(num_columns)
    }
    df = pd.DataFrame(data)

    df.to_csv(file_name, index=False)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--num_files', type=int, default=1)
    parser.add_argument('--num_rows', type=int, default=5)
    parser.add_argument('--num_columns', type=int, default=3)
    parser.add_argument('--range_start', type=int, default=1)
    parser.add_argument('--range_end', type=int, default=10)

    args = parser.parse_args()

    num_files = args.num_files
    num_rows = args.num_rows
    num_columns = args.num_columns
    range_start = args.range_start
    range_end = args.range_end

    for i in range(num_files):
        file_name = f"file_{i + 1}.csv"
        create_sample_csv(file_name, num_rows, num_columns, range_start, range_end)
        print(f"Created {file_name}")


if __name__ == "__main__":
    main()
