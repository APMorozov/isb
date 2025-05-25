import matplotlib.pyplot as plt


def plot(results: list[list[int | float]]) -> None:
    """
    make plot
    :param results: list[count of cores; time]
    :return: None
    """

    cores = [item[0] for item in results]
    times = [item[1] for item in results]

    plt.figure(figsize=(10, 6))
    plt.plot(cores, times, 'bo-', label="lead time")

    plt.title("Execution time dependence on the number of cores")
    plt.xlabel("Number of cores")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    plt.xticks(cores)
    plt.legend()

    plt.show()
    plt.close()
