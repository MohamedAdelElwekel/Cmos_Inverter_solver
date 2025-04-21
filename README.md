# CMOS Inverter Solver (Version 2 - with Channel Length Modulation)
This Python script provides an enhanced simulation of the DC characteristics of a CMOS inverter circuit by incorporating the effect of channel length modulation (Lambda) in the MOSFET current equations. This leads to a more accurate representation of the inverter's behavior compared to Version 1.

## Key Improvements over Version 1
* **Channel Length Modulation:** The MOSFET current model now includes the channel length modulation parameter (LAMBDA) for both NMOS and PMOS transistors. This accounts for the dependence of the drain current on the drain-source voltage in the saturation region, resulting in more realistic simulation results, especially in the output voltage curve.

## Features
* **Parameter Input:** Prompts the user to enter the supply voltage (Vdd), bulk voltage (Vbulk), and the channel widths (W) and lengths (L) for both NMOS and PMOS transistors.
* **Advanced MOSFET Modeling:** Implements a more accurate MOSFET current model including triode, saturation regions, and channel length modulation.
* **Numerical Solution:** Utilizes the `fsolve` function from the `scipy.optimize` library to find the output voltage where the NMOS and PMOS drain currents are equal.
* **Visualization:** Generates plots of the Vin-Vout and Vin-Id characteristics using `matplotlib`.

## Getting Started
1.  **Prerequisites:**
    * Python 3.x
    * NumPy (`pip install numpy`)
    * Matplotlib (`pip install matplotlib`)
    * SciPy (`pip install scipy`)

2.  **Running the Script:**
    * Save the Python code as `Version_2.py`.
    * Open a terminal or command prompt.
    * Navigate to the directory where you saved the file.
    * Run the script using the command: `python Version_2.py`
    * The script will then prompt you to enter the required parameters.
    * After entering the parameters, the script will generate and display the plots.

## Input Parameters
The script will ask you to provide the following inputs:
* **Vdd (Supply Voltage):** The positive supply voltage for the CMOS inverter.
* **Vbulk (Bulk Voltage):** The voltage applied to the bulk terminals of the MOSFETs (you can usually enter 0 if not specified).
* **W (NMOS Channel Width):** The width of the NMOS transistor channel.
* **L (NMOS Channel Length):** The length of the NMOS transistor channel.
* **W (PMOS Channel Width):** The width of the PMOS transistor channel.
* **L (PMOS Channel Length):** The length of the PMOS transistor channel.
* **End value of Vin range (start is 0):** The maximum input voltage for the simulation.
* **Step:** The increment step for the input voltage range.

## Output
The script will display two plots:
1.  **Vin - ID Curve:** Shows the relationship between the input voltage (Vin) and the drain current (Id) of the NMOS transistor (now influenced by channel length modulation).
2.  **Vin - Vout Curve:** Shows the voltage transfer characteristic (VTC) of the CMOS inverter, simulated with greater accuracy due to the inclusion of channel length modulation.

## Notes
* This version incorporates channel length modulation for a more accurate simulation of real-world CMOS inverter behavior.
* The physical constants and default MOSFET parameters are defined within the script and can be modified if needed. The LAMBDA parameter for both NMOS and PMOS is included in their respective parameter dictionaries.

## Author
Mohamed Adel Elwekel
