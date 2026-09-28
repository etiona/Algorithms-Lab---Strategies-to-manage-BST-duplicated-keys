import random


def random_dataset(n):

    return random.sample(
        range(n*10),
        n
    )

def duplicated_dataset(n):

    values=[]

    for _ in range(n):

        values.append(
            random.randint(0,n//2)
        )

    return values

def many_duplicates_dataset(n):

    values=[]

    for _ in range(n):

        values.append(
            random.randint(0,10)
        )

    return values
