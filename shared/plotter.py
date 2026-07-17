import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import numpy.typing as npt

def plot_series(n_val: npt.NDArray = None, results_1: npt.NDArray = None, results_2: npt.NDArray = None, results_3: npt.NDArray = None, asymptote: float = None, label_1: str = None, label_2: str = None, label_3: str = None, label_a: str = None, size: int = 20):
    plt.figure(figsize=(16,9))

    if n_val is None:
        raise Exception("Check your n_values")
    try:
        if results_1 is not None and label_1 is not None:
            plt.scatter(n_val, results_1, color='red', marker='o', s=size, label=label_1)
    except:
        print("Correct your input data: results_1, label_1")
    try:
        if results_2 is not None and label_2 is not None:
            plt.scatter(n_val, results_2, color='blue', marker='^', s=size, label=label_2)
    except:
        print("Correct your input data: results_2, label_2")
    try:
        if results_3 is not None and label_3 is not None:
            plt.scatter(n_val, results_3, color='green', marker='*', s=size, label=label_3)
    except:
        print("Correct your input data: results_3, label_3")
    try:
        if asymptote is not None and label_a is not None:
            plt.axhline(y=asymptote, color='black', linestyle='--', label=label_a)
    except:
        print("Correct your input data: asymptote, label_a")
    
    plt.legend(loc='right', fontsize=25)
    plt.title(r"The graph of serieses", fontsize=30, pad= 20)
    plt.xlabel(r"$n$", fontsize=20)
    plt.ylabel("Values", fontsize=20)

    plt.show()

