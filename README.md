# Resistor Color Code Calculator

## Description
A Python tool that calculates the closest E-series nominal resistance, computes percent error for standard tolerance, and outputs 4-band color codes for values from 0.1Ω to 70GΩ.

## Features
* **Wide Input Range:** Handles the user inputs for the wanted resistance ranging from 0.1 Ohm to 70 GigaOhm.
* **Tolerance Selection:** Supports calculations from standard 5%, 10%, and 20% tolerances.
* **E-Series Matching:** Automatically converts the target resistance to a base value M (10 <= M < 100) and multiplier C, then finds the closest standard nominal value (Rnom) from E-series lists.
* **Color Code Extraction:** Isolates the A and Bg digits to output the correct 4-band color sequence.
* **Error Checking:** Calculates the final percent error and outputs a warning if the calculated error exceeds the user's chosen tolerance.

## Documentation
* System Block Diagram
* Logic Flowchart
* Project Growth and Reflection

## Usage
Run the script in your terminal using Python. Foillow the given prompts to enter your desired resitance and tolerance values. 
```bash
python resistor_calculator.py
