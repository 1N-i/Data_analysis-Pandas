import pandas

data = pandas.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

experience_level = {
    "SE": "Senior",
    "MI": "Mid-level",
    "EN": "Junior",
    "EX": "Executive"
}
data["experience_level"] = data["experience_level"].replace(experience_level)

employment_type = {
    "FT": "Full-time",
    "PT": "Part-time",
    "FL": "Freelance",
    "CT": "Contract"
}
data["employment_type"] = data["employment_type"].replace(employment_type)

company_size = {
    "S": "Small",
    "M": "Medium",
    "L": "Large"
}
data["company_size"] = data["company_size"].replace(company_size)

remote_ratio = {
    0: "On-site",
    50: "Hybrid",
    100: "Remote"
}
data["remote_ratio"] = data["remote_ratio"].replace(remote_ratio)

def data_verification(max):
    while True:
        try:
            i = int(input("Option: "))
            if max >= i >= 1:
                return i
            raise ValueError
        except ValueError:
            print("Invalid value")

#Data cleaning
data_cleaned = data.dropna()
data_cleaned = data_cleaned.assign(work_year = data_cleaned["work_year"].astype("int64"))

test = 1 #Test mode
if test == 1:
    while True: #Main menu
        print("\n1- Show experience level \n2- Show employment type \n3- Show company size \n4- Show remote ratio")
        print("5- Show data count \n6- Finish program")
        option = data_verification(6)

        if option == 1: #Experience level
            print("\n", data_cleaned["experience_level"].value_counts())
        elif option == 2: #Employment type
            print("\n", data_cleaned["employment_type"].value_counts())
        elif option == 3: #Company size
            print("\n", data_cleaned["company_size"].value_counts())
        elif option == 4: #Remote ration
            print("\n", data_cleaned["remote_ratio"].value_counts())
        elif option == 5: #Data count
            print("\n", data_cleaned.describe(include = "object"))
        elif option == 6: #Finish program
            print("Ending program...")
            break