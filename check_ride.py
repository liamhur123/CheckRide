# super cool check ride app

def pressure_alt():
    standard_press = 29.92
    current_press = float(input("\nPlease enter current pressure: "))
    airport_elav = int(input("\nPlease enter airport elevation: "))
    pressure_diff = round((standard_press - current_press), 3)
    pressure_solve = round(((pressure_diff * 1000) + airport_elav), 3)
    print('\nPressure altitude calculation:')
    print(f'\n{standard_press}'
          f'\n- {current_press}'
          f'\n-------'
          f'\n{pressure_diff}'
          f'\nx 1000'
          f'\n ------'
          f'\n{pressure_diff * 1000}'
          f'\n+ {airport_elav}'
          f'\n ------'
          f'\n{pressure_solve}')
    print(f"\nPressure altitude = '{pressure_solve}ft'")


def shortfield_takeoff_dist():
    pressureAlt = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]
    temps = [0, 10, 20, 30, 40]
    sea_lvl_grnd = [640, 695, 755, 810, 875]
    one_thousand_ft_grnd = [705, 765, 825, 890, 960]
    two_thousand_ft_grnd = [775, 840, 910, 980, 1055]
    sea_lvl_obs = [1190, 1290, 1390, 1495, 1605]
    one_thousand_ft_obs = [1310, 1420, 1530, 1645, 1770]
    two_thousand_ft_obs = [1445, 1565, 1690, 1820, 1960]
    current_temp = int(input('\nPlease enter current temperature (Celcius): '))
    pressure = int(input("\nPlease enter Pressure Altitude: "))
    # for loop to go through pressureAlts and temps then calc final values
    for i in range(len(temps)):
        for j in range(len(pressureAlt)):
            if temps[i] < current_temp < temps[i+1] and pressureAlt[j] < pressure < pressureAlt[j + 1]:
                print(temps[i],temps[i+1],one_thousand_ft_grnd[j],one_thousand_ft_grnd[j+1], sea_lvl_grnd[i])
                print("{}°C:{} ".format(temps[i],low:=(((one_thousand_ft_grnd[j] - sea_lvl_grnd[i]) * (pressure / 1000)) + sea_lvl_grnd[i])))
                print("{}°C:{} ".format(temps[i+1],high:=(((one_thousand_ft_grnd[j+1] - sea_lvl_grnd[i+1]) * (pressure / 1000)) + sea_lvl_grnd[i+1])))
                print("{}°C:{} ".format(current_temp,(((high - low) * (current_temp / 100)) + low)))






def main():
    print("\nWelcome to nana's sexy check ride calculator. *moans*")
    shortfield_takeoff_dist()
    print("\nThanks hoe, bye.")


main()
