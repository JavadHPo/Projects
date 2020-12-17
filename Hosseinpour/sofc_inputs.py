# Inputs:

import numpy as np

save_tag = 'porosity_study'
i_ext = 10000  # External current (A/m2)

t_final = 100000

" Thermo-chemical inputs "
T = 300 #500 #298   # Simulation temperature, K
P_an_0 = 101325 #Pa
X_k_an_0 = np.array([0.97, 0.03])

" Microstructure and geometry "
eps_gas_GDL = 0.7 # Gas phase volume fraction in GDL

eps_solid_CL = 0.6 # Volume fraction of solids (Pt +C) in CL
eps_gas_CL = 0.28  # Volume fraction of gas in CL

# Exponent in the Bruggeman correlatin: tau_fac = eps^alpha
alpha_Brugg_GDL = -1
alpha_Brugg_CL = -0.5

Pt_surf_frac = 0.1 # Fraction of carbon surface covered by Pt in CL.

dy_GDL = 100e-6 # GDL thickness (m)
dy_CL = 20e-6   # CL thickness (m)

# Carbon particle diameter:
d_part_GDL = 5e-6 # m
d_part_CL = 100e-9 # m

" Transport properties"
D_k_g_an = np.array([5.48e-4, 6.13e-5]) #Mixture-averaged diffusion coeffs, m2/s
mu_g_an = 9.54e-6                       # Dynamic viscsity, Pa-s

" Initial electric potential values "
phi_an_0 = 0
phi_elyte_0 = 0.6
phi_ca_0 = 1.1

" Charge transfer inputs "
C_dl_an = 0.003 # F/m2
C_dl_ca = 0.2 # F/m2

i_o_an = 2.5e-3
i_o_ca = 1e-3

n_an = -2.
n_ca = 4

F = 96485
R = 8.3145

# Charge transfer stoichiometric coefficients:
# Must be in same order as X_k_an:
nu_k_an = np.array([-1., 0.])

beta_ca = 0.5
beta_an = 0.5

delta_Phi_eq_an = -0.61
delta_Phi_eq_ca = 0.55