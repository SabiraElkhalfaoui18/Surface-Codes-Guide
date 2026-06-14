# Beginner Guide to Surface Codes

## 1. What problem do surface codes solve?

Quantum computers are very sensitive to noise. Physical qubits can suffer from bit-flip errors, phase-flip errors, measurement errors, and gate errors.

A surface code protects quantum information by encoding one logical qubit into many physical qubits.

## 2. Physical qubits vs logical qubits

A physical qubit is a real noisy qubit.

A logical qubit is an error-protected qubit built from many physical qubits.

The purpose of quantum error correction is to keep the logical qubit correct even when some physical qubits fail.

## 3. What is a stabilizer?

A stabilizer is a measurement used to check whether an error has happened.

Surface codes use two main types of stabilizers:

* X stabilizers detect Z-type errors
* Z stabilizers detect X-type errors

The results of stabilizer measurements are called syndromes.

## 4. What is code distance?

The code distance, usually written as `d`, measures how many physical errors are needed to cause a logical error.

Larger distance means better protection, but it requires more qubits.

For example:

```text
d = 3  small code, less protection
d = 5  medium code, better protection
d = 7  larger code, even better protection
```

## 5. What does Stim do?

Stim is a fast stabilizer-circuit simulator. It can generate surface-code circuits, add noise, and sample measurement results.

Example:

```python
import stim

circuit = stim.Circuit.generated(
    "surface_code:rotated_memory_Z",
    distance=3,
    rounds=3,
    after_clifford_depolarization=0.001,
)
```

## 6. What does a decoder do?

The decoder receives syndrome data and guesses which errors happened.

In this project, PyMatching is used as the decoder.

The workflow is:

```text
Surface-code circuit
        ↓
Noise creates errors
        ↓
Stabilizers detect changes
        ↓
Decoder predicts correction
        ↓
Check whether logical error happened
```

## 7. What is logical error rate?

The logical error rate is the probability that the encoded logical qubit fails.

A successful surface code should show lower logical error rate when the distance increases, especially below the error threshold.

## 8. Suggested first experiment

Run the same simulation for:

```python
distances = [3, 5, 7]
noise_rates = [0.001, 0.003, 0.005]
```

Then compare the logical error rates.

If the code works well, larger distances should usually give lower logical error rates at low physical noise.
