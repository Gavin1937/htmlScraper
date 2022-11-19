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
        encoding: string encoding of html content
    """
    
    def __init__(self, url:str, encoding:str='utf-8'):
        self.url:str = url
        self.encoding:str = encoding
    
    
    # api
    def updateUrl(self, url:str) -> None:
        """
        update self.url property.
        """
        self.url:str = url
    
    def updateEncoding(self, encoding:str) -> None:
        """
        update self.encoding property.
        """
        self.encoding:str = encoding
    
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
                soup:BeautifulSoup = BeautifulSoup(res.content.decode(self.encoding), 'lxml')
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
                soup:BeautifulSoup = BeautifulSoup(res.content.decode(self.encoding), 'lxml')
            else:
                raise RequestFailed(f'Failed to request url = {url}')
            
            ret = soup.select_one(selector)
        except Exception as e:
            raise
        
        return ret.getText()
    
    def getAllHtml(self, selector:str, next:str=None, nextAttr:str='href') -> Tag:
        """
        Make http get request with self.url and extract all elements from received html content.
        
        Parameter:
            selector: string css selector to extract multiple html elements
            next: string css selector to select element contains url to next page. (can be None, default None)
            nextAttr: string html attribute of "next" html element. (default "href")
        
        Returns:
            if success, return list of html elements selected (list[bs4.ResultSet[bs4.element.Tag]])
            if failed, return None
        """
        
        url = self.url
        ret:list = []
        try:
            while url is not None and len(url) > 0:
                res = requests.get(url, headers=HEADERS)
                if res.ok:
                    soup:BeautifulSoup = BeautifulSoup(res.content.decode(self.encoding), 'lxml')
                else:
                    return None
                
                ret += [s for s in soup.select(selector)]
                if next is not None:
                    url = soup.select_one(next)
                else:
                    url = None
                if url is None:
                    break
                url = url.get(nextAttr)
        except Exception as e:
            raise
        
        return ret
    
    def getAllStr(self, selector:str, next:str, nextAttr:str='href') -> Tag:
        """
        Make http get request with self.url and extract text of all elements from received html content.
        
        Parameter:
            selector: string css selector to extract multiple html elements
            next: string css selector to select element contains url to next page
            nextAttr: string html attribute of "next" html element. (default "href")
        
        Returns:
            if success, return list of text selected (list[list[str]])
            if failed, return None
        """
        
        url = self.url
        ret:list = []
        try:
            while url is not None and len(url) > 0:
                res = requests.get(url, headers=HEADERS)
                if res.ok:
                    soup:BeautifulSoup = BeautifulSoup(res.content.decode(self.encoding), 'lxml')
                else:
                    return None
                
                ret += [s.getText() for s in soup.select(selector)]
                if next is not None:
                    url = soup.select_one(next)
                else:
                    url = None
                if url is None:
                    break
                url = url.get(nextAttr)
        except Exception as e:
            raise
        
        return ret
    
