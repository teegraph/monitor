import requests
import psutil
import sys
import time
import argparse


def main(args):
    try:
        while True:
            time.sleep(10)
            utilize = psutil.cpu_percent(interval=None, percpu=False)
            print(utilize)
            r = requests.post("{}:{}/api/v1/data".format(args.host, args.port), data={"utilize": utilize})
            print(r)
    except KeyboardInterrupt:
        print("Interrupt")
        sys.exit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="Host must be specified", required=True)
    parser.add_argument("--port", default=8080, help="Port, default 8080")
    args = parser.parse_args()
    main(args)
