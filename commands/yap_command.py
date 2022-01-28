import requests
import discord
import random
import bs4


def embed_return(question):
    url = f'https://yandex.ru/images/search?text={question}&isize=large'
    data = requests.get(url)
    soup = bs4.BeautifulSoup(data.text, 'html.parser')
    img = soup.findAll('img')
    try:
        url = img[random.randint(2, len(img) - 1)].get('src')

        embed_obj = discord.Embed(title='Yandex Images', description=f'Image for {question}')
        embed_obj.set_image(url=f'http:{url}')
    except IndexError:
        embed_obj = discord.Embed(title='Yandex Images', description='Nothing not found!')
    return embed_obj
