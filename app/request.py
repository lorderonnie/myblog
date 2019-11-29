import urllib.request,json
from .models import Quote



get_quote_url='http://quotes.stormconsultancy.co.uk/random.json'


def get_quote():
    '''
    This gets thejson respond and allows you to access the url information
    '''
    with urllib.request.urlopen(get_quote_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)
        
        quote_results = None
        
        if get_quote_response:
            quote_results_list = get_quote_response
            quote_results = process_results(quote_results_list)
            
        
    return quote_results




def process_results(quote_list):
    '''
    This function will process the results and return them as objects
    '''    
    quote_results=[]
    
    id = quote_list.get('id')    
    author = quote_list.get('author')
    quote = quote_list.get('quote')
    
    if quote:
        quote_object = Quote(id,author,quote)
        quote_results.append(quote_object)
        
    return quote_results
    
        
        
        
        