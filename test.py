try:
    from bs4 import BeautifulSoup
    import html5lib
    import requests 
    import validators
    import os
except ModuleNotFoundError as error:
    print(error) 
    module_name=str(error).split(' ')
    print(f'please run : pip3 install {module_name[len(module_name)-1]}')

def get_article(soup):
     try:
          with open('article.txt','w',encoding='utf-8') as article:
               for articles in soup.find_all('article'):
                    article.write(articles.text)  
                    article.write('\n\n')
          
          print("article.txt created successfully")
     except:
          print("something went wrong in artile.txt")

def get_all_html_text(soup):
     try:
          with open('html_text.txt','w',encoding='utf-8') as text:
               text.write(soup.get_text())
          print("file creadted successfully")
     except:
          print("something went wrong")

def get_all_headings(soup):
     try:
          with open('headings.txt','w',encoding='utf-8') as headings:

               headings.write('H1 type headings'.center(40,'*'))
               headings.write('\n')
               for heading in soup.find_all('h1'):
                    headings.write(heading.text)
                    headings.write('\n')

               headings.write('\n\n')
              
               headings.write(' H2 type headings'.center(40,'*'))
               headings.write('\n')
               for heading in soup.find_all('h2'):
                    headings.write(heading.text)
                    headings.write('\n')

               headings.write('\n\n')
              
               headings.write(' H3 type headings'.center(40,'*'))
               headings.write('\n')
               for heading in soup.find_all('h3'):
                    headings.write(heading.text)
                    headings.write('\n')
               
               headings.write('\n\n')

               headings.write(' H4 type headings'.center(40,'*'))
               headings.write('\n')
               for heading in soup.find_all('h4'):
                    headings.write(heading.text)
                    headings.write('\n')

               headings.write('\n\n')

               headings.write(' H5 type headings'.center(40,'*'))
               headings.write('\n')
               for heading in soup.find_all('h5'):
                    headings.write(heading.text)
                    headings.write('\n')

               headings.write('\n\n')

               headings.write(' H6 type headings'.center(40,'*'))
               headings.write('\n')
               for heading in soup.find_all('h6'):
                    headings.write(heading.text)
                    headings.write('\n')
          print('heading.txt created successfully')
     except:
          print("something went wrong on heading")

def get_all_paragraphs(soup):
     
     try:
          with open('paragraph.txt','w',encoding='utf-8') as p:
              
               for para in soup.find_all('p'):
                    #print(para.text)
                    p.write(para.text)
                    p.write('\n')
                    p.write('\n')

          print('paragraph,.txt created successfully...')
     except:
          print("error in file opening and reading... ")

#get all links
def get_all_links(soup):

     try:
          with open('links.txt','w',encoding = 'utf-8') as a:
              
               for link in soup.find_all('a'):
                    if url_validation(link.get('href')):
                         a.write(link.get('href'))
                         a.write('\n')
                        
          print('links.txt created successfully')
     except:
          print("error in file opening and reading... ")
   

def get_html_page(url):

     print("Please wait ....")
     response=requests.get(url)
     print(f'Response status code {response.status_code} ,Header-type {response.headers["content-type"]} , encoding-type {response.encoding}')
     soup=BeautifulSoup(response.content,'html.parser')

     if soup.title.string in os.listdir():
          os.chdir(soup.title.string)
     else:
          os.mkdir(soup.title.string)
          os.chdir(soup.title.string)
     

     get_all_html_text(soup)
     get_all_links(soup)
     get_all_paragraphs(soup)
     get_all_headings(soup)
     get_article(soup)

#url validatioin
def url_validation(valid_url):

     if validators.url(valid_url):
          return True 
     else:
          print(f"Invalid url found : {valid_url}")

def main():
     urls=""
     while True:
          urls=str(input("Enter a url :").strip())
          if urls is not None or urls !="":
               if url_validation(urls):
                    break
          else:
               continue

     print(urls)
     get_html_page(urls)

    

if __name__=="__main__":
     main()