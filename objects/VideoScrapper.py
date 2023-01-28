import json
import requests

from os.path import exists
from urllib.request import urlopen, Request, urlretrieve
from bs4 import BeautifulSoup as soup
from config import *
from objects.Logs import Logs as log

class VideoScrapper:

    BASE_URL_3P = 'http://dinamics.ccma.cat/pvideo/media.jsp?media=video&version=0s&idint='
    BASE_URL_TV3 = 'https://www.ccma.cat'
    URL_TV3_PATH = '/tv3/el-cor-de-la-ciutat/capitols/?pagina='
    HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}

    last_v_page = -1
    last_v_ix = -1

    def __init__(self):

        page = requests.get(VideoScrapper.BASE_URL_TV3, headers=self.HEADERS)
        if page.status_code != 200:
            log.error("VideoScrapper (" + VideoScrapper.BASE_URL_TV3 + ' is down.)')
            quit()

        page = requests.get(VideoScrapper.BASE_URL_3P, headers=self.HEADERS)
        if page.status_code != 400:
            log.error("VideoScrapper (" + VideoScrapper.BASE_URL_3P + ' is down.)')
            quit()

        file = open(CONF_PATH_FILE_IX, "r")
        f_cont = file.read().split('\n')
        file.close()

        self.last_v_page = int(f_cont[0])
        self.last_v_ix = int(f_cont[1])

        if self.last_v_page > CONF_IX_FIRST_PAGE:
            self.last_v_page = CONF_IX_FIRST_PAGE

    def save_video(self, save_prod=True):

        save_path = CONF_PATH_FOLDER_VIDEOS + CONF_NAME_VIDEO

        url_3p = self.get_video_3p_url()

        if url_3p == '':
            log.msg('save_video (Cant retrieve url to download)')
            quit()

        log.msg("save_video (Downloading: " + url_3p + ")")

        if save_prod:
            urlretrieve(url_3p, save_path); 
            if exists(save_path) != True:
                log.error('save_video (The video hasnt download)')
                quit()

        log.msg('save_video (Saved)')

        return CONF_PATH_FOLDER_VIDEOS + CONF_NAME_VIDEO

    def scrap(self, url):
        req = Request(url, None, VideoScrapper.HEADERS)
        resp = urlopen(req)
        r_text = resp.read()

        return soup(r_text, 'html.parser')

    def get_video_url(self):

        last_page = self.last_v_page
        last_ix = self.last_v_ix

        url = VideoScrapper.BASE_URL_TV3 + VideoScrapper.URL_TV3_PATH + str(last_page)
        s_text = self.scrap(url)

        divs = s_text.find_all(class_='F-llistat-item')

        # --- ⚠ Página finalizada, leemos la actual y modifico valores para editar fichero
        if last_ix == 0:
            self.last_v_ix = CONF_IX_FIRST_VIDEO # Último elemento página nueva
            self.last_v_page = last_page - 1 # Página nueva anterior a la actual

        if last_ix == CONF_IX_FIRST_VIDEO:
            last_ix = len(divs) - 1 # Nueva página, leemos el último elemento (los elementos vienen ordenador DESC)
            self.last_v_ix = last_ix - 1
        else:
            self.last_v_ix = last_ix - 1
        # --- End IX treatment
        

        try:
            div = divs[last_ix]
        except:
            log.error('get_video_url (No index)\nLast page: ' + str(last_page) + "\nLast index: " + str(last_ix) + "\nURL: " + url)
            return ''

        try:
            rel_path = div.find('a', href=True)['href'].strip()
        except:
            log.error('get_video_url (No href)')
            return ''

        return VideoScrapper.BASE_URL_TV3 + rel_path

    def get_video_3p_url(self):

        # https://videostv3.vercel.app/
        # https://videostv3.vercel.app/video/1490589
        # div.links > a.jsx-58affef38ee63c26

        url = self.get_video_url()
        url_query = url.split('/')

        video_id = ''
        try:
            video_id = url_query[len(url_query) - 1]
            if video_id == '':
                video_id = url_query[len(url_query) - 2]
            
        except:
            log.error('get_video_3p_url (Cant find video ID - Wrong index)')
            return ''

        if video_id == '':
            log.error('get_video_3p_url (Cant find video ID - Empty)')
            return ''

        url = VideoScrapper.BASE_URL_3P + video_id
        log.msg('get_video_3p_url (Calling: '+url+')')
        req = Request(url, None, VideoScrapper.HEADERS)
        resp = urlopen(req)
        print(resp)
        resp_raw = resp.read().decode('UTF-8')
        # log.msg('get_video_3p_url (response: )')
        # log.msg(resp_raw)
        r_json = json.loads(resp_raw)

        try:
            urls = r_json['media']['url']
            log.msg("get_video_3p_url (Videos retrieved)")
            log.msg(urls)
            
        except:
            log.error('get_video_3p_url (Cant find any video URLs)')
            return ''

        # --- Guardo metadatos
        try:
            title = r_json['informacio']['titol']
            durada = r_json['informacio']['durada']['text']
            dataemisio = r_json['informacio']['data_emissio']['text'].split()
            metatitle = "El cor de la ciutat"
            hashtags = "#tv3 #elcor #elcordelaciutat #ecdlc"

            file = open(CONF_PATH_FILE_CURRENT_VIDEO_META, "w")
            file.write(metatitle + "\n" + title + "\nDurada: " + durada + " - Emissio: " + dataemisio[0] + "\n" + hashtags)
            file.close()

            log.msg("get_video_3p_url (Metadata saved)")

        except:
            log.error('get_video_3p_url (Cant retrieve metadata)')
        # ---

        url_out = ''
        for urldic in urls:

            if url_out != '':
                pass

            # try:
            url_video = urldic['file']

            log.msg("get_video_3p_url (Try get: "+url_video+")")

            reqbar = Request(url_video, None, VideoScrapper.HEADERS)
            resfoo = urlopen(reqbar)

            if resfoo.status == 200:
                url_out = url_video

                file = open(CONF_PATH_FILE_VIDEO_URLS, "a")
                file.write(url_out + "\n")
                file.close()

                return url_out

            else:
                log.error('get_video_3p_url (Cant retrieve video URL='+url_video+' in 10)')

            # except:
            #     log.error(urldic)
            #     log.error('get_video_3p_url (Cant get `file` from urldic)')
            #     pass

        return url_out

    def delete_old():
        return

    def update_file(self):
        file = open(CONF_PATH_FILE_IX, "w")
        # last_v_page y last_v_ix SE MODIFICAN en ⚠ get_video_url
        str_2_upd = str(self.last_v_page) + "\n" + str(self.last_v_ix)
        file.write(str_2_upd)
        file.close()

        log.msg("update_file {\n" + str_2_upd + "\n}");

        return True