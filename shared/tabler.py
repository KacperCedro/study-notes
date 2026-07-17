import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import numpy.typing as npt
from IPython.display import Markdown

def draw_table(table_data: object = None, slice_rate: int = 5):
    if table_data is None:
        raise Exception("No tabl_data")
    if slice_rate < 1:
        raise Exception("Incorrect split_rate - must be above 1")
    df = pd.DataFrame(table_data)
    df_sliced = df.iloc[::slice_rate]
    return Markdown(df_sliced.to_markdown(index=False))
