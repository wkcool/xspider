#coding=utf-8

from b2 import exceptions2 
from ..model.fileds import Fileds
from b2 import str2

__all__ = ["PageProcessor","BasePageMatchUrlProcessor","PageMatchStartUrlProcessor","PageMatchEndsUrlProcessor"]

class PageProcessor(object):
    """parse page or extract web fileds or do somthing 
    """
    def __init__(self,name = None):
        self.name = name if name else type(self).__name__ 

    def process(self , page , spider):
        raise NotImplmentError

    def match(self,page):
        return True

    def excute(self,page,spider):
        if self.match(page):
            return self.process(page,spider)


class BasePageMatchUrlProcessor(PageProcessor):
    """extract web filed by url prefix match
    """    
    
    def __init__(self,name,url_pattern,lower = True):    
        """init function
            param:name:bastring:processor name
            param:url_pattern:basestring:url prefix  
            param:lower:blooean:lower url match
            exception:ValueError:url_pattern is empty 
            exception:TypeError:url_pattern's type not basestring
            return:None
        """
        super(PageMatchStartUrlProcessor,self).__init__(name)
        if str2.isBlank(url_pattern):
            raise ValueError("url_pattern must be not empty string")
        if not isinstance(start_url_pattern,basestring):
            exceptions2.raiseTypeError(start_url_pattern)
        self.lower = lower
        self.url_pattern = url_pattern if self.lower is False else url_pattern.lower()
         
class PageMatchStartUrlProcessor(BasePageMatchUrlProcessor):
    """extract web filed by url prefix match
    """    
    
    def __init__(self,name,start_url_pattern,lower = True):    
        """init function
            param:name:bastring:processor name
            param:start_url_pattern:basestring:url prefix  
            param:lower:blooean:lower url match
            exception:ValueError:start_url_pattern is empty 
            exception:TypeError:start_url_pattern's type not basestring
            return:None
        """
        super(PageMatchStartUrlProcessor,self).__init__(name,start_url_pattern,lower)
         
    def match(self,page):
        url = page.request["url"].lower() if self.lower else page["url"] 
        return True if self.url_pattern.startswith(url) else False



class PageMatchEndsUrlProcessor(BasePageMatchUrlProcessor):
    """extract web filed by url suffix match
    """    
    
    def __init__(self,name,end_url_pattern,lower = True):    
        """init function
            param:name:bastring:processor name
            param:end_url_pattern:basestring:url suffix  
            param:lower:blooean:lower url match
            exception:ValueError:start_url_pattern is empty 
            exception:TypeError:start_url_pattern's type not basestring
            return:None
        """
        super(PageMatchStartUrlProcessor,self).__init__(name,end_url_pattern,lower)
         
    def match(self,page):
        url = page.request["url"].lower() if self.lower else page["url"] 
        return True if self.url_pattern.endswith(url) else False
