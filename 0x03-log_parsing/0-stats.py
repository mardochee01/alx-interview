#!/usr/bin/python3
"""Write a script that reads
stdin line by line and computes metrics"""
import sys

if __name__ == '__main__':

    f_size, count = 0, 0
    code = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in code}

    def print_stats(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(f_size))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                f_size += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_stats(stats, f_size)
        print_stats(stats, f_size)
    except KeyboardInterrupt:
        print_stats(stats, f_size)
        raise
