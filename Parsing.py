import requests as rq
import pandas as pd


class DataParser:
    def __init__(self, job, number_of_pages):
        self.url = 'https://api.hh.ru/vacancies'
        self.job = job
        self.number_of_pages = number_of_pages

    def get_data(self):
        data = []
        for i in range(self.number_of_pages):
            url = 'https://api.hh.ru/vacancies'
            par = {'text': self.job, 'area': '113', 'per_page': '10', 'page': i}
            r = rq.get(url, params=par)
            e = r.json()
            data.append(e)
        return data

    def save_to_csv(self):
        data = self.get_data()
        vacancy_details = data[0]['items'][0].keys()
        df = pd.DataFrame(columns=list(vacancy_details))
        ind = 0
        for i in range(len(data)):
            for j in range(len(data[i]['items'])):
                df.loc[ind] = data[i]['items'][j]
                ind += 1
        csv_name = self.job + ".csv"
        df.to_csv(csv_name)


job_title = ["QA"]
for job in job_title:
    parser = DataParser(job, number_of_pages=100)
    parser.save_to_csv()
