# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

def get_desc_stats():
    pass


def general_get_desc(path: "str"):
    return pd.read_csv(path).describe()
