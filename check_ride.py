# super cool check ride app
from tabulate import tabulate
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
        if temps[i] < current_temp < temps[i+1]:
            print("{}°C:{} ".format(temps[i],low:=(((one_thousand_ft_grnd[i] - sea_lvl_grnd[i]) * (pressure / 1000)) + sea_lvl_grnd[i])))
            print("{}°C:{} ".format(temps[i+1],high:=(((one_thousand_ft_grnd[i+1] - sea_lvl_grnd[i+1]) * (pressure / 1000)) + sea_lvl_grnd[i+1])))
            print("{}°C:{} ".format(current_temp,(((high - low) * (current_temp / 100)) + low)))
            middle = (((high - low) * (current_temp % 10)/10) + low)
            header = ["{}°C".format(temps[i]),"{}°C".format(current_temp), "{}°C".format(temps[i+1])]
            data = [[sea_lvl_grnd[i],(((sea_lvl_grnd[i+1] - sea_lvl_grnd[i]) * (current_temp % 10)/10) + sea_lvl_grnd[i]),sea_lvl_grnd[i+1]],
                    [low,middle,high],
                    [one_thousand_ft_grnd[i],(((one_thousand_ft_grnd[i+1] - one_thousand_ft_grnd[i]) * (current_temp % 10)/10) + one_thousand_ft_grnd[i]),one_thousand_ft_grnd[i+1]]
                    ]
            print("GROUND")
            print(tabulate(data,headers=header,tablefmt="grid"))
            print("{}°C:{} ".format(temps[i],low_obs:=(((one_thousand_ft_obs[i] - sea_lvl_obs[i]) * (pressure / 1000)) + sea_lvl_obs[i])))
            print("{}°C:{} ".format(temps[i+1],high_obs:=(((one_thousand_ft_obs[i+1] - sea_lvl_obs[i+1]) * (pressure / 1000)) + sea_lvl_obs[i+1])))
            print("{}°C:{} ".format(current_temp,(((high_obs - low_obs) * (current_temp / 100)) + low)))
            middle_obs = (((high_obs - low_obs) * (current_temp % 10)/10) + low_obs)
            header = ["{}°C".format(temps[i]),"{}°C".format(current_temp), "{}°C".format(temps[i+1])]
            data = [[sea_lvl_obs[i],(((sea_lvl_grnd[i+1] - sea_lvl_obs[i]) * (current_temp % 10)/10) + sea_lvl_obs[i]),sea_lvl_obs[i+1]],
                    [low_obs,middle_obs,high_obs],
                    [one_thousand_ft_obs[i],(((one_thousand_ft_obs[i+1] - one_thousand_ft_obs[i]) * (current_temp % 10)/10) + one_thousand_ft_obs[i]),one_thousand_ft_obs[i+1]]
                    ]
            print("OBS")
            print(tabulate(data,headers=header,tablefmt="grid"))



def main():
    print("\nWelcome to nana's sexy check ride calculator. *moans*")
    print("\n 1.Calculate Pressure Altitude \n 2.Shortfield take off distance")
    user = int(input("what would you like to do?:"))
    if user == 1:
        pressure_alt()
    elif user == 2:
        shortfield_takeoff_dist()
    else:
        print("Sorry, that was not an option!")
    print("\nThanks hoe, bye.")


main()
