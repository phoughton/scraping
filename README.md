# An example web scraping project

## Introduction

This is a simple example of how to use [Scrapy](https://scrapy.org/) to collate data from a website and output the results in a JSON file.

## Instructions

First clone this repo. Then create and activate your python env, and install the requirements.txt 

Details on how to do that can be found here: 
- [Set up a venv environment](https://docs.python.org/3/library/venv.html)
- [Installing the packages in a requirements.txt](https://intellipaat.com/community/31672/how-to-use-requirements-txt-to-install-all-dependencies-in-a-python-project),
then `cd scraping` and run:
```
scrapy runspider medspider/spiders/medicalSpider.py -o medical_company_data.json
```
