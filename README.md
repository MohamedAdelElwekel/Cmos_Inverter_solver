# CMOS Inverter Solver (Version 1)

This Python script simulates the DC characteristics of a CMOS inverter circuit by solving the relevant MOSFET equations. It allows users to input key parameters and visualizes the input-output voltage relationship (Vin-Vout curve) and the input voltage versus the NMOS drain current (Vin-Id curve).

## Features
* **Parameter Input:** Prompts the user to enter the supply voltage (Vdd), bulk voltage (Vbulk), and the channel widths (W) and lengths (L) for both NMOS and PMOS transistors.
* **MOSFET Modeling:** Implements a simplified MOSFET current model, considering both triode and saturation regions.
* **Numerical Solution:** Utilizes the `fsolve` function from the `scipy.optimize` library to find the output voltage where the NMOS and PMOS drain currents are equal.
* **Visualization:** Generates plots of the Vin-Vout and Vin-Id characteristics using `matplotlib`.

## Getting Started
1.  **Prerequisites:**
    * Python 3.x
    * NumPy (`pip install numpy`)
    * Matplotlib (`pip install matplotlib`)
    * SciPy (`pip install scipy`)

2.  **Running the Script:**
    * Save the Python code as `Version_1.py` (or any other `.py` file).
    * Open a terminal or command prompt.
    * Navigate to the directory where you saved the file using the `cd` command.
    * Run the script using the command: `python Version_1.py`
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
1.  **Vin - ID Curve:** Shows the relationship between the input voltage (Vin) and the drain current (Id) of the NMOS transistor.
2.  **Vin - Vout Curve:** Shows the voltage transfer characteristic (VTC) of the CMOS inverter.

## Notes
* This version uses a simplified MOSFET model and does not include second-order effects like channel length modulation.
* The physical constants and default MOSFET parameters are defined within the script and can be modified if needed.

## Author
Mohamed Adel Elwekel
