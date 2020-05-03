import requests
import psutil
import sys
import time


def main():
    try:
        while True:
            time.sleep(10)
            utilize = psutil.cpu_percent(interval=None, percpu=False)
            print(utilize)
            r = requests.post("http://localhost:5000/api/v1/data", data={"utilize": utilize})
            print(r)
    except KeyboardInterrupt:
        print("Interrupt")
        sys.exit()


if __name__ == "__main__":
    main()
