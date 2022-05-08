from requests import get

BASE_URL = "http://127.0.0.1:5000"
WORKERS = "/workers"

def printWorkers() -> None:
    API = BASE_URL + WORKERS
    workers = get(API).json()
    for position in workers.keys():
        print(str(position + ":"))
        if isinstance(workers[position], dict):
            print(workers[position]["Name"] + " " + workers[position]["Surname"])
        else:
            for person in workers[position]:
                print(person["Name"] + " " + person["Surname"])
        print()

def AverageRegularsSalary() -> float:
    API = BASE_URL + WORKERS
    regulars = get(API).json()["Regulars"]
    salary = 0
    for regular in regulars:
        salary += regular["Salary"]
    return round(salary/len(regulars), 2)

printWorkers()
print("Average Salary for Regular Workers: " + str(AverageRegularsSalary()))