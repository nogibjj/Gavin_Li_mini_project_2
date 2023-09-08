# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

def get_desc_stats():
    df = pd.read_csv("./dataset/train.csv")
    return df.describe(include="all")


def general_get_desc(path: "str") -> "pd.DataFrame":
    return pd.read_csv(path).describe()


def main():
    test = get_desc_stats()
    print(test.loc["count", "PassengerId"])

if __name__ == "__main__":
    main()
