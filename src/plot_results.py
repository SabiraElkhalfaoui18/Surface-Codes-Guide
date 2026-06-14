import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "../results/logical_error_rates.csv"

)

for distance in sorted(
    df["distance"].unique()
):
    subset = df[
        df["distance"] == distance
    ]

    plt.plot(
        subset["physical_error_rate"],
        subset["logical_error_rate"],
        marker = "o",
        label=f"d={distance}"
    )

plt.xlabel(
    "Physical error rate"
)

plt.ylabel(
    "Logical error rate"
)

plt.title(
    "Surface Code Performane"
)

plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
   "../results/logical_error_rate.png" ,
   dpi=300
)

plt.show