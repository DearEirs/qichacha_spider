#!coding=utf-8
import scrapy
from qichacha.items import  QichachaItem
import re


class QiChaChaSpider(scrapy.Spider):
    name = "qichacha1"
    suffix = ""
    url = "https://www.qichacha.com"
    start_urls = (
        url + suffix,
    )
    cookie = {
        'UM_distinctid':'15d2a788dcc8e1-025c8d5bc8b836-8383667-100200-15d2a788dcdc11',
        '_uab_collina':'149965613035223206976143',
        'gr_user_id':'e60370f9-933f-46ce-82c5-d1ac176db196',
        'hasShow':'1',
        '_umdata':'0712F33290AB8A6D951430D1E0117EE1D14231F8130F1C2858BD826A13625AE2FD621DC5C2F9A92DCD43AD3E795C914C09063375D36107DCACBC946225EED311',
        'PHPSESSID':'850lvp2rq40cds1hsn83nkton5',
        'acw_tc':'AQAAAPuEvn89+wwAGAWCd7ZVD5bspHPf',
        'gr_session_id_9c1eb7420511f8b2':'d961fa41-6e3e-4632-a548-4256ca09c71a',
        'CNZZDATA1254842228':'415804783-1499653268-%7C1499745096'
    }

    def start_requests(self):
        return [scrapy.Request("https://www.qichacha.com/user_login", meta={'cookiejar': 1}, callback=self.login)]


    def login(self,response):

        return [scrapy.FormRequest.from_response(response,
                                                 meta= {'cookiejar':response.meta['cookiejar']},
                                                 formdata={
                                                     'nameNormal': '18816797855',
                                                     'pwdNormal': '523920',
                                                     'keep': 'on',
                                                     'csessionid_one': '01RGpRDMWvrFihIVZpI9IiDLCMukJb5wygnUHr_xFgWIegcOf-vRFUwvGYP1_oSvX7mji-apZNVH5xFmdBlEJpMvZG5kc9ij6_AYnrMCh4tHCWvGr0uFeOb_oizPOpArhN',
                                                     'sig_one': '05LhskazT-maWpw8U2LmKB3QinSEf25gceASVjQojoMlxOrLYopJuxIJaGsTYf32gNQN4JBNu1LYXrW9xImZ0X6DD0Q6nBOKaxida1cokTdPF0RwtKkX1nIQfiQoHoANJJ1znmek3sAdzC96DzfIuT48Pt_PjWvEABJ47xGOUxs5pP2btTxUBUTYWG7sETQsLP-9mgLY04FeTyqagKa4MVD1hxMgVF6pDW4QD1bgllG_KeojQnEd9mLErY_Atb99k9Yn-GrW3AL7HPi7v0QSx1gqzx4uQjIrj3tSqf4H8J-3qO7raJwI6eM6vR2u77OpV3',
                                                     'token_one': 'QNYX:1499957990145:0.6167600148644341',
                                                     'scene_one': 'login',
                                                     'verify_type': '1'
                                                 },
                                                 callback=self.after_login,
                                                 dont_filter=True
                                                 )]

    def after_login(self,response):
        yield scrapy.Request(
            url = self.url,
            cookies=self.cookie,
            callback= self.get_industry
        )

    def get_industry(self, response):
        industry_urls = response.xpath('//div[@class="col-md-8 columns"]/ul/li/a/@href').extract()
        for i in industry_urls:
            yield scrapy.Request(
                url = self.url + i,
                cookies=self.cookie,
                #url = 'https://www.qichacha.com/gongsi_industry.shtml?industryCode=A&subIndustryCode=05&industryorder=0&p=10',

                callback= self.get_company
            )

    def get_company(self,response):
        #print '------------------------------------------------------'
        #print response.url

        #print response.encoding
        company_urls = response.xpath('//section[@class="panel panel-default"]/a/@href').extract()
        #print company_urls
        for i in company_urls:
            yield scrapy.Request(
                url = self.url + i,
                cookies=self.cookie,
                #meta={
                 #   'dont_redirect': True,
                  #  'handle_httpstatus_list': [302]
                #},
                callback= self.get_data
            )
        #last_page = response.xpath('//div[@class="text-left m-t-lg m-b-lg"]/a').extract()
        #print response.xpath('//div[@class="text-left m-t-lg m-b-lg"]').extract()
        for i in range(2,100):
            if 'p=' not in response.url:
                page_url = response.url + '&p=%s' % i
            else:
                page_url = re.sub('p=\d+','&p=%s' % i,response.url)
            yield scrapy.Request(
                url= page_url,
                cookies=self.cookie,
                meta={
                    'dont_redirect': True,
                    'handle_httpstatus_list': [302]
                },
                callback= self.get_company
            )
        '''
        page_url = '/gongsi_industry.shtml?industryCode=A&subIndustryCode=05&industryorder=0&p=%s'
        a = 'https://www.qichacha.com/gongsi_industry?industryCode=C&subIndustryCode=17&industryorder=2'
        if 'p=' not in response.url:
            next_page_url = response.url + 'p=%s'
        else:
            next_page_url =
        for i in range(2,501):
            yield scrapy.Request(
                url= response + 'p=%s' % i

        '''

    def get_data(self,response):
        print '----------------------------------------'
        if len(response.body) < 200 :
            print response.body
            yield scrapy.Request(
                url= 'http://www.qichacha.com/index_verifyAction',
                cookies = self.cookie,
                callback=self.verification
            )
            return

        company = response.xpath('//div[@class="text-big font-bold company-top-name"]/text()').extract()[0]
        data = response.xpath('//small[@class="clear text-ellipsis m-t-xs text-md text-black ma_line2"]/text()').extract()[0]
        data2 = response.xpath('//small[@class="clear m-t-xs text-md text-black ma_line3 m-r"]/text()').extract()[0]
        address = response.xpath('//small[@class="clear m-t-xs text-md text-black ma_line3 m-r"]/span[last()]/text()').extract()[0]
        phone = data.split('\n')[2]
        web_site = data2.split('\n')[2]
        try:
            email = response.xpath('//small[@class="clear text-ellipsis m-t-xs text-md text-black ma_line2"]/a/text()').extract()[0]
        except:
            email = response.xpath('//small[@class="clear text-ellipsis m-t-xs text-md text-black ma_line2"]/text()[2]').extract()[0]
        company_id = response.url.split('_')[-1].split('.')[0]

        print company_id,company
        yield scrapy.Request(
            url='http://www.qichacha.com/company_getinfos?unique=%s&companyname=%s&tab=base' % (company_id,company),
            cookies = self.cookie,
            meta={
                'dont_redirect': True,
                'handle_httpstatus_list': [302],
                'company':company,
                'phone':phone,
                'email':email,
                'web_site':web_site,
                'address':address
            },
            callback=self.get_data2
        )
    def get_data2(self,response):

        item = QichachaItem()
        item['company'] = response.meta['company']
        item['email'] = response.meta['email']
        item['web_site'] = response.meta['web_site']
        item['address'] = response.meta['address']


        main_staff = response.xpath('//table[@class="m_changeList"]/tr/td/div[@style="margin-top:8px;"]/a/text()').extract()
        item['main_staff'] = ','.join(main_staff)


        datas = response.xpath('//section[@class="panel b-a base_info"]/table[@class="m_changeList"]')[0]

        item['credit_code'] = datas.xpath('./tr[1]/td[2]/text()').extract()[0]
        item['taxpayer_code'] = datas.xpath('./tr[1]/td[4]/text()').extract()[0]
        item['registered_code'] = datas.xpath('./tr[2]/td[2]/text()').extract()[0]
        item['organization_code'] = datas.xpath('./tr[2]/td[4]/text()').extract()[0]
        item['representative'] = datas.xpath('./tr[3]/td[2]/text()').extract()[0]
        item['registered_capital'] = datas.xpath('./tr[3]/td[4]/text()').extract()[0]
        item['state'] = datas.xpath('./tr[4]/td[2]/text()').extract()[0]
        item['create_date'] = datas.xpath('./tr[4]/td[4]/text()').extract()[0]
        item['type'] = datas.xpath('./tr[5]/td[2]/text()').extract()[0]
        item['scale'] = datas.xpath('./tr[5]/td[4]/text()').extract()[0]
        item['limit_date'] = datas.xpath('./tr[6]/td[2]/text()').extract()[0]
        item['registration_authority'] = datas.xpath('./tr[6]/td[4]/text()').extract()[0]
        item['approved_date'] = datas.xpath('./tr[7]/td[2]/text()').extract()[0]
        item['english_name'] = datas.xpath('./tr[7]/td[4]/text()').extract()[0]
        item['area'] = datas.xpath('./tr[8]/td[2]/text()').extract()[0]


        yield item

    def verification(self,response):
        print '**************************************'
        print response.body
        return [scrapy.Request.from_response(response,
                                                 formdata={
                                                     'scene': 'register',
                                                     'token': 'QNYX:1499915612736:0.6468428006101972',
                                                     'sig': '05LhskazT-maWpw8U2LmKB3cfyUliha3vsmSs6DSyFgFQ2F-4BRG-UO24AeyIzBSFl1MGrlKm6dS4fcXpZAVtJR1iD7a8cHUnjhn1wxJn56aD2Qr3Qq9lYVBAJdxf8M_63FWKcclfRx3GyID1v2XqNJWVaiJGlMdyd3ffihB312Bm4BE_Y7TY7C0D_68WiBEoYHSpT9cS9-Przm-AfGFV2uuIrKpvh5DMaYZP7fLz0uiVY26LDObyLkI1th0xD32MrSEcogZ2DgZT5yDQWmrrPR8DWvJuiMfOILQ4wKL16DY97l39ieVrRTnTnqe7kUqMQ',
                                                     'csessionid': '018a5GMUYN008JRtkcdREuI09vM4OteKYwgpGXgMGYCX5qtwg3NzlZNSidSEHfQyT9iFEEdLLX-RMhB-LRhNhi0LrrmI8mVDTqs9hYP4heR3z8M_NIKQPpSsijPlTWurzw',
                                                     'type': 'companyview',

                                                 },
                                                 callback=self.get_data,
                                                 dont_filter=True
                                                 )]


