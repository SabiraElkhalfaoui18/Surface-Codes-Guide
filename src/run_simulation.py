import pandas as pd

from surface_code import simulate_surface_code

DISTANCES = [3,5,7]
PHYSICAL_ERROR_RATES = [
    0.001,
    0.003,
    0.005,
]

SHOTS = 10000

results = []

for d in DISTANCES:
    for p in PHYSICAL_ERROR_RATES:

        ler = simulate_surface_code(
            distance = d,
            rounds = d,
            physical_error_rate=p,
            shots= SHOTS,

        )

        print(
            f"d={d}, p={p:.4f},"
            f"logical_error_rate={ler: .6f}"
        )

        results.append(
            {
                "distance": d,
                "physical_error_rate": p,
                "logical_error_rate": ler,
            }
        )
    
df = pd.DataFrame(results)

df.to_csv(
    "../results/logical_error_rates.csv",
    index = False
)

print("\nResults saved.")