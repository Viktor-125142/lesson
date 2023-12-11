import pandas as pd
import pprint

pr = pprint.PrettyPrinter()

data = pd.read_csv("data_fake.csv", encoding="cp1251", sep=";")
data = data.drop(["Тех. секретарь", "Unnamed: 27"], axis=1)

d = {chr(ord("A") + i): data.columns[i] for i in range(len(data.columns))}


pr.pprint(d)

data.columns = d.keys()

ind = data[data["Y"] == "да"].index
data = data.drop(ind, axis=0)
data = data.drop(["Y"], axis=1)

ind = data[data["Специальность"] != "Бакалавры/Специалисты"].index
data = data.drop(ind, axis=0)

data = data.drop(["0"], axis=1)

print(data.info())
