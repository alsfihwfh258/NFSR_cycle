#!/usr/bin/env python3
"""
NFSR Cycle Calculator - Test Script

This script demonstrates how to use the NFSRCycleCalculator class programmatically
without the interactive command-line interface.
"""

from nfsr_cycle_calculator import NFSRCycleCalculator, example_feedback_function, fibonacci_feedback
from example_feedback_functions import grain_feedback, trivium_feedback

def run_test(name, register_length, feedback_function):
    """Run a test with a specific feedback function and display the results."""
    print(f"\n===== Testing {name} with register length {register_length} =====")
    
    calculator = NFSRCycleCalculator(register_length, feedback_function)
    cycles = calculator.find_all_cycles()
    
    calculator.display_cycles(cycles)
    calculator.calculate_cycle_distribution(cycles)
    print(f"===== End of {name} test =====\n")
    
    return cycles


def create_custom_function(expression):
    """Create a custom feedback function from a string expression."""
    from nfsr_cycle_calculator import create_custom_feedback_function
    return create_custom_feedback_function(expression, 4)  # 4-bit register


def main():
    """Run a series of tests with different feedback functions."""
    print("NFSR Cycle Calculator - Test Script")
    print("==================================")
    
    # Test 1: Example nonlinear feedback function with 3-bit register
    run_test("Example nonlinear function", 3, example_feedback_function)
    
    # Test 2: Fibonacci LFSR (linear) with 4-bit register
    run_test("Fibonacci LFSR", 4, fibonacci_feedback)
    
    # Test 3: Grain stream cipher with 5-bit register
    run_test("Grain stream cipher", 5, grain_feedback)
    
    # Test 4: Trivium stream cipher with a 4-bit register
    run_test("Trivium stream cipher", 4, trivium_feedback)
    
    # Test 5: Custom function with 4-bit register
    custom_function = create_custom_function("x[0] ^ x[1] ^ (x[2] & x[3])")
    run_test("Custom function: x[0] ^ x[1] ^ (x[2] & x[3])", 4, custom_function)
    
    print("All tests completed.")


if __name__ == "__main__":
    main() 