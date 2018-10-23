# -*- coding: utf-8 -*-

print "SSSSSSSSSSSSSSSSSSUCKING EVERYTHING IN SSSSSSSSSSSIGHT                  "
print "                                                                        "
print "              \                                                         "
print "               \                                                        "
print "                   /^\/^\                                               "
print "                 _|__|  O|                                              "
print "        \/     /~     \_/ \                                             "
print "         \____|__________/  \                                           "
print "                \_______      \                                         "
print "                        `\     \                 \                      "
print "                          |     |                  \                    "
print "                         /      /                    \                  "
print "                        /     /                       \\                "
print "                      /      /                         \ \              "
print "                     /     /                            \  \            "
print "                   /     /             _----_            \   \          "
print "                  /     /           _-~      ~-_         |   |          "
print "                 (      (        _-~    _--_    ~-_     _/   |          "
print "                  \      ~-____-~    _-~    ~-_    ~-_-~    /           "
print "                    ~-_           _-~          ~-_       _-~   - andy -"
print "                       ~--______-~                ~-___-~               "

             
from bs4 import BeautifulSoup

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import requests

page = requests.get("https://www.globohq.com/dashboard/index")


import time
import datetime

import json

soup = BeautifulSoup(page.content, 'html.parser')

# http://dl.dropbox.com/u/49962071/blog/python/resource/bs_sample3.html

# soup = BeautifulSoup(html_content) # making soap

# for c in soup.find_all('.in-call-indicator-message'):

# print c




i=0

while True:


	_usuarios = requests.get('http://142.93.249.250:8000/listausuarios')


	print json.loads(_usuarios.text)

	for u in json.loads(_usuarios.text):

		usuario = u['nombre']

		contrasena= u['password']

		driver = webdriver.Chrome('/Users/xiencias/Downloads/chromedriver')

		driver.get('https://www.globohq.com/users/sign_in');

		username = driver.find_element_by_id("user_email")

		password = driver.find_element_by_id("user_password")

		username.click();

		time.sleep(1)

		username.send_keys(usuario)

		password.click();

		print 'contrasena,,,',contrasena

		password.send_keys(contrasena)


		driver.find_element_by_name("commit").click();

		estado = driver.find_element_by_class_name('in-call-indicator-message')

		print usuario,estado.text,datetime.datetime.today()

		requests.get('http://142.93.249.250:8000/guarda/?usuario='+str(usuario)+'&estado='+str(estado.text))

		driver.close()

		pass

#password.send_keys("Pa55worD")

#driver.find_element_by_name("submit").click()

#driver.findElement(By.id("user_email")).sendKeys("555-55-5555"); 

# elem = driver.find_element_by_partial_link_text('Mostrar n')

# elem.click()

# elem = driver.find_element_by_class_name('number')

# number = elem.text

#driver.close()