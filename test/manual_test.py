import random
import sys

sys.path.append("../textfy")

from textfy import send_msg


def test():
    loss, acc = random.random(), random.random() * 100
    print("loss:", loss)
    print("acc:", acc)

    send_msg(f"loss: {loss:.4f} | acc: {acc:.4f}")


if __name__ == "__main__":
    test()
