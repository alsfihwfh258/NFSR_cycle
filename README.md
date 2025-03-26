# NFSR Cycle Calculator

A Python program that calculates all cycles generated by a Nonlinear Feedback Shift Register (NFSR).

## What is an NFSR?

A Nonlinear Feedback Shift Register (NFSR) is a sequence generator where the next bit is determined by a nonlinear function of the current state. Unlike Linear Feedback Shift Registers (LFSRs), the feedback function in an NFSR can include nonlinear operations like AND, OR, and other boolean functions.

NFSRs are commonly used in cryptography, random number generation, and stream ciphers due to their complex behavior and resistance to certain types of cryptanalysis.

## Features

- Calculate all cycles generated by an NFSR with a configurable register length
- Support for predefined feedback functions
- Custom feedback function input using Python syntax
- Detailed display of cycle structures and distributions
- Performance timing for calculations
- Save results to a file for further analysis
- Library of example feedback functions from real-world applications

## Requirements

- Python 3.6 or higher

## Usage

1. Run the program:

```
python nfsr_cycle_calculator.py
```

2. Enter the register length (recommendation: start with small values like 3-8 bits for quick results)

3. Choose a feedback function:
   - Predefined example: `x[0] ⊕ (x[1] AND x[2])`
   - Fibonacci LFSR: `x[0] ⊕ x[1]`
   - Custom feedback function
   - Various example functions from the library (Grain, Trivium, etc.)

4. If you choose a custom function, enter it using Python syntax:
   - Use `x[i]` to refer to the i-th bit of the register (0-indexed)
   - Use `^` for XOR, `&` for AND, `|` for OR, `~` for NOT
   - Example: `x[0] ^ (x[1] & x[2])`
   
5. Choose whether to save results to a file

## Example Feedback Functions

The program includes several predefined feedback functions inspired by real-world cryptographic applications:

- **Grain Stream Cipher**: A simplified version of the feedback function used in the Grain stream cipher
- **Trivium Stream Cipher**: Based on one of the feedback functions in the Trivium stream cipher
- **Alternating Step Generator**: A nonlinear construction that uses one bit to select between two others
- **Majority Function**: Outputs the majority value (0 or 1) among the input bits
- **Threshold Function**: Outputs 1 if the proportion of 1s exceeds a threshold (70%)
- **Even Parity**: Outputs 1 if there's an odd number of 1s in the input
- **Galois LFSR**: A maximum-length LFSR implementation with predefined tap positions

## Example Output

For a 3-bit register with feedback function `x[0] ^ (x[1] & x[2])`:

```
NFSR with register length 3
Found 2 unique cycles:

Cycles of length 1: 1
  Cycle 1:
    000

Cycles of length 7: 1
  Cycle 1:
    001
    010
    100
    011
    110
    111
    101

Cycle Distribution Statistics:
------------------------------
Length 1: 1 cycles (1 states)
Length 7: 1 cycles (7 states)
------------------------------
Total: 2 cycles (8 states out of 8 possible)

Calculation completed in 0.0010 seconds
```

## Understanding the Results

The program displays:
- All unique cycles found in the NFSR
- The length of each cycle
- The states within each cycle (represented as binary strings)
- Statistics on cycle distribution
- Total number of cycles and states
- Calculation time

## Saving Results

When prompted, you can choose to save the results to a file. The program provides detailed feedback during the saving process:
- Shows progress for each cycle length being written
- Indicates completion of each major section (header, cycles, statistics)
- Confirms successful file save with checkmarks (✓)

The saved file contains:
- All cycle information in a readable format
- Cycle distribution statistics
- Total number of cycles and states

Example of the save process output:
```
Saving cycle information to nfsr_cycles.txt...
Writing data for 3 different cycle lengths...
Writing header information... ✓
Writing cycles of length 1 (1 cycles)... ✓
Writing cycles of length 4 (2 cycles)... ✓
Writing cycles of length 7 (1 cycles)... ✓
Writing distribution statistics... ✓

File saved successfully to nfsr_cycles.txt ✓
```

## Performance Note

The number of possible states grows exponentially with register length. For registers larger than 20 bits, the calculation may take a very long time or exhaust available memory. Start with smaller register sizes to get familiar with the program.

## Extending the Program

The code is structured to allow easy extensions:
- Add more predefined feedback functions to the `example_feedback_functions.py` file
- Implement additional analysis methods
- Modify the display format for results

## Files

- `nfsr_cycle_calculator.py` - Main program
- `example_feedback_functions.py` - Library of example feedback functions
- `README.md` - This documentation
- `requirements.txt` - Empty, as no external dependencies are required 