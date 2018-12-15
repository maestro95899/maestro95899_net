Это есть вики-краулер (программа, обходящая заданный сегмент интернета по ссылкам),
 который должен обойти статьи википедии (по умолчанию румынской),
  достижимые со [стартовой страницы](по умолчанию http://rmy.wikipedia.org).
Для каждой найденной статьи посчитанны её удалённость от главной страницы.
 Удалённость стартовой страницы равна 0. Если на страницу можно попасть разными способами, будем брать
  кратчайшее расстояние.
* Служебные ссылки и ссылки на несуществующие страницы не входят в ответ.
* Для скачивания странички пользуемся библиотекой `requests`, для парсинга html – `BeautifulSoup`.
* Всего статей примерно 300(в румынской), работать кроулер должен совсем не долго.
* запускать для любой другой вики без ограничения на максимальный уровень глубины равный <= 2 не рекомендуется
* в случае отказа доступа к сайту, краулер пытается использовать Proxy (осторожно, не стоит запускать с максимальным уровенем глубины равный > 1)
чтобы запустить краулер:
```json
>python crawler.py
```

чтобы запустить краулер с дополнительными параметрами:
```json
>python crawler.py adress lang max_deepth
```
где adress определяет стартовую страницу, lang определяет язык вики по которой мы ищем и max_deepth определяет максимальную глубину поиска

например:
```json
>python crawler.py https://rmy.wikipedia.org/wiki/Sherutni_patrin rmy 2
```



пример результата работы:
```json
{'Sherutni_patrin': 0, 'Vikipidiya': 1, 'Lekh': 1, 'Romane_manusha': 1, 'Romani_chib': 1, 'Standardizuimi_Romani_chib': 1, 'Romano_lekhipen': 1, 'Chiba_le_romenge': 1, 'Patrinipen_le_bare_Romengo': 1, 'Romano_siklyaripen': 1, 'Kale': 1, 'Sinti': 1, 'Poraimos': 1, 'Pativ': 1, 'Desi': 1, 'Banjara': 1, 'Devnagrī': 1, 'Chexanipen': 1, 'Phuvipen': 1, 'Sikavdimos': 1, 'Compyutereske_janglimata': 1, 'Chhibavipen': 1, 'Jivaniakohramovipen': 1, 'Mesto_software': 2, 'Sel': 2, 'Sudutni_Asiya': 2, 'Pakistan': 2, 'Bharat': 2, 'Mashkarutne_Indo-Ariyane_chhiba': 2, 'Shuto_Orizari': 2, 'Republika_Makedoniya': 2, 'Gav': 2, 'Foro': 2, 'Budeshti': 2, 'Chhib': 2, 'Chave': 2, 'Rekshan': 2, 'Them': 2, 'Jermaniya': 2, 'Bari_Britaniya': 2, 'Spaniya': 2, 'Norvejiya': 2, 'Valshenengi_Romani_chhib': 2, 'Standardizuyimi_Romani_qhib_(Selahetin_Kruezi)': 2, 'Bulgariya': 2, 'Rusiya': 2, 'Rumuniya': 2, 'Chexiya': 2, 'Ungariya': 2, 'Nicolaye_Gyorge': 2, 'Viktoriya_Mohaci': 2, 'Liviya_Yaroka': 2, 'Cedomir_Yovanovic': 2, 'Shtefan_Răzvan': 2, 'Yanosh_Bogdan': 2, 'Raiko_Juric': 2, 'Deliya_Grigore': 2, 'Selahetin_Kruezi': 2, 'Ronald_Lee': 2, 'Mateo_Maximov': 2, 'Hedina_Sijercic': 2, 'Katarina_Taikon': 2, 'Vasile_Yonesko': 2, 'Grigorash_Diniku': 2, 'Django_Reinhardt': 2, 'Yon_Voiku': 2, 'Romika_Puchanu': 2, 'Esma_Rejepova': 2, 'Azis': 2, 'Sandro': 2, 'Shaban_Bayramovic': 2, 'Reyhan': 2, 'Sofi_Marinova': 2, 'Vali_Vizheliye': 2, 'Adriyan_Minune': 2, 'Zvonko_Demirovic': 2, 'Fazliya': 2, 'Haso_Menovin_Frohlish': 2, 'Zhean_Konstantin': 2, 'Shtefan_Bǎnikǎ': 2, 'Xoakin_Kortes': 2, 'Valery_Novoselsky': 2, 'Johann_Trollmann': 2, 'Rosa_Taikon': 2, 'Sikingro%27Kher': 2, 'Europa': 2, 'Romano_siklyaripen_la_Rumuniyatar': 2, 'Romano_siklyaripen_le_Slovaikostar': 2, 'Romano_siklyaripen_la_Ungariyatar': 2, 'Franchiya': 2, 'Portugaliya': 2, 'Indo-Europikane_chhiba': 2, 'Kontinento': 2, 'Andalusiya': 2, 'Kalo': 2, 'Shelbersh': 2, 'Italiya': 2, 'Transilvaniya': 2, 'Slovaiko': 2, 'Manush': 2, 'Nasho': 2, 'Phuv': 2, 'Nordutni_Amerika': 2, 'ABCD': 2, 'Seloro': 2, 'Jegeya': 2, 'Chexay': 2, 'Shiyaron': 2, 'Samodor': 2, 'Phuvipnaske_patrinimata': 2, 'Chhibavipnaski_familiya': 2}
```


