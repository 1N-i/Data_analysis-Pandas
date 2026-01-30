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
        print("5- Show data count \n6- Pie graph \n7- Donut graph \n8- Close menu")
        option = data_verification(7)

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
        elif option == 6:
            import matplotlib.pyplot as plt
            import seaborn as sns
            import plotly.express as px

            while True:
                print("\n1- Bar graph \n2- Histogram \n3- Boxplot \n4- Boxplot 2")
                print("5- Bar graph 2 \n6- See graphs \n7- Finish program")
                option2 = data_verification(8)
                if option2 == 1: #Bar graph
                    ordered = data_cleaned.groupby("experience_level")["salary_in_usd"].mean().sort_values(ascending = False).index
                    plt.figure(figsize = (8, 5))
                    sns.barplot(data = data_cleaned, x = "experience_level", y = "salary_in_usd", order = ordered)
                    plt.title("Distribuition of experience level")
                    plt.xlabel("Experience Level")
                    plt.ylabel("Mean salary yearly (USD)")
                    plt.show()
                elif option2 == 2: #Histogram
                    plt.figure(figsize = (8, 4))
                    sns.histplot(data_cleaned["salary_in_usd"], bins = 50, kde = True)
                    plt.title("Distribuition of yearly salary")
                    plt.xlabel("Salary (USD)")
                    plt.ylabel("Frequency")
                    plt.show()
                elif option2 == 3: #Boxplot
                    plt.figure(figsize = (8, 5))
                    sns.boxplot(x = data_cleaned["salary_in_usd"])
                    plt.title("Distribuition of yearly salary")
                    plt.xlabel("Salary (USD)")
                    plt.show()
                elif option2 == 4: #Boxplot 2
                    ordered = ["Senior", "Mid-level", "Junior", "Executive"]
                    plt.figure(figsize = (8, 5))
                    sns.boxplot(x="experience_level", y="salary_in_usd", data=data_cleaned, order=ordered, palette="Set2", hue = "experience_level")
                    plt.title("Distribuition of yearly salary per experience level")
                    plt.xlabel("Experience level")
                    plt.ylabel("Salary (USD)")
                    plt.show()
                elif option2 == 5: #Plotly bar graph
                    graph = data_cleaned.groupby("experience_level")["salary_in_usd"].mean().sort_values(ascending=False).reset_index()
                    figure = px.bar(graph,
                    x = "experience_level",
                    y = "salary_in_usd",
                    title = "Mean salary by experience level",
                    labels = {"experience_level": "Experience level", "salary_in_usd": "Mean yearly salary (USD)"})
                    figure.show()
                elif option2 == 6: #Plotly pie graph
                    graph = data_cleaned["remote_ratio"].value_counts().reset_index()
                    graph.columns = ["Type of work", "Quantity"]
                    figure = px.pie(graph,
                                    names = "Type of work",
                                    values = "Quantity",
                                    title = "Proportion of work types")
                    figure.show()
                elif option2 == 7: #Plotly donut graph
                    graph = data_cleaned["remote_ratio"].value_counts().reset_index()
                    graph.columns = ["Type of work", "Quantity"]

                    figure = px.pie(graph,
                                    names = "Type of work",
                                    values = "Quantity",
                                    title = "Proportion of work types",
                                    hole = 0.5)
                    figure.update_traces(textinfo = "percent+label")
                    figure.show()
                elif option2 == 8:
                    break
        elif option == 7: #Finish program
            print("Ending program...")
            break