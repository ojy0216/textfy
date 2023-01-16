import random
import sys
from time import sleep

sys.path.append("../textfy")

from textfy import Textfy


@Textfy()
def test():
    sleep_time = random.randint(3, 6)

    sleep(sleep_time)

    loss, acc = random.random(), random.random() * 100
    print("sleep_time: ", sleep_time)
    print("loss: ", loss)
    print("acc:", acc)

    return {"loss": loss, "acc": acc}


if __name__ == "__main__":
    test()
