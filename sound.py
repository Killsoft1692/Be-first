# -*- coding: utf-8 -*-

import pygame
from grab import Grab
import time
import warnings

warnings.filterwarnings('ignore')

url = 'http://mysku.ru' #target
title_old = ""
end_loop_time = time.time() + 60 * 30 # Выставляем время наблюдения(30 минут)

while time.time() < end_loop_time:
	g = Grab()
	g.go(url)
	title = g.xpath_text('//div[@class="topic-title"]')


	if title_old != title:
		print title
		print g.xpath('//div[@class="topic-title"]/a').get('href')
		title_old = title
		pygame.mixer.init()
		pygame.mixer.music.load("sniper0.wav")
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
			continue
	    	
	
	time.sleep(10) #Время между запросами