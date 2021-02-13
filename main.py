try:
    from bs4 import BeautifulSoup
    import html5lib
    import requests 
    import validators
    from time import sleep
except ModuleNotFoundError as error:
    print(error) 
    module_name=str(error).split(' ')
    print(f'please run : pip3 install {module_name[len(module_name)-1]}')

def get_article(soup):
     try:
          
          file_name="_".join(soup.find('h1').text.split())
          with open(f'{file_name}.txt','w',encoding='utf-8') as article:
               for articles in soup.find_all('article'):
                    article.write(articles.text)  
                    article.write('\n\n')
          
          print(f'{soup.title.string}.txt created successfully....')
     except:
          print(f"something went wrong in {soup.title.string}.txt")


def get_html_page(url):

     print("Please wait ....")
     response=requests.get(url)
     print(f'Response status code {response.status_code} ,Header-type {response.headers["content-type"]} , encoding-type {response.encoding}')
     soup=BeautifulSoup(response.content,'html.parser')

     get_article(soup)

#url validatioin
def url_validation(valid_url):

     if validators.url(valid_url):
          return True 
     else:
          print(f"Invalid url found : {valid_url}")


def main():

     number_of_urls=int(input("Enter a number of url :"))
     urls=[]
     for _ in range(number_of_urls):
     
          while True:
               url=str(input("Enter a url :").strip())
               if url is not None or url !="":
                    if url_validation(url):
                         urls.append(url)
                         break
               else:
                    continue

     for url in urls:
          get_html_page(url)
          sleep(3)

    

if __name__=="__main__":
     main()