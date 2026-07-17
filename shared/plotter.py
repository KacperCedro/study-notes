import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import numpy.typing as npt

def plot_func(n_val: npt.NDArray = None, results_1: npt.NDArray = None, results_2: npt.NDArray = None, results_3: npt.NDArray = None, asymptote_1: float = None, asymptote_2: float = None, asymptote_3: float = None, label_1: str = None, label_2: str = None, label_3: str = None, label_a1: str = None, label_a2: str = None, label_a3: str = None,  size: int = 50, space: int = 10, line_width: int = 2):
    plt.figure(figsize=(16,9))

    if n_val is None:
        raise Exception("Check your n_values")
    try:
        if results_1 is not None and label_1 is not None:
            plt.plot(n_val, results_1, 'r-o', markevery=space, linewidth=line_width, label=label_1)
    except:
        print("Correct your input data: results_1, label_1")
    try:
        if results_2 is not None and label_2 is not None:
            plt.plot(n_val, results_2, '^-b', markevery=space, linewidth=line_width, label=label_2)
    except:
        print("Correct your input data: results_2, label_2")
    try:
        if results_3 is not None and label_3 is not None:
            plt.plot(n_val, results_3, '*-g',markevery=space, linewidth=line_width, label=label_3)
    except:
        print("Correct your input data: results_3, label_3")
    try:
        if asymptote_1 is not None and label_a1 is not None:
            plt.axhline(y=asymptote_1, color='black', linestyle='--', linewidth=line_width, label=label_a1)
    except:
        print("Correct your input data: asymptote, label_a")
    try:
        if asymptote_2 is not None and label_a2 is not None:
            plt.axhline(y=asymptote_2, color='black', linestyle='-.', linewidth=line_width, label=label_a2)
    except:
        print("Correct your input data: asymptote, label_a")
    try:
        if asymptote_3 is not None and label_a3 is not None:
            plt.axhline(y=asymptote_3, color='black', linestyle=':', linewidth=line_width, label=label_a3)
    except:
        print("Correct your input data: asymptote, label_a")
    
    plt.legend(loc='right', fontsize=25)
    plt.title(r"The graph of serieses", fontsize=30, pad= 20)
    plt.xlabel(r"$n$", fontsize=20)
    plt.ylabel("Values", fontsize=20)
    plt.grid(True, linestyle=':', alpha=0.7)

    plt.show()

