# Movie Review Scraper

> movie review scraper to generate data for natural language processing

---

### Table of Contents
- [Description](#description)
- [How To Use](#how-to-use)
- [Author Info](#author-info)

---

## Description

Collecting data in the form of sentences can be useful for many applications including sentiment analysis using NLP or for a simple classification model. Gathering such data can often be a tedious and frustrating task. This project will help you generate the required data by performing a few simple steps.

#### Requirements

- python
- scrapy python package

---

## How To Use




#### Installing scrapy

```bash
   pip install scrapy
```
This project was created on Scrapy 2.5.0, but any subsequent versions will also work.

#### Setting up the project
You will first need to go to the rotten tomatoes website and search for the movie whose reviews you want. Then proceed to the critic or audience reviews and click on view all. The link in your browser will act as the starting point for the crawler. Copy this link and navigate to Scrapy Web Crawler/crawler/crawler/spiders/review\_spider.py. Paste the copied link in the start\_urls list and also in the next\_page variable below.

#### Running the project
To crawl the reviews and store them in a csv file, we simply have to navigate to the project in our command line terminal and write
```bash
   scrapy crawl reviews -o reviews.csv
```
Here, you can replace reviews.csv with any filename of your choice. The crawler will crawl and store the first 500 reviews of the movie. This can be changed by navigating to the reviews\_spider.py file as shown above and changing the number of pages from 25 to the required amount.

---

## Author Info

- Instagram - [@AnishMulay](https://www.instagram.com/_Anish_Mulay_/)
- Email - f20180907@goa.bits-pilani.ac.in
