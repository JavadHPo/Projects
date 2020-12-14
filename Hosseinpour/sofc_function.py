"""
    This file runs and executes a youyr model, calculating the cell/device/system properties of interest as a function of time. 

    The code structure at this level is meant to be very simple, and delegates most functions to lower-level modules, which can be updated with new capabilties, over time.  The code:

        1 - Reads inputs and initializes the model
        
        2 - Calls the residual function and integrates over the user-defined    
            time span.
        3 - The simulation then returns the solution vector at the end of the 
            integration, which can be processed as needed to plot or analyze any quantities of interest.
"""

# Import necessary modules:
#from scipy.integrate import solve_ivp #integration function for ODE system.

# Either directly in this file, or in a separate file that you import, define: 
#   - A residual function called 'residual'
#   - An array 'time_span' which has [0, t_final] where t_final is the total 
#       length of time you want the model to simulate.
#   - An intial solution vector SV_0
#solution = solve_ivp(residual, time_span, SV_0,rtol=1e-4, atol=1e-6)

###########################################
# Copy-pasted from main model
#from scipy.integrate import solve_ivp
#import numpy as np
#from matplotlib import pyplot as plt
#from math import exp

#import importlib
import sofc_init
importlib.reload(sofc_init)
from sofc_init import pars
    
#from sofc_function import sofc_func

def sofc_func(i_ext, SV_0, pars, plot_flag):

    i_o_an = 2.5
    i_o_ca = 1
    n_an = 2
    n_ca = 4
    F = 96485
    beta_ca = 0.5
    beta_an = 0.5
    R = 8.3145
    T = 298

    delta_Phi_eq_an = 0.61
    delta_Phi_eq_ca = 0.55

    SV_0 = np.array([phi_elyte_0 - phi_an, phi_ca_0 - phi_elyte_0])
    time_span = np.array([0,100])

    # define a derivative. 
    def residual(t,SV):
        dSV_dt = np.zeros_like(SV)

        # Anode Interface:
        eta_an = SV[0] - delta_Phi_eq_an
        i_Far_an = pars.i_o_an*(exp(-n_an*F*beta_an*eta_an/R/T)
                          - exp(n_an*F*(1-beta_an)*eta_an/R/T))
        i_dl_an = i_ext - i_Far_an
        dSV_dt[0] = -i_dl_an/pars.C_dl_an

        # Cathode Interface:
        eta_ca = SV[1] - delta_Phi_eq_ca
        i_Far_ca = pars.i_o_ca*(exp(-n_ca*F*beta_ca*eta_ca/R/T)
                          - exp(n_ca*F*(1-beta_ca)*eta_ca/R/T))
        i_dl_ca = i_ext - i_Far_ca


        dSV_dt[1] = -i_dl_ca/pars.C_dl_ca
        return dSV_dt

    solution = solve_ivp(residual,time_span,SV_0,rtol=1e-4, atol=1e-6)

    V_elyte = solution.y[0,:]
    V_ca = V_elyte + solution.y[1,:]
    
        if plot_flag:
        plt.plot(solution.t,V_elyte)
        plt.plot(solution.t,V_ca)

        plt.xlabel('Time (s)',fontsize=14)
        plt.ylabel('Electric Potential (V)',fontsize=14)

        plt.legend([r'$\phi_{\rm elyte}$',r'$\phi_{\rm cathode}$'],fontsize=14,frameon=False)
   
    return solution.y[:,-1]

##############################