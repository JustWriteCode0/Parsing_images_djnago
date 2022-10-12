import os
from bs4 import BeautifulSoup
import lxml
from pathlib import Path
import requests
from .models import Url


class scraping:
    def get_images(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
        # используем последнюю запись(ссылку на страницу) из бызы данных

        model = Url.objects.all().order_by('-id')[:1]
        for clear_link in model:
            url = clear_link
            response = requests.get(url, stream=True, headers=headers).content
            soup = BeautifulSoup(response, 'lxml')
        try:
            # получем все обьекты img и все обьекты src из img
            image_link = [x['src'] for x in soup.find_all('img')]
            if image_link == None:
                return 'Извините мы не смогли получить изображения с этой страницы'
            else:
                return image_link
        except KeyError:
            return 'Извините мы не смогли получить изображения с этой страницы'
