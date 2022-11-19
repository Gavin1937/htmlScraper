#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag
from .exceptions import RequestFailed


# public variable for http request
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
    'Connection': 'keep-alive',
    'Refer': 'https://www.google.com'
}

class htmlScraper:
    """
    Extract content from html content.
    
    Properties:
        url: string url
    """
    
    def __init__(self, url:str):
        self.url:str = url
    
    
    # api
    def updateUrl(self, url:str) -> None:
        """
        update self.url property.
        """
        self.url = url
    
    def getOneHtml(self, selector:str) -> Tag:
        """
        Make http get request with self.url and extract one element from received content.
        
        Parameter:
            selector: string css selector to extract one html element
        
        Returns:
            if success, return html element selected (bs4.element.Tag)
            if failed, return None
        """
        
        url = self.url
        ret:Tag = None
        try:
            res = requests.get(url, headers=HEADERS)
            if res.ok:
                soup:BeautifulSoup = BeautifulSoup(res.content.decode('utf-8'), 'lxml')
            else:
                raise RequestFailed(f'Failed to request url = {url}')
            
            ret = soup.select_one(selector)
        except Exception as e:
            raise
        
        return ret
    
    def getOneStr(self, selector:str) -> str:
        """
        Make http get request with self.url and extract text from one element from received content.
        
        Parameter:
            selector: string css selector to extract one html element
        
        Returns:
            if success, return string in the html element selected
            if failed, return None
        """
        
        url = self.url
        ret:Tag = None
        try:
            res = requests.get(url, headers=HEADERS)
            if res.ok:
                soup:BeautifulSoup = BeautifulSoup(res.content.decode('utf-8'), 'lxml')
            else:
                raise RequestFailed(f'Failed to request url = {url}')
            
            ret = soup.select_one(selector)
        except Exception as e:
            raise
        
        return ret.getText()
    
    
