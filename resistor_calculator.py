"""
Resistor color code calculator.
Lucas Lutes, Mitch LaRue, Bennett Etheridge
"""

def get_input(Rmin, Rmax):
    ''' Prompt user to enter desired resistance and tolerance'''
    while True:
        try:
            Rdes = float(input(f'Enter desired resistance from {Rmin} to {Rmax/1e9} G ohm (examples: 11000 or 1.1e4): '))
            if Rdes >= Rmin and Rdes <= Rmax:
                break
            else:
                print('Invalid resistance, out of range')
        except ValueError:
            print('Invalid resistance, must be a number')

    while True:
        try:
            tol = int(input('Enter desired tolerance of 5, 10, or 20 percent: '))
            if tol == 5 or tol == 10 or tol == 20:
                break
            else:
                print('Invalid tolerance, must be an integer 5, 10, or 20')
        except:
            print('Invalid tolerance, must be an integer 5, 10, or 20')
    return Rdes, tol

# Define min and max resistance values for user input, in ohms
Rmin = 0.1
Rmax = 70e9

Rdes, tol = get_input(Rmin, Rmax)
print(f'Finding closest nominal resistance value to {Rdes:g} ohm with tolerance {tol}%:')

# Define nominal resistance values for the given tolerance.
# Add 100 at the end of the list so that the rightmost tolerance band is included.
# All of them start with 10 and ends with 100
if tol == 5:
    Rnom = [10, 11, 12, 13, 15, 16, 18, 20, 22, 24, 27, 30, 33, 36, 39, 43, 47, 51, 56, 62, 68, 75, 82, 91, 100]
elif tol == 10:
    Rnom = [10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82, 100]
elif tol == 20:
    Rnom = [10, 15, 22, 33, 47, 68, 100]

## Assume we have 4 color bands: A B C tol. The ABC_color is indexed by an integer in this version. A and B are the first and second color bands. C is the multipler
ABC_color = {-2:'silver', -1:'gold', 0:'black', 1:'brown', 2:'red', 3:'orange',
    4:'yellow', 5:'green', 6:'blue', 7:'violet', 8:'grey', 9:'white'}
tol_color = {5:'gold', 10:'silver', 20:''}  # No color band for 20% tol

## Convert to Rdes = M x 10^C with 10 <= M < 100
C = 0
M = Rdes
if M >= 100:
    while M >= 100:
        M = M / 10
        C += 1
elif M < 10:
    while M < 10:
        M = M * 10
        C -= 1

## Find closest nominal value in terms of A B
for R in range(len(Rnom) - 1):
    R_low = Rnom[R]
    R_high = Rnom[R + 1]
    if R_low <= M <= R_high:
        Diff_low = abs(M - R_low)
        Diff_high = abs(M - R_high)
        if Diff_high > Diff_low:
            closest_Rnom = R_low
        else:
            closest_Rnom = R_high
        break

# Handle the edge case if the closest nominal value is 100
if closest_Rnom == 100:
    closest_Rnom = 10
    C += 1

# Get the A and B values with integer division and mod operations
A = int(closest_Rnom // 10)
B = int(closest_Rnom % 10)

# Rclosest = AB*10**C  # Closest nominal resistance in ohms
Rclosest = closest_Rnom * (10 ** C)

# Find the % error between the desired and nominal resistances
# Percent Error = |R_actual − R_nominal| / R_nominal  × 100% 
# R_actual=Rdes, R_nominal=Rcandidate
Percent_Error = (abs(Rdes - Rclosest) / Rclosest) * 100

# print(f'Error between desired and nominal resistance values = {percent_error:.2f}%') also warning
print(f'Error between desired and nominal resistance values = {Percent_Error:.2f}%')

if Percent_Error > tol:
    print('Warning: The error between desired and nominal resistance exceeds the tolerance!')

# Get colors and print color code
print(f'Color code for {Rclosest:.1e} ohm with {tol}% tolerance is "{ABC_color[A]} {ABC_color[B]} {ABC_color[C]} {tol_color[tol]}"')
