# -*- coding: utf-8 -*-
import scrapy
from urlparse import urljoin
from scrapy.http import FormRequest


class GlassdoorbotSpider(scrapy.Spider):
    name = 'glassdoorbot'

    custom_settings = {
        "DOWNLOAD_DELAY": 3,
        "CONCURRENT_REQUESTS_PER_DOMAIN": 3
        #"HTTPCACHE_ENABLED": True
    }

    allowed_domains = []
    '''
    Start url order:
    new york, ny
    california
    seattle
    colorado
    texas
    '''

    start_urls = ['https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=data&sc.keyword=data&locT=C&locId=1132348&jobType=',
                  'https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=data&sc.keyword=data&locT=S&locId=2280&jobType=,',
                  'https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=data&sc.keyword=data&locT=C&locId=1150505&jobType=',
                  'https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=data&sc.keyword=data&locT=C&locId=1138213&jobType=',
                  'https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=data&sc.keyword=data&locT=S&locId=2519&jobType=',
                  'https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword=data&sc.keyword=data&locT=S&locId=1347&jobType='
                  '']
    base_url = 'https://www.glassdoor.com/'

    def parse(self, response):
        return [FormRequest.from_response(
            response,
            formdata={'KeywordSearch': 'data'},
            callback=self.parse_page)]

    def parse_page(self, response):
        job_link = response.xpath('//*[@id="MainCol"]/div/ul/li//a[@class="jobLink"]/@href').extract()
        job_link = [urljoin(self.base_url, url) for url in job_link]
        job_name = response.xpath('//*[@id="MainCol"]/div/ul/li//a[@class="jobLink"]/text()').extract()

        for i in range(len(job_link)):
            yield scrapy.Request(
                url=job_link[i],
                callback=self.parse_job,
                meta={'url': job_link[i]}
            )

        next_url = response.xpath('//li[@class="next"]//@href').extract_first()
        next_url = urljoin(self.base_url, next_url)
        print("NEXT PAGE ____________________________:", next_url)

        yield scrapy.Request(
            url=next_url,
            callback=self.parse_page
        )

    def parse_job(self, response):

        #url = response.request.meta['url']

        title = (
            response.xpath('//*[@id="HeroHeaderModule"]/div[3]/div[1]/div[2]/div[1]/h2/text()').extract()
        )

        header = (
            response.xpath('normalize-space(//*[@id="HeroHeaderModule"]/div[3]/div[1]/div[2])').extract()
        )

       # company = (
        #    response.xpath('//*[@id="HeroHeaderModule"]/div[3]/div[1]/div[2]/span[1]/text()').extract()
        #)
        salary_est = (
            response.xpath('//*[@id="salWrap"]/h2/text()').extract()
        )
        description = (
            response.xpath('normalize-space(//*[@id="JobDescriptionContainer"])').extract()
        )
        yield {
            'title': title,
            'header': header,
            #'company': company,
            'salary_estimation': salary_est,
            'description': description
        }
