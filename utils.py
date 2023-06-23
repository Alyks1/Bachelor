import matplotlib.pyplot as plt


def plot_accuracy(h, accType):
    plt.plot(h.history[accType])
    plt.plot(h.history["val_" + accType])
    plt.title("model accuracy")
    plt.ylabel("MAE")
    plt.xlabel("epoch")
    plt.legend(["train", "validation"], loc="upper left")
    plt.show()
