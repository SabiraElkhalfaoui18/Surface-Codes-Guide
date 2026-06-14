import stim
import pymatching
import numpy as np

def simulate_surface_code(
        distance,
        rounds,
        physical_error_rate,
        shots = 1000,
        basis = "Z"
):

    """
    Simulate a rotated surface code memory experiment.
    Returns the logical error rate.
    """

    circuit = stim.Circuit.generated(
        f"surface_code:rotated_memory_{basis.lower()}",
        distance=distance,
        rounds=rounds,
        after_clifford_depolarization=physical_error_rate,
        before_round_data_depolarization=physical_error_rate,
        before_measure_flip_probability=physical_error_rate,
        after_reset_flip_probability=physical_error_rate,
        )

    dem = circuit.detector_error_model(
        decompose_errors = True
    )

    matcher = pymatching.Matching.from_detector_error_model(
        dem
    )

    sampler = circuit.compile_detector_sampler()

    detection_events, observable_flips = sampler.sample(
        shots,
        separate_observables= True
    )

    predictions = matcher.decode_batch(
        detection_events
    )

    failures = np.any(
        predictions != observable_flips,
        axis = 1
    )

    logical_error_rate = failures.mean()

    return logical_error_rate