import pandas
from numpy import nan

def data_verification(max):
    while True:
        try:
            i = int(input("Option: "))
            if max >= i >= 1:
                return i
            raise ValueError
        except ValueError:
            print("Invalid value")

data_salary = pandas.DataFrame({
    "name": ["Ana", "Bruno", "Carlos", "Daniel", "Eduardo"], 
    "salary": [4000, nan, 5000, nan, 10000]
    })

test = 0 #Test mode
if test == 1:
    while True: #Main menu
        print("\n1- Substitute 'nan' for the mean value \n2- Substitute 'nan' for the median value \n3- Finish program")
        option = data_verification(3)

        if option == 1: #Mean value
            data_salary["fixed salary"] = data_salary["salary"].fillna(data_salary["salary"].mean().round(2))
            print(data_salary)
        elif option == 2: #Median value
            data_salary["fixed salary"] = data_salary["salary"].fillna(data_salary["salary"].median().round(2))
            print(data_salary)
        elif option == 3: #Finish program
            print("Ending program...")
            break

data_temperatures = pandas.DataFrame({
    "days": ["monday", "tuesday", "wednesday", "thursday", "friday"],
    "temperature": [30, nan, nan, 28, 27]
    })

test = 0 #Test mode
if test == 1:
    while True: #Main menu
        print("\n1- Substitute 'nan' for the last value \n2- Substitute 'nan' for the next value \n3- Finish program")
        option = data_verification(3)

        if option == 1: #Foward fill
            data_temperatures["fixed temperatures"] = data_temperatures["temperature"].ffill()
            print(data_temperatures)
        elif option == 2: #Bacward fill
            data_temperatures["fixed temperatures"] = data_temperatures["temperature"].bfill()
            print(data_temperatures)
        elif option == 3: #Finish program
            print("Ending program...")
            break

data_city = pandas.DataFrame({
    "name": ["Ana", "Bruno", "Carlos", "Daniel", "Eduardo"],
    "city": ["São Paulo", nan, "Curitiba", nan, "Belém"]
})

test = 0 #Test mode
if test == 1:
    while True: #Main menu
        print("\n1- Substitute 'nan' for 'No information' \n2- Finish program")
        option = data_verification(2)

        if option == 1: #Foward fill
            data_city["fixed_city"] = data_city["city"].fillna("No information")
            print(data_city)
        elif option == 2: #Finish program
            print("Ending program...")
            break