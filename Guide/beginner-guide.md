# Beginner Guide to Surface Codes

## 1. What problem do surface codes solve?

Quantum computers are very sensitive to noise. Physical qubits can suffer from:

* Bit-flip errors
* Phase-flip errors
* Combined bit-and-phase-flip errors
* Measurement errors
* Gate errors

A surface code protects quantum information by encoding one logical qubit into many physical qubits.

The goal is to detect and correct errors before they corrupt the logical information.

---

## 2. Physical qubits vs logical qubits

A physical qubit is a real qubit implemented in hardware.

Examples:

* Superconducting qubits
* Trapped ions
* Neutral atoms

Physical qubits are noisy and error-prone.

A logical qubit is an error-protected qubit built from many physical qubits.

The purpose of quantum error correction is to preserve the logical qubit even when some physical qubits fail.

```text
Logical Qubit
      ↓
Encoded into
      ↓
Many Physical Qubits
```

---

## 3. The Three Pauli Errors

Surface codes are designed to detect and correct Pauli errors.

### X Error (Bit Flip)

Changes:

```text
|0⟩ → |1⟩
|1⟩ → |0⟩
```

### Z Error (Phase Flip)

Changes the phase:

```text
|+⟩ → |−⟩
```

without changing the computational basis measurement result.

### Y Error

A Y error is a combination of X and Z:

```text
Y = iXZ
```

Therefore:

```text
Y error = X error + Z error
```

Surface codes do not usually decode Y errors separately. Instead, the decoder handles the X and Z components independently.

---

## 4. What is a stabilizer?

A stabilizer is a measurement used to detect errors without measuring the logical quantum information directly.

Surface codes use two main types of stabilizers:

### X Stabilizers

Detect Z-type errors.

### Z Stabilizers

Detect X-type errors.

The outcomes of stabilizer measurements are called syndromes.

```text
X stabilizer  → detects Z errors

Z stabilizer  → detects X errors
```

A Y error activates both types of stabilizers because it contains both X and Z components.

---

## 5. What is a syndrome?

A syndrome is the result of a stabilizer measurement.

A syndrome does not tell us exactly which qubit experienced an error.

Instead, it indicates where inconsistencies appear in the code.

```text
Error occurs
      ↓
Stabilizer changes
      ↓
Syndrome appears
      ↓
Decoder infers correction
```

---

## 6. What is code distance?

The code distance, usually written as `d`, measures how many physical errors are needed to create a logical error.

Larger distance means stronger protection but requires more physical qubits.

Examples:

```text
d = 3  small code
d = 5  medium code
d = 7  larger code
```

A larger code distance generally leads to a lower logical error rate.

---

## 7. What does Stim do?

Stim is a fast stabilizer-circuit simulator.

It can:

* Generate surface-code circuits
* Add realistic noise
* Simulate stabilizer measurements
* Generate detector events
* Produce detector error models

Example:

```python
import stim

circuit = stim.Circuit.generated(
    "surface_code:rotated_memory_z",
    distance=3,
    rounds=3,
    after_clifford_depolarization=0.001,
)
```

---

## 8. What are detector events?

Detector events are changes in syndrome measurements.

Instead of tracking every physical qubit directly, Stim tracks detector events.

```text
Physical Error
      ↓
Syndrome Change
      ↓
Detector Event
```

These detector events are what the decoder actually receives.

---

## 9. What does a decoder do?

The decoder receives detector events and tries to determine the most likely error pattern.

In this project, PyMatching is used as the decoder.

The workflow is:

```text
Surface-Code Circuit
        ↓
Noise Creates Errors
        ↓
Stabilizers Detect Changes
        ↓
Detector Events
        ↓
PyMatching Decoder
        ↓
Correction Prediction
        ↓
Check Logical Failure
```

---

## 10. What is logical error rate?

The logical error rate is the probability that the encoded logical qubit fails after decoding.

It is the most important performance metric in quantum error correction.

A successful surface code should show:

```text
Higher distance
        ↓
Lower logical error rate
```

especially when the physical error rate is below the threshold.

---

## 11. Suggested First Experiment

Run the simulation for:

```python
distances = [3, 5, 7]

noise_rates = [
    0.001,
    0.003,
    0.005,
]
```

Compare the logical error rates.

Expected behavior:

```text
Distance increases
        ↓
Logical error rate decreases
```

This demonstrates the fundamental principle of quantum error correction.

---

## 12. Key Concepts to Remember

Before studying advanced surface codes, make sure you understand:

* Physical qubits
* Logical qubits
* Pauli X, Y, Z errors
* Stabilizers
* Syndromes
* Detector events
* Code distance
* Decoding
* Logical error rate

These concepts form the foundation of modern fault-tolerant quantum computing.
