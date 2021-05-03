import requests
from bs4 import BeautifulSoup
import smtplib


URL = 'https://www.amazon.com/AbergBest-Rechargeable-Digital-Students-cameras/dp/B078YR3MNK/ref=sxin_5?asc_contentid=amzn1.osa.45c1331f-748b-41f9-bc72-a2a4a0470b9b.ATVPDKIKX0DER.en_US&asc_contenttype=article&ascsubtag=amzn1.osa.45c1331f-748b-41f9-bc72-a2a4a0470b9b.ATVPDKIKX0DER.en_US&creativeASIN=B078YR3MNK&cv_ct_cx=camera&cv_ct_id=amzn1.osa.45c1331f-748b-41f9-bc72-a2a4a0470b9b.ATVPDKIKX0DER.en_US&cv_ct_pg=search&cv_ct_we=asin&cv_ct_wn=osp-single-source-pecos-desktop&dchild=1&keywords=camera&linkCode=oas&pd_rd_i=B078YR3MNK&pd_rd_r=dd0ddcf6-e74d-425d-955b-67f07f5fa595&pd_rd_w=trJms&pd_rd_wg=W4fEF&pf_rd_p=9ca0c43d-5b2f-4d08-be2c-4bf20950d3e4&pf_rd_r=0TM33W9J6ZZS8YJZ2DQH&qid=1620071950&sr=1-1-c26ac7f6-b43f-4741-a772-17cad7536576&tag=geekcontent-20'
headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
def find_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.prettify())

    title = soup.find(id="priceblock_dealprice").get_text()
    converted_price = price = flaot(price[0:5])

    if(converted_price < 1.700):
        send_mail()
    print(converted_price)
    print(title)

   
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.startls()
    server.ehlo()
    
    server.login('tabualhsan@gmail.com', )

    subject = 'price fell down'

    body = "check the amazon link https://www.amazon.com/AbergBest-Rechargeable-Digital-Students-cameras/dp/B078YR3MNK/ref=sxin_5?asc_contentid=amzn1.osa.45c1331f-748b-41f9-bc72-a2a4a0470b9b.ATVPDKIKX0DER.en_US&asc_contenttype=article&ascsubtag=amzn1.osa.45c1331f-748b-41f9-bc72-a2a4a0470b9b.ATVPDKIKX0DER.en_US&creativeASIN=B078YR3MNK&cv_ct_cx=camera&cv_ct_id=amzn1.osa.45c1331f-748b-41f9-bc72-a2a4a0470b9b.ATVPDKIKX0DER.en_US&cv_ct_pg=search&cv_ct_we=asin&cv_ct_wn=osp-single-source-pecos-desktop&dchild=1&keywords=camera&linkCode=oas&pd_rd_i=B078YR3MNK&pd_rd_r=dd0ddcf6-e74d-425d-955b-67f07f5fa595&pd_rd_w=trJms&pd_rd_wg=W4fEF&pf_rd_p=9ca0c43d-5b2f-4d08-be2c-4bf20950d3e4&pf_rd_r=0TM33W9J6ZZS8YJZ2DQH&qid=1620071950&sr=1-1-c26ac7f6-b43f-4741-a772-17cad7536576&tag=geekcontent-20"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'tabualhsan@gmail.com',
         msg
    )

    print('Hey the email has been sent!')

find_price()