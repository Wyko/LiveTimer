import time
from random import randint

from livetimer import RichTimer


def run():
    "Run a timer demo"
    with RichTimer().start as timer:
        for _ in range(100):
            with timer.cycle as cycle:
                time.sleep(randint(1, 8) * 0.001)
                cycle.log("Logpoint: 10-80ms")
                time.sleep(randint(1, 2) * 0.001)
                cycle.log("Logpoint: 10-20ms")
                time.sleep(0.1)
                cycle.log("Logpoint: 100ms")


if __name__ == "__main__":
    run()
