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
####Logic Flowchart

#### Part 1: User Input and E-Series Conversion
![Screenshot_11-3-2026_161750_docs google com](https://github.com/user-attachments/assets/d7117084-c539-47bc-ad8f-0f7e3e92eb44)
#### Part 2: Error Calculation and Color Output
![Screenshot_11-3-2026_16181_docs google com](https://github.com/user-attachments/assets/edf3deab-e72c-4e89-a6e8-b096686675c0)

### Project Growth and Reflection
This coding exercise tested not only our Python skills but also our error-catching and proofreading abilities. Initially, we struggled to tackle the entire project because the provided file comments were confusing. We worked together to break down each comment, tackling the requirements one step at a time since everything built off the previous step.

**Key Technical Challenges Overcome:**
* **Looping Nominal Resistances:** We conceptually struggled with finding which values `M` fell between. We solved this by assigning one value to `low`, setting the next iteration to `high`, and comparing `M` between them.
* **Calculating A and B:** Splitting our `M` value was difficult. Instead of one long equation, we learned to check the edge case (if `M` was 100) first, set the value to 10, and add 1 to `C`. From there, we found `A` using simple integer division and `B` using modulo.

**The Outcome:**
A major success was getting our code to work on the first run because we extensively proofread and checked our logic beforehand. Overall, our group gained valuable experience in problem-solving and breaking down complex technical ideas into manageable chunks.

## Usage
Run the script in your terminal using Python. Follow the given prompts to enter your desired resitance and tolerance values. 
```bash
python resistor_calculator.py
