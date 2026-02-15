import matplotlib.pyplot as plt


def plot_gdp_paths(results_dict, shock_time=None):

    plt.figure()

    for label, results in results_dict.items():
        plt.plot(results["Y"], label=label)

    if shock_time is not None:
        plt.axvline(x=shock_time, linestyle='--')

    plt.title("GDP Paths Comparison")
    plt.xlabel("Time")
    plt.ylabel("Output (Y)")
    plt.legend()
    plt.show()

