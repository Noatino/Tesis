from astropy.coordinates import get_sun,SkyCoord, EarthLocation, AltAz
import numpy as np
import astropy.units as u
from astropy.time import Time
import matplotlib.pyplot as plt


CRAB = SkyCoord.from_name("Crab nebula")
GW = SkyCoord.from_name("GW 170817")
#print(GW)


HAWC = EarthLocation(lat=19*u.deg, lon=-97*u.deg, height=4100*u.m)


#plt.title('Transito de NGC 12775 e IC 310')


for day in range(57982, 57983,):
    t = Time(day, format='mjd')
    midnight = Time(day, format='mjd')
    delta_midnight = np.linspace(0, 24,100)*u.hour
    times = midnight + delta_midnight
    frame = AltAz(obstime=times, location=HAWC)
    
    


    ##############################################################################
    # Find the alt,az coordinates of NGC1275 at those same times:
    GWaltazs = GW.transform_to(frame)
    CRABaltazs = CRAB.transform_to(frame)

    ##############################################################################
    # Make a beautiful figure illustrating nighttime and the altitudes of NGC1275 and
    # the Sun over that time:
    T0 = (12.41*u.h).value
    timeGW = [times for times in delta_midnight.value if times > T0]
    indices = [list(delta_midnight.value).index(time) for time in timeGW]
    zenit =  GWaltazs.alt.value[indices]

    print(timeGW)
    print("-------")
    print(zenit)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.title("MJD 57982")
    #ax.plot(delta_midnight.value, CRABaltazs.alt.value,'k-', lw = 3, label = "Crab")
    ax.plot(timeGW, zenit,'-',color='red', lw = 2, label = "GW170817/GRB170814A")
    plt.arrow(T0,0,0,90)
    plt.arrow(T0+8.5,0,0,90, linestyle = "--", color="navy")
    ax.text(13,80, r"T$_{0}$",fontsize=18)
    plt.fill_between(delta_midnight.value,45,90, color = 'forestgreen', alpha=0.35)


ylabel = [r'$90^{\circ}$',r'$80^{\circ}$',r'$70^{\circ}$',r'$60^{\circ}$',r'$50^{\circ}$',r'$40^{\circ}$',r'$30^{\circ}$',r'$20^{\circ}$',r'$10^{\circ}$',r'$0^{\circ}$']
ax.set_yticklabels(ylabel)

plt.xlim(0,24)
plt.ylim(0,90)
plt.legend(loc=2)
plt.xlabel('hrs [UTC]')
plt.ylabel('Angulo Cenital [Deg]')
plt.grid(True)
#plt.show()
plt.savefig('../Figures/GW_Transit.pdf')
