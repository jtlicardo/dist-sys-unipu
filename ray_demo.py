import ray
import pandas as pd
import os
import time


@ray.remote
def process_csv(file_path):
    """Example of a function that takes a long time to run."""
    df = pd.read_csv(file_path)
    total_sum = 0
    for row in df.values:
        for value in row:
            total_sum += value
    return total_sum


def process_csv_without_ray(file_path):
    """Example of a function that takes a long time to run."""
    df = pd.read_csv(file_path)
    total_sum = 0
    for row in df.values:
        for value in row:
            total_sum += value
    return total_sum


def main():
    csv_files = [os.path.join('csv', file) for file in os.listdir('csv')]

    print(f"Found {len(csv_files)} CSV files")

    print("Processing CSV files with Ray...")
    start_time_ray = time.time()
    futures = [process_csv.remote(file) for file in csv_files]
    results_ray = ray.get(futures)
    end_time_ray = time.time()

    print("Processing CSV files without Ray...")
    start_time_seq = time.time()
    results_seq = [process_csv_without_ray(file) for file in csv_files]
    end_time_seq = time.time()

    print(f"Results with Ray: {len(results_ray)}")
    print(f"Results without Ray: {len(results_seq)}")

    print(f"\nTime taken with Ray: {end_time_ray - start_time_ray} seconds")
    print(f"Time taken without Ray: {end_time_seq - start_time_seq} seconds")


if __name__ == "__main__":
    print(f"Number of CPU cores: {os.cpu_count()}")
    ray.init(num_cpus=os.cpu_count())
    main()
