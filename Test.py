import pandas
import numpy
import matplotlib.pyplot as pyplot
import seaborn

import os

import requests
import requests_html
import bs4



def getBlogsData(blog_pages_urls:list)->pandas.DataFrame:
    """_summary_

    Args:
        blog_pages_urls (list): list of links of blogs

    Returns:
        pandas.DataFrame: requested blogs data in DataFrame
    """
    blogs_urls=[]
    blog_titles=[]
    blog_posting_timestamp=[]
    blog_contents=[]
    for blog_pages_url in blog_pages_urls:
        request=session.get(blog_pages_url)
        content=bs4.BeautifulSoup(request.result().content)
        blog_links=content.find_all("a",class_="dib-post")
        for link in blog_links:
            blogs_urls.append(link['href'])
    for blogs_url in blogs_urls:
        request=session.get(blogs_url)
        content=bs4.BeautifulSoup(request.result().content)
        title=content.find_all("h1",class_="dib-post-title")[0]
        blog_titles.append(title.text.strip())
        posting_timestamp=content.find_all("span",class_="dib-post-date")[0]
        blog_posting_timestamp.append(posting_timestamp.text.strip())
        description=[]
        descriptions=content.find_all(class_="dib-post-content")[0]
        for element in description.find_alll():
            if element.name in ["h1","h2","h3"]:
                break
            elif element.name in ["p","strong"]:
                description.append(element.text.strip())
        blog_contents.append(" ".join(description))
    Blog_Data=pandas.DataFrame()
    Blog_Data['name']=blog_titles
    Blog_Data['posting_timestamp']=blog_posting_timestamp
    Blog_Data['content']=blog_contents
    Blog_Data['url']=blogs_urls
    return Blog_Data



def getProductsData(initial_url:str,limit=1)->pandas.DataFrame:
    """_summary_

    Args:
        initial_url (str): initial common url
        limit (int, optional): number of pages to be traversed. Defaults to 1.

    Returns:
        pandas.DataFrame: requested products data in DataFrame
    """
    products_page_urls=[]
    for page_index in range(limit):
        products_page_url=initial_url+str(page_index+1)
        products_page_urls.append(products_page_url)
    products_pages=[]
    for products_page in products_page_urls:
        browser.get(products_page)
        html = browser.page_source
        content = BeautifulSoup(html, 'lxml')
        product_links=content.find_all("a",class_="snize-view-link")
        for product_link in product_links:
            products_pages.append("https://himalayawellness.in"+product_link["href"])
    titles=[]
    prices=[]
    descriptions=[]
    for product_page in products_pages:
        print(product_page)
        try:
            request=requests.get(product_page)
            content=bs4.BeautifulSoup(request.content)
            title=content.find_all("h1",class_="pt-title")[0]
            price=content.find_all("span",class_="new-price")[0]
            description =content.find_all("div",class_="pt-layout-text")[0]
            titles.append(title.text.strip())
            prices.append(price.text.strip())
            descriptions.append(description.text.strip())
        except Exception as e:
            print(e)
    Products_Data=pandas.DataFrame()
    Products_Data['title']=titles
    Products_Data['price']=prices
    Products_Data['description']=descriptions
    return Products_Data