# An example web scraping project

## Introduction

This is a simple example of how to use [Scrapy](https://scrapy.org/) to collate data from a website and output the results in a JSON file.

## Instructions

First clone this repo. Then create and activate your python env from the requirements.txt (https://docs.python.org/3/library/venv.html),
then `cd scraping` and run:
```
scrapy runspider medspider/spiders/medicalSpider.py -o medical_company_data.json
```
