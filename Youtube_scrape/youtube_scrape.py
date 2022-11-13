import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from Webdriver_options import Webdriver_options
import time


class Youtube:

    def __init__(self, youtube_owner: str, channel_type: str):
        self.driver = webdriver.Chrome(executable_path=Webdriver_options.chromedriver_path(),
                                       options=Webdriver_options.configuration())
        self.youtube_owner = youtube_owner
        if channel_type == 'c':
            self.url = f'https://www.youtube.com/c/{youtube_owner}/videos'
        else:
            self.url = f'https://www.youtube.com/channel/{youtube_owner}/videos'
        self.videos_info = []

    def get_data(self):
        self.driver.get(self.url)

        self.youtube_owner = self.driver.find_element(By.XPATH, '//*[@id="text"]').text
        popular_button = self.driver.find_element(By.XPATH, '//*[@id="chips"]/yt-chip-cloud-chip-renderer[2]')
        popular_button.click()
        time.sleep(2)
        while True:
            scroll_height = 2000
            document_height_before = self.driver.execute_script("return document.documentElement.scrollHeight")
            self.driver.execute_script(f"window.scrollTo(0, {document_height_before + scroll_height});")
            time.sleep(2)
            document_height_after = self.driver.execute_script("return document.documentElement.scrollHeight")
            if document_height_after == document_height_before:
                break

        all_videos = self.driver.find_elements(By.ID, 'details')

        for video in all_videos[:-1]:
            title = video.find_element(By.ID, 'video-title-link').text
            views = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[1]').text.strip().replace('&nbsp', '')
            when = video.find_element(By.XPATH, './/*[@id="metadata-line"]/span[2]').text
            self.videos_info.append({
                'title': title,
                'views': views,
                'when': when
            })

        self.driver.close()

        return self.videos_info

    def save_to_scv(self):
        df = pd.DataFrame(self.videos_info)
        df.to_csv(f'{self.youtube_owner}.csv', index=False)
        print('Saved to csv')


def main():
    channel_type = str(input('Write channel type: "c" or "channel "'))
    youtube_owner = str(input('Write name of youtube channel '))
    youtube_page = Youtube(youtube_owner, channel_type)
    youtube_page.get_data()
    youtube_page.save_to_scv()


if __name__ == '__main__':
    main()
