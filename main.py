from selenium import webdriver
from pytube import YouTube
import urllib.request
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)

video_id = "VIDEO_ID"
url = f"https://www.youtube.com/watch?v={video_id}"
driver.get(url)

yt = YouTube(url)
video_url = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().url

title = yt.title.replace('|','').replace(':','').replace('/','').replace('\\','').replace('?','').replace('*','').replace('<','').replace('>','').replace('"','').replace('.','')
file_name = os.path.join('videos', f"{title}.mp4")
urllib.request.urlretrieve(video_url, file_name)

driver.quit()
