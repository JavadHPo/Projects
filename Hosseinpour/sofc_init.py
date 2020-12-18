""" Initialize SOFC model.
    
    Read in user inputs from 'sofc_inputs', then construct initial solution vector SV_0.  Create a class for all other needed parameters, called 'params.'
    
"""
from sofc_inputs import *
import numpy as np

#Adding equilibrium potential calculations

DeltaG_circ_an = g_circ_H2O - g_circ_H2 - g_circ_O2_m
delta_Phi_eq_an = -DeltaG_circ_an/(n_an*F) #-0.61

DeltaG_circ_ca = 2*g_circ_O2_m - g_circ_O2
delta_Phi_eq_ca = -DeltaG_circ_ca/(n_ca*F) #0.55

"============ INITIALIZE SOLUTION VECTOR ============"
C_k_an_CL_0 = P_an_0*X_k_an_0/R/T


# Construct initial solution vector
SV_0 = np.hstack((np.array([phi_an_0 - phi_elyte_0]), C_k_an_CL_0, C_k_an_CL_0,
    np.array([phi_ca_0 - phi_elyte_0])))

# Construct class containing all parameters.  Mostly we are just copying the 
#   variable names from the user inputs into the class structure:
class pars:
    time_span = np.array([0,t_final])

    T = T

    i_ext = i_ext

    # Anode
    delta_Phi_eq_an = delta_Phi_eq_an
    i_o_an = i_o_an
    n_an = n_an
    beta_an = beta_an

    C_dl_an = C_dl_an

    dy_GDL = dy_GDL
    dy_CL = dy_CL

    eps_g_dy_Inv_CL = 1/dy_CL/eps_gas_CL
    eps_g_dy_Inv_GDL = 1/dy_GDL/eps_gas_GDL

    eps_g_GDL = eps_gas_GDL
    eps_g_CL = eps_gas_CL
    n_Brugg_GDL = alpha_Brugg_GDL
    n_Brugg_CL = alpha_Brugg_CL

    nu_k_an = nu_k_an

    X_k_GDL = X_k_an_0

    D_k_g_an = D_k_g_an
    mu_g_an = mu_g_an

    # Pt surface area per unit geometric area:
    A_fac_Pt = 0.5*eps_solid_CL*3.*dy_CL*Pt_surf_frac/d_part_CL
    # Geometric area per unit double layer area:
    A_fac_dl = Pt_surf_frac/A_fac_Pt

    # Fraction of Carbon surface covered by Pt:
    f_Pt = Pt_surf_frac

    d_solid_GDL = d_part_GDL
    d_solid_CL = d_part_CL
    
    # Cathode
    delta_Phi_eq_ca = delta_Phi_eq_ca
    i_o_ca = i_o_ca
    n_ca = n_ca
    beta_ca = beta_ca

    C_dl_ca = C_dl_ca

# Create a 'pointer' class that specifies where in SV certain variables are 
#    stored:
class ptr:
    phi_dl_an = 0
    
    # C_k in anode GDL: starts just after phi_dl, is same size as X_k_an:
    C_k_an_GDL = np.arange(phi_dl_an+1, phi_dl_an+1+X_k_an_0.shape[0])
    
    # C_k in anode CL: starts just after GDL, is same size as X_k_an:
    C_k_an_CL = np.arange(C_k_an_GDL[-1]+1, C_k_an_GDL[-1]+1+X_k_an_0.shape[0])
    
    # phi_dl_ca: starts just after C_k_an_CL:
    phi_dl_ca = C_k_an_CL[-1] + 1