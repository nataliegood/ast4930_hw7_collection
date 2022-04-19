import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
import pandas as pd

data = open("sed.txt", "r")
lines = data.readlines()

for i in range(0,3):
    lines.pop(0)
wavelength = [float(x.split(",")[0]) for x in lines]
specific_luminosity = [float(x.split(",")[1]) for x in lines]

fig,axs = plt.subplots()
axs.plot(wavelength, specific_luminosity, color = "m")
axs.set_title('Spectral Energy Distribution')
axs.set_xscale('log')
axs.set(xlabel = "Wavelength in microns", ylabel = "Specific Luminosity in Lsun/ micron")
axs.set_yscale('log')

x_array = np.array(wavelength)
y_array = np.array(specific_luminosity)

data = np.column_stack([x_array, y_array])
df = pd.DataFrame(data = data)

wavmicros = (df[0] > 10)&(df[0] < 1000)
dfcorrect = df[wavmicros]

integral = np.trapz(dfcorrect[0], dfcorrect[1])
integral *= u.Lsun
integral_units = integral*(u.erg/u.s)

print(integral_units)

plt.savefig('good_natalie_hw7.png', dpi=300)