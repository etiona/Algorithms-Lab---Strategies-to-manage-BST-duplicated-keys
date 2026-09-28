import pandas as pd
import time

from standard_bst import StandardBST
from flag_bst import FlagBST
from list_bst import ListBST
import sys

sys.setrecursionlimit(100000)

from datasets import (
    random_dataset,
    duplicated_dataset,
    many_duplicates_dataset
)


def measure_insert(tree_class, data):

    tree = tree_class()

    start = time.perf_counter()

    for value in data:
        tree.insert(value)

    end = time.perf_counter()

    return {
        "time": end - start,
        "height": tree.height(),
        "nodes": tree.node_count(),
        "elements": tree.element_count()
    }


# Alberi da confrontare

trees = [
    StandardBST,
    FlagBST,
    ListBST
]


# Dimensioni dei test

sizes = [
    1000,
    5000,
    10000,
    50000
]


# Dataset disponibili

datasets = {
    "random": random_dataset,
    "medium_duplicates": duplicated_dataset,
    "many_duplicates": many_duplicates_dataset
}



results = []


for dataset_name, dataset_generator in datasets.items():

    print("\nDataset:", dataset_name)


    for n in sizes:

        print(" Size:", n)

        dataset = dataset_generator(n)


        for tree in trees:

            metrics = measure_insert(
                tree,
                dataset
            )


            results.append({

                "tree": tree.__name__,

                "dataset": dataset_name,

                "size": n,

                "time": metrics["time"],

                "height": metrics["height"],

                "nodes": metrics["nodes"],

                "elements": metrics["elements"]

            })


            print(
                tree.__name__,
                "time:",
                metrics["time"]
            )



# Salvataggio risultati

df = pd.DataFrame(results)


df.to_csv(
    "results.csv",
    index=False
)


print("\nResults saved in results.csv")

print(df)