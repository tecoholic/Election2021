import os
import scrapy
import pandas as pd


class EciSpider(scrapy.Spider):
    name = 'eci'
    allowed_domains = ['results.eci.gov.in']

    def start_requests(self):
        for i in range(1, 235):
            url = f'https://results.eci.gov.in/Result2021/ConstituencywiseS22{i}.htm?ac={i}'
            yield scrapy.Request(url=url, callback=self.parse)

        for i in range(1, 127):
            url = f"https://results.eci.gov.in/Result2021/ConstituencywiseS03{i}.htm?ac={i}"
            yield scrapy.Request(url=url, callback=self.parse)

        for i in range(1, 141):
            url = f"https://results.eci.gov.in/Result2021/ConstituencywiseS11{i}.htm?ac={i}"
            yield scrapy.Request(url=url, callback=self.parse)

        for i in range(1, 31):
            url = f"https://results.eci.gov.in/Result2021/ConstituencywiseU07{i}.htm?ac={i}"
            yield scrapy.Request(url=url, callback=self.parse)

        for i in range(1, 295):
            url = f"https://results.eci.gov.in/Result2021/ConstituencywiseS25{i}.htm?ac={i}"
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        rows = response.xpath('//*[@id="div1"]/table[1]/tbody/tr').getall()
        rows = "<table>" + "".join(rows[2:-1]) + "</table>"

        table = pd.read_html(rows)[0]

        ac_no = response.url.split("ac=")[-1]

        if "ConstituencywiseS03" in response.url:
            state = "AS"
        elif "ConstituencywiseS11" in response.url:
            state = "KL"
        elif "ConstituencywiseU07" in response.url:
            state = "PY"
        elif "ConstituencywiseS25" in response.url:
            state = "WB"
        else:
            state = "TN"

        if not os.path.isdir(state):
            os.mkdir(state)

        fname = os.path.join(state, f"{ac_no}.csv")

        table.to_csv(fname, index=False)
        print(f"State: {state} Constituency: {ac_no}")
