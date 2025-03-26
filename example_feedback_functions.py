"""
Example NFSR Feedback Functions

This file contains example feedback functions that can be used with the NFSR Cycle Calculator.
Each function takes a list of bits (the current register state) and returns a single bit.

Usage:
    from example_feedback_functions import functions
    function_name = list(functions.keys())[0]  # Get first function name
    feedback_function = functions[function_name]
    
    # Or import specific functions directly:
    from example_feedback_functions import grain_feedback
"""

from typing import List, Dict, Callable


def grain_feedback(state: List[int]) -> int:
    """
    Simplified version of the feedback function used in Grain stream cipher.
    For a full implementation, the register would need to be much longer.
    
    This implements: x[0] ⊕ x[1] ⊕ x[3] ⊕ x[4] ⊕ (x[1] & x[2]) ⊕ (x[2] & x[3]) ⊕ (x[3] & x[4])
    """
    # Ensure the state is long enough for this function
    if len(state) < 5:
        raise ValueError("Grain feedback function requires at least 5 bits in the register")
    
    # Linear part
    linear = state[0] ^ state[1] ^ state[3] ^ state[4]
    # Nonlinear part
    nonlinear = (state[1] & state[2]) ^ (state[2] & state[3]) ^ (state[3] & state[4])
    
    return (linear ^ nonlinear) % 2


def trivium_feedback(state: List[int]) -> int:
    """
    Simplified version of one of the feedback functions used in Trivium stream cipher.
    For a full implementation, the register would need to be much longer.
    
    This implements: x[0] ⊕ x[2] ⊕ (x[1] & x[2])
    """
    if len(state) < 3:
        raise ValueError("Trivium feedback function requires at least 3 bits in the register")
    
    return (state[0] ^ state[2] ^ (state[1] & state[2])) % 2


def alternating_step_generator(state: List[int]) -> int:
    """
    Simplified version of the alternating step generator.
    
    This uses the first bit to control whether to use the second or third bit.
    """
    if len(state) < 3:
        raise ValueError("Alternating step generator requires at least 3 bits in the register")
    
    # If the first bit is 1, use the second bit, otherwise use the third bit
    return state[1] if state[0] == 1 else state[2]


def majority_function(state: List[int]) -> int:
    """
    Majority function - outputs the majority value among the input bits.
    For odd-length registers, this is well-defined.
    For even-length registers, ties are broken by returning 0.
    """
    ones_count = sum(state)
    majority = 1 if ones_count > len(state) // 2 else 0
    return majority


def threshold_function(state: List[int], threshold: float = 0.7) -> int:
    """
    Threshold function - outputs 1 if the proportion of 1s exceeds the threshold.
    """
    ones_count = sum(state)
    proportion = ones_count / len(state)
    return 1 if proportion >= threshold else 0


def threshold_with_feedback(state: List[int]) -> int:
    """
    A version of the threshold function where the threshold is 0.7.
    """
    return threshold_function(state, 0.7)


def even_parity(state: List[int]) -> int:
    """
    Even parity function - outputs 1 if there's an odd number of 1s in the input.
    This makes the total number of 1s (including the output) even.
    """
    return sum(state) % 2


def galois_lfsr(state: List[int]) -> int:
    """
    Galois LFSR feedback function for a maximum-length sequence.
    This implementation is for specific register lengths with known tap positions.
    
    The tap positions are chosen to create maximum-length sequences for common register lengths.
    """
    length = len(state)
    
    # Tap positions for maximum-length LFSRs of various sizes
    taps = {
        2: [0, 1],
        3: [0, 1],
        4: [0, 1],
        5: [0, 2],
        6: [0, 1],
        7: [0, 1],
        8: [0, 2, 3, 4],
        9: [0, 4],
        10: [0, 3],
        11: [0, 2],
        15: [0, 1],
        16: [0, 1, 3, 12],
        17: [0, 3],
        18: [0, 7],
        19: [0, 1, 4, 18],
        20: [0, 3],
        21: [0, 2],
        22: [0, 1],
        23: [0, 5],
        24: [0, 1, 3, 4],
        25: [0, 3],
        28: [0, 3],
        29: [0, 2],
        30: [0, 1, 4, 6],
        31: [0, 3],
        32: [0, 1, 2, 22]
    }
    
    if length not in taps:
        raise ValueError(f"No tap positions defined for register length {length}")
    
    result = 0
    for tap in taps[length]:
        result ^= state[tap]
    
    return result


# Dictionary of all available functions
functions: Dict[str, Callable[[List[int]], int]] = {
    "Grain Stream Cipher": grain_feedback,
    "Trivium Stream Cipher": trivium_feedback,
    "Alternating Step Generator": alternating_step_generator,
    "Majority Function": majority_function,
    "Threshold (70%)": threshold_with_feedback,
    "Even Parity": even_parity,
    "Galois LFSR": galois_lfsr
} 