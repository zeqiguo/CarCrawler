#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import re
import os
import string
import csv

import numpy as np
import pandas as pd


from bs4 import BeautifulSoup


# In[2]:


# ChromeBot
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}

root = 'https://www.carcomplaints.com'


# In[66]:


# Google Cloud Version

# class Crawler:
#     '''
#     url: url that need to be crawled 
#     '''
#     ################### INIT FUNCTION ###################

#     def __init__(self, url):
#         self.url = url

        
#     ################### PRIVATE FUNCTIONS ##################
#     def __to_html(self):
#         html = requests.get(url=self.url, headers=headers)
#         return html.text

    
#     ################### BASIC FUNCTIONS ###################
#     def get_head(self):
#         '''
#         :return: html <head>
#         '''
#         # return html code of head
#         html = self.__to_html()
#         soup = BeautifulSoup(html, 'lxml')
#         return soup.head

#     def get_title(self):
#         '''
#         :return: html <title>
#         '''
#         # return the page title
#         html = self.__to_html()
#         soup = BeautifulSoup(html, 'lxml')
#         return soup.title

#     def get_body(self):
#         '''
#         :return: html <body>
#         '''
#         # return html code of body
#         html = self.__to_html()
#         soup = BeautifulSoup(html, 'lxml')
#         return soup.body

    
#     ##################### MAKE FUNCTIONS #####################
#     def get_makes(self) -> list:
#         '''
#         :return: [Acura]
        
#         Return the makes as a list, prepare for further crawl, the return values in the list was removed all '/'
#         find all of a tags whitch include required title but not have class_ in body
#         '''
        
#         return [title.get('href').replace('/', '') for title in self.get_body().find_all(title=re.compile('Complaints About'), class_=False)]

#     def number_of_makes(self) -> int:
#         return len(self.get_makes())

#     def get_make_urls(self, save=False) -> list:
#         '''
#         :return: [https://www.carcomplaints.com/Acura]
        
#         Use makes list from self.makes to combine with root 
#         '''
#         path = 'Make/'
#         make_url_pool = []
#         makes = self.get_makes()

#         for make in makes:
#             make_url = root+'/'+make
#             make_url_pool.append(make_url)

# #             if save:
# #                 if not os.path.exists('Make'):
# #                     os.mkdir('Make')
# #                 make_path = path + make                             # specific make path
# #                 if not os.path.exists(make_path):
# #                     os.mkdir(make_path)
#         if save and not os.path.exists('makes.npy'):
#             np.save(file='makes.npy', arr=make_url_pool)

#         return make_url_pool

    
#     ##################### MODE FUNCTIONS ######################
#     def get_models(self, make: str) -> list:
#         '''
#         :return: [/Acura/CL/]
        
#         find as /Make/Model/
#         '''
#         # return models as a list
#         # all make got was removed '/'
#         c1 = Crawler(root+'/'+make)
#         return [model.get('href') for model in c1.get_body().find_all(href=re.compile('/%s/' % make), title=re.compile(r'complaints'))]

#     def get_model_urls(self, save=False) -> list:
#         '''
#         :return: [[]]
        
        
#         '''
#         model_url_pool = []                                                     # 2D list
#         make_urls = self.get_make_urls(save)
#         makes = self.get_makes()

#         for make in makes:
#             # get models by giving make
#             models = self.get_models(make)
#             # use to save models of this make
#             urls = []
#             for model in models:
#                 model_url = root + model
#                 urls.append(model_url)
#                 # path for make model dictionary
#                 model_path = 'Make' + model
#                 if save:
#                     if not os.path.exists(model_path):
#                         os.mkdir(model_path)
#             model_url_pool.append(urls)

# #             if save and not os.path.exists('models.txt'):
# #                 with open('models.txt', 'a', encoding='utf8') as f:
# #                     f.write('{}\n{}\n\n' .format(make, models))
#         if save and not os.path.exists('models.npy'):
#             np.save(file='models.npy', arr=model_url_pool)

#         return model_url_pool

#     ##################### YEAR FUNCTIONS ######################

#     def get_years(self, url: str) -> list:
#         '''
#         :return: 
        
        
#         '''
#         c1 = Crawler(url)
#         return [year.get('href') for year in c1.get_body().find_all(href=re.compile(r'%s/[0-9]{4}\/$' % url.split('/')[-2]), title=re.compile(r'Problems'))]

#     def get_year_urls(self, save=False) -> list:
#         '''
#         :return: 
        
        
#         '''
#         year_url_pool = []
#         model_url_pool = self.get_model_urls(
#             save)                                 # [[]]

#         for model_urls in model_url_pool:
#             models = []
#             for url in model_urls:
#                 years = self.get_years(url)
#                 year_urls = [root+year for year in years]
#                 models.append(year_urls)
#             year_url_pool.append(models)

#         if save and not os.path.exists('years.npy'):
#             np.save(file='years.npy', arr=year_url_pool)

#         return year_url_pool

#     ##################### PROBKEM(LV1) FUNCTIONS ######################

#     def get_problems(self, url: str) -> list:
#         c1 = Crawler(url)
#         return [problem.find('a').get('href') for problem in c1.get_body().find_all(id=re.compile('bar\d{1}'), class_=True)]

#     def get_problem_urls(self, save=False) -> list:
#         '''
#         :return: 
        
        
#         '''

#         problems_url_pool = []

#         if not os.path.exists('years.npy'):
#             self.get_year_urls(save=True)

#         urls = np.load('years.npy')
#         for makes in urls:
#             for models in makes:
#                 for years in models:
#                     problem_href = self.get_problems(years)
#                     problems_url_pool.append(
#                         [years+problem for problem in problem_href])

#         if save:
#             np.save(file='problems.npy', arr=problems_url_pool)

#         return problems_url_pool             # [[[]]]

#     ##################### PROBKEM(LV2) FUNCTIONS ######################
#     def get_sub_problems(self, url: str) -> list:
#         '''
#         :return: 
        
        
#         '''
#         c1 = Crawler(url)
#         return [sub_problem.find('a').get('href') for sub_problem in c1.get_body().find_all(id=re.compile('bar\d{1}'))]

#     def get_sub_problem_urls(self, save=False) -> list:
#         '''
#         :return: 
        
#         '''
#         sub_problem_url_pool = []

#         if not os.path.exists('problems.npy'):
#             self.get_problem_urls(save=True)
#         p_urls = np.load('problems.npy')
#         for urls in p_urls:
#             problems_pool = []
#             for url in urs:
#                 sub_p_href = self.get_sub_problems(url)
#                 problems_pool.append(sub_p_href)
# #                 for each in sub_p_href:
# #                     sub_problem_url_pool.append(root+each)
#             sub_problem_url_pool.append(problems_pool)

#         if save:
#             np.save(file='sub_problems.npy', arr=sub_problem_url_pool)

#         return sub_problem_url_pool

#     #################### COMMENTS FUNCTIONS ######################

#     def get_comments(self, url: str) -> list:
#         '''
#         :return: 
        
        
#         '''
#         # return comments div
#         c1 = Crawler(url)
#         results = c1.get_body().find_all(class_=re.compile(r'^comments'))
#         return results

#     @log('execute')
#     def get_date(self, url: str) -> list:
        
#         c1 = Crawler(url)
#         time = c1.get_body().find_all(class_=re.compile(r'^pdate'))
#         return time

#     def csv_header(self, all_header=False):
#         '''
#         :return:
        
        
#         '''
#         cars = np.load('problems.npy')

#         problem_set = set()
#         for car in cars:
#             for record in car:
#                 problem = record.split('/')[-2]
#                 problem_set.add(problem)
#         if all_header:        
#             return ['Make', 'Model', 'Year'] + list(problem_set)
#         else:
#             return list(problem_set)
    
#     def problem2index(self):
#         '''
#         :return: {transmission: 1}
        
#         pair the problem to index(int)
#         '''
#         problem_dict = {}
#         headers = self.csv_header()
        
#         for index in range(len(headers)):
#             problem_dict[headers[index]] = index+3
        
#         return problem_dict
        

    
#     def get_all_comments(self):
#         '''
#         :return: 
        
#         save as a csv file, all 23 columns. First three col are Make, Model, Year, other 20 are different problems. 
#         '''
#         print('=======================================================================================')
#         print('============================     CRAWLER START WORKING     ============================')
#         print('=======================================================================================')
#         print('============================      Wait Paitent Please      ============================')
#         print('============================               .               ============================')
#         print('============================               .               ============================')
#         print('============================               .               ============================')
#         print('============================               .               ============================')
#         print('============================               .               ============================')
        
#         all_comments = []
#         row = []
        
#         header = self.csv_header(all_header=True)
#         index_table = self.problem2index()
        
#         with open('CarV3_1.csv', mode='w', encoding='utf-8') as carFile:
#             writer = csv.writer(carFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#             writer.writerow(header)
            
#             years = np.load('sub_1.npy')
# #             new_years = [a for a in years if len(a)!=0]
#             new_years = list(filter(lambda x: len(x)!=0, years))
            
#             for year_ in new_years:
                
# #               got make model year
#                 sp = year_[0][0].split('/')
#                 make = sp[1]
#                 model = sp[2]
#                 year = sp[3]
#                 row = [make, model, year] + [0 for i in range(20)]

#                 for problems in year_:
#                     comment_list =[]
# #                   got problem
#                     problem = problems[0].split('/')[4]

#                     for sub_p in problems:
            
# #                       crawler got comments and save into a list
#                         comments = self.get_comments(root+sub_p)
#                         comment_list += [comment.text for comment in comments]

# #                   find row index  
#                     index = index_table[problem]
#                     row[index] = comment_list         # change value at index
#                 writer.writerow(row)
            
#         print('============================               DONE            ============================')

                        
                        

#     #################### TEST FUNCTIONS ######################



# In[ ]:


# Mac Version


class Crawler:
    '''
    url: url that need to be crawled 
    '''
    ################### INIT FUNCTION ###################

    def __init__(self, url):
        self.url = url

        
    ################### PRIVATE FUNCTIONS ##################
    def __to_html(self):
        html = requests.get(url=self.url, headers=headers)
        return html.text
    
    
    ##################### DECORATOR ########################
    def log(text):
        def decorator(func):
            def wrapper(*args, **kw):
                print('%s %s():' % (text, func.__name__))
                return func(*args, **kw)
            return wrapper
        return decorator


    ################### BASIC FUNCTIONS ###################
    @log('execute')
    def get_head(self):
        '''
        :return: html <head>
        '''
        # return html code of head
        html = self.__to_html()
        soup = BeautifulSoup(html, 'lxml')
        return soup.head

    @log('execute')
    def get_title(self):
        '''
        :return: html <title>
        '''
        # return the page title
        html = self.__to_html()
        soup = BeautifulSoup(html, 'lxml')
        return soup.title

    @log('execute')
    def get_body(self):
        '''
        :return: html <body>
        '''
        # return html code of body
        html = self.__to_html()
        soup = BeautifulSoup(html, 'lxml')
        return soup.body

    
    ##################### MAKE FUNCTIONS #####################
    @log('execute')
    def get_makes(self) -> list:
        '''
        :return: [Acura]
        
        Return the makes as a list, prepare for further crawl, the return values in the list was removed all '/'
        find all of a tags whitch include required title but not have class_ in body
        '''
        
        return [title.get('href').replace('/', '') for title in self.get_body().find_all(title=re.compile('Complaints About'), class_=False)]

    @log('execute')
    def number_of_makes(self) -> int:
        return len(self.get_makes())

    @log('execute')
    def get_make_urls(self, save=False) -> list:
        '''
        :return: [https://www.carcomplaints.com/Acura]
        
        Use makes list from self.makes to combine with root 
        '''
        path = 'Make/'
        make_url_pool = []
        makes = self.get_makes()

        for make in makes:
            make_url = root+'/'+make
            make_url_pool.append(make_url)

#             if save:
#                 if not os.path.exists('Make'):
#                     os.mkdir('Make')
#                 make_path = path + make                             # specific make path
#                 if not os.path.exists(make_path):
#                     os.mkdir(make_path)
        if save and not os.path.exists('makes.npy'):
            np.save(file='makes.npy', arr=make_url_pool)

        return make_url_pool

    
    ##################### MODE FUNCTIONS ######################
    @log('execute')
    def get_models(self, make: str) -> list:
        '''
        :return: [/Acura/CL/]
        
        find as /Make/Model/
        '''
        # return models as a list
        # all make got was removed '/'
        c1 = Crawler(root+'/'+make)
        return [model.get('href') for model in c1.get_body().find_all(href=re.compile('/%s/' % make), title=re.compile(r'complaints'))]

    @log('execute')
    def get_model_urls(self, save=False) -> list:
        '''
        :return: [[]]
        
        get a 2D list, each dimension means models of each make
        '''
        model_url_pool = []                                                     # 2D list
        make_urls = self.get_make_urls(save)
        makes = self.get_makes()

        for make in makes:
            # get models by giving make
            models = self.get_models(make)
            # use to save models of this make
            urls = []
            for model in models:
                model_url = root + model
                urls.append(model_url)
                # path for make model dictionary
                model_path = 'Make' + model
                if save:
                    if not os.path.exists(model_path):
                        os.mkdir(model_path)
            model_url_pool.append(urls)

#             if save and not os.path.exists('models.txt'):
#                 with open('models.txt', 'a', encoding='utf8') as f:
#                     f.write('{}\n{}UUUUUU\n\n' .format(make, models))
        if save and not os.path.exists('models.npy'):
            np.save(file='models.npy', arr=model_url_pool)

        return model_url_pool

    ##################### YEAR FUNCTIONS ######################

    @log('execute')
    def get_years(self, url: str) -> list:
        '''
        :return: 
        
        
        '''
        c1 = Crawler(url)
        return [year.get('href') for year in c1.get_body().find_all(href=re.compile(r'%s/[0-9]{4}VVVVVV\/$' % url.split('/')[-2]), 
                                                                    title=re.compile(r'Problems'))]

    @log('execute')
    def get_year_urls(self, save=False) -> list:
        '''
        :return: 
        
        get a 3D list, 2nd dimension means same model, 3rd dimension means same years.
        '''
        year_url_pool = []
        model_url_pool = self.get_model_urls(
            save)                                 # [[]]

        for model_urls in model_url_pool:
            models = []
            for url in model_urls:
                years = self.get_years(url)
                year_urls = [root+year for year in years]
                models.append(year_urls)
            year_url_pool.append(models)

        if save and not os.path.exists('years.npy'):
            np.save(file='years.npy', arr=year_url_pool)

        return year_url_pool

    ##################### PROBKEM(LV1) FUNCTIONS ######################

    @log('execute')
    def get_problems(self, url: str) -> list:
        c1 = Crawler(url)
        return [problem.find('a').get('href') for problem in c1.get_body().find_all(id=re.compile('bar\d{1}'), class_=True)]

    @log('execute')
    def get_problem_urls(self, save=False) -> list:
        '''
        :return: 
        
        1D list, urls of each year
        '''

        problems_url_pool = []

        if not os.path.exists('years.npy'):
            self.get_year_urls(save=True)

        urls = np.load('years.npy')
        for makes in urls:
            for models in makes:
                for years in models:
                    problem_href = self.get_problems(years)
                    problems_url_pool.append(
                        [years+problem for problem in problem_href])

        if save:
            np.save(file='problems.npy', arr=problems_url_pool)

        return problems_url_pool             # [[[]]]

    ##################### PROBKEM(LV2) FUNCTIONS ######################
    @log('execute')
    def get_sub_problems(self, url: str) -> list:
        '''
        :return: 
        
        
        '''
        c1 = Crawler(url)
        return [sub_problem.find('a').get('href') for sub_problem in c1.get_body().find_all(id=re.compile('bar\d{1}'))]

    @log('execute')
    def get_sub_problem_urls(self, save=False) -> list:
        '''
        :return: 
        
        2D list, 2nd dimension means different sub problems.
        '''
        sub_problem_url_pool = []

        if not os.path.exists('problems.npy'):
            self.get_problem_urls(save=True)
        p_urls = np.load('problems.npy')
        for urls in p_urls:
            problems_pool = []
            for url in urs:
                sub_p_href = self.get_sub_problems(url)
                problems_pool.append(sub_p_href)
#                 for each in sub_p_href:
#                     sub_problem_url_pool.append(root+each)
            sub_problem_url_pool.append(problems_pool)

        if save:
            np.save(file='sub_problems.npy', arr=sub_problem_url_pool)

        return sub_problem_url_pool

    #################### COMMENTS FUNCTIONS ######################

    @log('execute')
    def get_comments(self, url: str) -> list:
        '''
        :return: 
        
        
        '''
        # return comments div and time div
        c1 = Crawler(url)
        results = c1.get_body().find_all(class_=re.compile(r'^comments'))
        return results
    
    @log('execute')
    def get_date(self, url: str) -> list:
        
        c1 = Crawler(url)
        time = c1.get_body().find_all(class_=re.compile(r'^pdate'))
        return time

    @log('execute')
    def csv_header(self, all_header=False):
        '''
        :return:
        
        create a hearder, Make, Model, Year, others are name of problems
        '''
        cars = np.load('problems.npy')

        problem_set = set()
        for car in cars:
            for record in car:
                problem = record.split('/')[-2]
                problem_set.add(problem)
        if all_header:        
            return ['Make', 'Model', 'Year'] + list(problem_set)
        else:
            return list(problem_set)
    
    @log('execute')
    def problem2index(self):
        '''
        :return: {transmission: 1}
        
        pair the problem to index(int)
        '''
        problem_dict = {}
        headers = self.csv_header()
        
        for index in range(len(headers)):
            problem_dict[headers[index]] = index+3
        
        return problem_dict
        


    @log('execute')
    def get_all_comments(self):
        '''
        :return: 
        
        save as a csv file, all 23 columns. First three col are Make, Model, Year, other 20 are different problems. 
        '''
        print('=======================================================================================')
        print('============================     CRAWLER START WORKING     ============================')
        print('=======================================================================================')
        print('============================      Wait Paitent Please      ============================')
        print('============================               .               ============================')
        print('============================               .               ============================')
        print('============================               .               ============================')
        print('============================               .               ============================')
        print('============================               .               ============================')
        
        all_comments = []
        row = []
        
        header = self.csv_header(all_header=True)
        index_table = self.problem2index()
        
        with open('CarV4_0_1.csv', mode='w', encoding='utf-8') as carFile:
            writer = csv.writer(carFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(header)
            
            years = np.load('sub_0_1.npy')
            new_years = list(filter(lambda x: len(x)!=0, years))
            
            for year_ in new_years:
                
#               got make model year
                sp = year_[0][0].split('/')
                make = sp[1]
                model = sp[2]
                year = sp[3]
                row = [make, model, year] + [0 for i in range(20)]

                for problems in year_:
                    comment_list =[]
#                   got problem
                    problem = problems[0].split('/')[4]

                    for sub_p in problems:
            
#                       crawler got comments and save into a list
                        comments = self.get_comments(root+sub_p)
                        date = self.get_date(root+sub_p)
                        comment_list += [comments[i].text + ' ' + date[i].text for i in range(len(comments))]

#                   find row index, in order to fill data into correct col of csv  
                    index = index_table[problem]
                    row[index] = comment_list         # change value at index
                writer.writerow(row)
            
        print('============================               DONE            ============================')
    
                    
                    
                    
                    
    #################### TEST FUNCTIONS ######################
    def test(self):
        pass



# In[ ]:


######################## TEST CELL #############################
c = Crawler(root)

# c.get_head()
# c.get_title()
# c.get_body()

# c.get_makes()
# c.number_of_makes()
# c.get_make_urls(save=True)

# c.get_models('Acura')
# u = c.get_model_urls(save=False)

# c.get_years('https://www.carcomplaints.com/Audi/A4/')
# c.get_year_urls(save=True)

# c.get_problems('https://www.carcomplaints.com/Audi/A4/2006/')
# c.get_problem_urls(save=True)

# c.get_sub_problems('https://www.carcomplaints.com/Audi/Q5/2012/engine/')
# c.get_sub_problem_urls(save=True)

# c.get_comments('https://www.carcomplaints.com/Audi/A4/2009/engine/engine_and_engine_cooling.shtml')[0].text


# c.csv_header()

# c.problem2index()

c.get_all_comments()


# In[13]:


# a = np.load('sub_1.npy')
# b = np.load('sub_problems.npy')


# np.save(file='sub_0.npy', arr=a[:6810])
# np.save(file='sub_1.npy', arr=a[6810:])


# In[ ]:




