import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results.csv")

datasets = [
    "random",
    "medium_duplicates",
    "many_duplicates"
]


styles = {
    "StandardBST": {
        "marker": "o",
        "linestyle": "-",
        "linewidth": 2,
        "markersize": 8
    },
    "FlagBST": {
        "marker": "s",
        "linestyle": "--",
        "linewidth": 2,
        "markersize": 8
    },
    "ListBST": {
        "marker": "^",
        "linestyle": ":",
        "linewidth": 2,
        "markersize": 8
    }
}


# piccolo spostamento solo per rendere visibili curve identiche
offset = {
    "StandardBST": 0,
    "FlagBST": 0.15,
    "ListBST": -0.15
}


for dataset_name in datasets:

    plt.figure(figsize=(9, 6))

    data = df[df["dataset"] == dataset_name]


    for tree in ["StandardBST", "FlagBST", "ListBST"]:

        tree_data = data[data["tree"] == tree]


        plt.plot(
            tree_data["size"],
            tree_data["height"] + offset[tree],
            label=tree,
            **styles[tree]
        )


    plt.xlabel("Number of elements")
    plt.ylabel("Tree height")

    plt.title(
        f"Tree height comparison - {dataset_name}"
    )


    plt.grid(True)
    plt.legend()

    plt.xticks(
        sorted(data["size"].unique())
    )


    plt.savefig(
        f"{dataset_name}_height.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()

    plt.close()