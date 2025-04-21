import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Physical constants
q = 1.602e-19
es = 11.7 * 8.854e-12
epsilon_ox = 0.34
i_n = 1.45e10
VT = 0.025875

# NMOS Parameters
def get_nmos_params():
    return {
        "K1": 0.5802748,
        "TOX": 4e-9,
        "VTH0": 0.3662648,
        "U0": 265.1889031,
        "VSAT": 1.017732e5,
        "CGDO": 8.06e-10,
        "CGSO": 8.06e-10,
        "CJ": 8.995609e-4,
        "CJSW": 2.393608e-10,
        "LAMBDA": 0.05   # Channel length modulation for NMOS
    }

# PMOS Parameters
def get_pmos_params():
    return {
        "K1": 0.5895473,
        "TOX": 4e-9,
        "VTH0": -0.3780033,
        "U0": 103.0478426,
        "VSAT": 1.645114e5,
        "CGDO": 6.52e-10,
        "CGSO": 6.52e-10,
        "CJ": 1.157423e-3,
        "CJSW": 1.902456e-10,
        "LAMBDA": 0.04   # Channel length modulation for PMOS
    }

# Helper functions
def calc_cox(TOX):
    return (epsilon_ox * 0.1) / TOX

def calc_k(U0, Cox, W, L):
    return U0 * Cox * (W / L)

def calc_phi_f(NB):
    return VT * np.log(NB / i_n)

def calc_nb(K, Cox):
    return ((K * Cox)**2 * 1e4) / (29 * es)

def calc_vth(VTH0, K1, phi_f, VSB):
    return VTH0 + K1 * (np.sqrt(2 * phi_f + VSB) - np.sqrt(2 * phi_f))

# MOSFET current with channel length modulation
def id_mosfet(K, Vgs, Vds, Vth, lambda_mod):
    if Vgs <= Vth:
        return 0
    elif Vds < (Vgs - Vth):
        return K * ((Vgs - Vth) * Vds - 0.5 * Vds**2) * (1 + lambda_mod * Vds)
    else:
        return 0.5 * K * (Vgs - Vth)**2 * (1 + lambda_mod * Vds)

# --- User Inputs ---
Vdd = float(input("Enter the supply voltage (Vdd): "))
Vbulk = float(input("Enter the value for Vbulk (V): ") or 0)
W_n = float(input("NMOS Channel Width (W): "))
L_n = float(input("NMOS Channel Length (L): "))
W_p = float(input("PMOS Channel Width (W): "))
L_p = float(input("PMOS Channel Length (L): "))
end = float(input("Enter end value of Vin range (start is 0): "))
step = 0.01
Vin_range = np.arange(0, end + step, step)

# Simulation function
def simulate_cmos(Vdd, Vbulk, W_n, L_n, W_p, L_p, Vin_range):
    nmos = get_nmos_params()
    pmos = get_pmos_params()

    Cox_n = calc_cox(nmos["TOX"])
    Cox_p = calc_cox(pmos["TOX"])

    K_n = calc_k(nmos["U0"], Cox_n, W_n, L_n)
    K_p = calc_k(pmos["U0"], Cox_p, W_p, L_p)

    NB_n = calc_nb(K_n, Cox_n)
    NB_p = calc_nb(K_p, Cox_p)

    phi_f_n = calc_phi_f(NB_n)
    phi_f_p = calc_phi_f(NB_p)

    lambda_n = nmos["LAMBDA"]
    lambda_p = pmos["LAMBDA"]

    Vout_list = []
    Id_list = []

    for Vin in Vin_range:
        VSB_n = Vbulk
        VSB_p = Vdd - Vbulk
        VSG_p = Vdd - Vin

        Vth_n = calc_vth(nmos["VTH0"], nmos["K1"], phi_f_n, VSB_n)
        Vth_p = calc_vth(pmos["VTH0"], pmos["K1"], phi_f_p, VSB_p)

        def error(Vout):
            Id_n = id_mosfet(K_n, Vin, Vout, Vth_n, lambda_n)
            Id_p = id_mosfet(K_p, VSG_p, Vdd - Vout, abs(Vth_p), lambda_p)
            return Id_n - Id_p

        Vout_sol = fsolve(error, Vdd / 2)[0]
        Vout_list.append(Vout_sol)

        Id = id_mosfet(K_n, Vin, Vout_sol, Vth_n, lambda_n)
        Id_list.append(Id)

    # Plotting
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(Vin_range, Id_list, label="I_D")
    plt.xlabel("Vin (V)")
    plt.ylabel("Drain Current (A)")
    plt.title("Vin - ID Curve")
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(Vin_range, Vout_list, label="Vout", color="orange")
    plt.xlabel("Vin (V)")
    plt.ylabel("Vout (V)")
    plt.title("Vin - Vout Curve")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

# Run the simulation
simulate_cmos(Vdd, Vbulk, W_n, L_n, W_p, L_p, Vin_range)