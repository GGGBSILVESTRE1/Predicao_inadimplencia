import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import numpy as np


def plot_target_by_decile(df, feature: str, target: str, name: str):

    decile_series = pd.qcut(df[feature], q=10)
    proportions = pd.crosstab(decile_series, df[target], normalize="index")

    mean_proportions = proportions[1].mean() * 100

    fig, ax = plt.subplots(figsize=(8, 6))

    x = np.arange(len(proportions.index))
    ax.bar(
        x, proportions[1], width=0.35, color="orange", label="Default", data=proportions
    )

    ax.axhline(
        y=proportions[1].mean(),
        color="red",
        linestyle="--",
        label=f"Average Default Rate ({mean_proportions:.2f}%)",
    )
    ax.set_xticks(x)
    ax.set_xticklabels(proportions.index.astype(str), rotation=45, ha="right")
    for i, v in enumerate(proportions[1]):
        ax.text(i, v + 0.001, f"{v:.1%}", ha="center", fontsize=9)
    ax.set_xlabel(f"{feature}")
    ax.set_ylabel("Proportion")
    ax.set_title(name)
    ax.yaxis.set_major_formatter(PercentFormatter(1))
    ax.legend(
        bbox_to_anchor=(1.05, 1),
        loc="upper left",
    )
    plt.tight_layout()
    plt.show()
