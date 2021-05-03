import scrapy
import pandas as pd


class EciSpider(scrapy.Spider):
    name = 'eci'
    allowed_domains = ['results.eci.gov.in']

    def start_requests(self):
        for i in range(1, 235):
            url = f'https://results.eci.gov.in/Result2021/ConstituencywiseS22{i}.htm?ac={i}'
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        rows = response.xpath('//*[@id="div1"]/table[1]/tbody/tr').getall()
        rows = "<table>" + "".join(rows[2:-1]) + "</table>"

        table = pd.read_html(rows)[0]

        ac_no = response.url.split("ac=")[-1]

        table.to_csv(f"{ac_no}.csv", index=False)
        print("Saved Constituency: ", ac_no)
