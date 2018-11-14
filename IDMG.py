from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import scrapy
import pandas as pd

with open('codigos.txt') as arquivo:
	arquivo = arquivo.readlines()

escreve = open('resultados.txt', 'w')

chrome_options = Options()
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)
driver.get('http://consultasintegra.fazenda.mg.gov.br/sintegra/')

i = 0;

for cod in arquivo:
	# seleciona o Tipo de Identificação Número Inscrição
	time.sleep(1)
	menu = driver.find_element_by_xpath("""//*[@id="containerConteudoPrincipal"]/div/form/div/table[2]/tbody/tr[2]/td[2]/div/div[1]""")
	menu.click()

	time.sleep(1)
	opcao = driver.find_element_by_xpath("""//*[@id="containerConteudoPrincipal"]/div/form/div/table[2]/tbody/tr[2]/td[2]/div/div[2]/span[2]""")
	opcao.click()

	# escreve no elemento Identificação
	time.sleep(1)
	input_doc = driver.find_element_by_xpath("""//*[@name="filtro"]""")
	input_doc.send_keys(cod)

	# faz a pesquisa
	time.sleep(1)
	pesquisar = driver.find_element_by_xpath("""//*[@id="containerConteudoPrincipal"]/div/form/div/table[2]/tbody/tr[5]/td[2]/a/img""")
	pesquisar.click()

	# pega o documento 
	documento = driver.find_element_by_xpath("""//*[@id="cnpj.identificacaoFormatada"]""")
	escreve.write(documento.text + "\n")
	i = i + 1;
	print(i)

	# voltar a pagina e refazer o processo até o fim dos códigos
	voltar = driver.find_element_by_xpath("""//*[@id="containerConteudoPrincipal"]/div/form[3]/a/img""")
	voltar.click()

escreve.close()
