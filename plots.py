import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("results.csv")


datasets = [
    "random",
    "medium_duplicates",
    "many_duplicates"
]


for dataset_name in datasets:

    plt.figure(figsize=(9,6))


    data = df[df["dataset"] == dataset_name]


    for tree in data["tree"].unique():

        tree_data = data[data["tree"] == tree]


        plt.plot(
            tree_data["size"],
            tree_data["time"],
            marker="o",
            label=tree
        )


    plt.xlabel("Number of elements")

    plt.ylabel("Insertion time (seconds)")


    plt.title(
        f"Insertion time comparison - {dataset_name}"
    )


    plt.yscale("log")

    plt.grid(True)

    plt.legend()


    # Salvataggio immagine per LaTeX
    plt.savefig(
        f"{dataset_name}_time.png",
        dpi=300,
        bbox_inches="tight"
    )


    plt.show()

    plt.close()