import  re

def domain_name(url:str)->str:
    pattern = re.compile(r'(https?://|www\.)?(www\.)?([a-z0-9-]+)(\..+)?')
    sub_url = pattern.sub(r'\3',url)
    return sub_url

  def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
