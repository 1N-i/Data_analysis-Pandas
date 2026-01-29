import pandas

data = pandas.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

test = 0 #Test mode
if test == 1:
    print(data.columns) #Check names of columns
    print(data["remote_ratio"].value_counts())

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

#Before cleaning the data
test = 0 #Test mode
if test == 1:
    while True: #Main menu
        print("\n1- Show experience level \n2- Show employment type \n3- Show company size \n4- Show remote ratio")
        print("5- Show data count \n6- Finish program")
        option = data_verification(6)

        if option == 1: #Experience level
            print("\n", data["experience_level"].value_counts())
        elif option == 2: #Employment type
            print("\n", data["employment_type"].value_counts())
        elif option == 3: #Company size
            print("\n", data["company_size"].value_counts())
        elif option == 4: #Remote ration
            print("\n", data["remote_ratio"].value_counts())
        elif option == 5: #Data count
            print("\n", data.describe(include = "object"))
        elif option == 6: #Finish program
            print("Ending program...")
            break

data_cleaned = data.dropna()
data_cleaned = data_cleaned.assign(work_year = data_cleaned["work_year"].astype("int64"))

#After cleaning the data
test = 0 #Test mode
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

test = 0
if test == 1: #Bar graph
    import matplotlib.pyplot as plt
    import seaborn as sns
    ordered = data_cleaned.groupby("experience_level")["salary_in_usd"].mean().sort_values(ascending = False).index
    plt.figure(figsize = (8, 5))
    sns.barplot(data = data_cleaned, x = "experience_level", y = "salary_in_usd", order = ordered)
    plt.title("Distribuition of experience level")
    plt.xlabel("Experience Level")
    plt.ylabel("Mean salary yearly (USD)")
    plt.show()

test = 0
if test == 1: #Histogram
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.figure(figsize = (8, 4))
    sns.histplot(data_cleaned["salary_in_usd"], bins = 50, kde = True)
    plt.title("Distribuition of yearly salary")
    plt.xlabel("Salary (USD)")
    plt.ylabel("Frequency")
    plt.show()

test = 0
if test == 1: #Boxplot
    import matplotlib.pyplot as plt
    import seaborn as sns
    plt.figure(figsize = (8, 5))
    sns.boxplot(x = data_cleaned["salary_in_usd"])
    plt.title("Distribuition of yearly salary")
    plt.xlabel("Salary (USD)")
    plt.show()

test = 0
if test == 1: #Boxplot 2
    import matplotlib.pyplot as plt
    import seaborn as sns
    ordered = ["Senior", "Mid-level", "Junior", "Executive"]
    plt.figure(figsize = (8, 5))
    sns.boxplot(x="experience_level", y="salary_in_usd", data=data_cleaned, order=ordered, palette="Set2", hue = "experience_level")
    plt.title("Distribuition of yearly salary per experience level")
    plt.xlabel("Experience level")
    plt.ylabel("Salary (USD)")
    plt.show()

test = 0
if test == 1: #Plotly bar graph
    import plotly.express as px
    graph = data_cleaned.groupby("experience_level")["salary_in_usd"].mean().sort_values(ascending=False).reset_index()

    figure = px.bar(graph,
                    x = "experience_level",
                    y = "salary_in_usd",
                    title = "Mean salary by experience level",
                    labels = {"experience_level": "Experience level", "salary_in_usd": "Mean yearly salary (USD)"})
    figure.show()

test = 0
if test == 1: #Plotly pie graph
    import plotly.express as px
    graph = data_cleaned["remote_ratio"].value_counts().reset_index()
    graph.columns = ["Type of work", "Quantity"]

    figure = px.pie(graph,
                    names = "Type of work",
                    values = "Quantity",
                    title = "Proportion of work types"
                    )
    figure.show()

test = 0
if test == 1: #Plotly donut graph
    import plotly.express as px
    graph = data_cleaned["remote_ratio"].value_counts().reset_index()
    graph.columns = ["Type of work", "Quantity"]

    figure = px.pie(graph,
                    names = "Type of work",
                    values = "Quantity",
                    title = "Proportion of work types",
                    hole = 0.5)
    figure.update_traces(textinfo = "percent+label")
    figure.show()

#pip install matplotlib
#pip install seaborn
#pip install plotly