import numpy as np
import astropy.units as u
import matplotlib.pyplot as plt
from astropy.coordinates import SkyCoord


def FOV_HAWC():
    RA = np.arange(0,360)
    Dec_UP = np.ones(len(RA))*64
    Dec_LO = np.ones(len(RA))*-26

    HAWC_UP = SkyCoord(ra = RA*u.degree, dec = Dec_UP*u.degree)
    HAWC_UP = HAWC_UP.galactic
    
    HAWC_LO = SkyCoord(ra = RA*u.degree, dec = Dec_LO*u.degree)
    HAWC_LO = HAWC_LO.galactic

    hRA_up = -HAWC_UP.l.wrap_at(180*u.deg).radian
    hDec_up = HAWC_UP.b.radian
    hRA_lo = -HAWC_LO.l.wrap_at(180*u.deg).radian
    hDec_lo = HAWC_LO.b.radian

    Source = SkyCoord.from_name("GW 170817")
    Source = Source.galactic 
    
    GWl = -Source.l.wrap_at(180*u.deg).radian
    GWb = Source.b.radian

    fig = plt.figure() #Genero el canvas de la grafica
    ax = fig.add_subplot(111, projection="mollweide", facecolor = "aliceblue") #Defino una subplot con proyeccion Hammer

    ax.plot(GWl, GWb, "ro")
    ax.plot(hRA_up, hDec_up, 'k--')
    ax.fill(hRA_up, hDec_up, color = "white")
    ax.plot(hRA_lo, hDec_lo, 'k--')
    ax.fill(hRA_lo, hDec_lo, color = "white")

    xlabel = [r'$150^{\circ}$',r'$120^{\circ}$',r'$90^{\circ}$',r'$60^{\circ}$',r'$30^{\circ}$',r'$0^{\circ}$',r'$330^{\circ}$',r'$300^{\circ}$',r'$270^{\circ}$',r'$240^{\circ}$',r'$210^{\circ}$']

    ylabel = [r'$-75^{\circ}$',r'$-60^{\circ}$',r'$-45^{\circ}$',r'$-30^{\circ}$',r'$-15^{\circ}$',r'$0^{\circ}$',r'$15^{\circ}$',r'$30^{\circ}$',r'$45^{\circ}$',r'$60^{\circ}$',r'$75^{\circ}$']

    ax.set_xticklabels(xlabel)
    plt.grid(True)
    plt.savefig("../Figures/HAWC_GW.pdf", format="pdf")



FOV_HAWC()
