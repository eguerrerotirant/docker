# coding=utf-8
from bs4 import BeautifulSoup
import dryscrape
import json
import time
import sys



all_links = {}
REMAINING = True
if 'linux' in sys.platform:
    # start xvfb in case no X is running. Make sure xvfb
    # is installed, otherwise this won't work!
    dryscrape.start_xvfb()

base_url = 'https://www.dt.gob.cl/legislacion/1624/w3-channel.html'

sess = dryscrape.Session()


headers = {
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Sec-Fetch-User': '?1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Referer': 'https://www.dt.gob.cl/legislacion/1624/w3-channel.html',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'es-ES,es;q=0.9',
}
# sess.set_header(headers)

# if self.full:
#     params = (
#         ('_q', 'rango1_pnid_2294=2019-01-01&rango2_pnid_2294=2019-06-28'),
#     )

params = (
    ('_q', 'rango1_pnid_2294=2019-01-01&rango2_pnid_2294=2019-06-28'),
)

sess.visit(base_url)

sess.visit('https://www.dt.gob.cl/legislacion/1624/w3-search.php?_q=rango1_pnid_2294%3D2019-01-01%26rango2_pnid_2294%3D2019-06-28')

time.sleep(5)

soup_ini = BeautifulSoup(sess.body(), "lxml")

# if self.debug:
# print ('============== soup_ini 2===============')
# print (soup_ini)
# print ('============== FF soup_ini 2===============')

form = sess.at_xpath('//*[@id="BusquedaAvanzada"]')

desde = sess.at_xpath('//*[@id="rango1_pnid_2294_796"]')
desde.set('2019-01-01')
desde.set_attr('value', '2019-01-01')
desde.exec_script('javascript:BusquedaAvanzadaEvent(this.form);')

hasta = sess.at_xpath('//*[@id="rango2_pnid_2294_796"]')
hasta.set('2019-06-28')
hasta.set_attr('value', '2019-06-28')
hasta.exec_script('javascript:BusquedaAvanzadaEvent(this.form);')

buscar = sess.at_xpath('//*[@id="enviar_796"]')
#buscar.exec_script("javascript:return BusquedaAvanzada17019Submit(this.form, 'submit')")
buscar.click()
# buscar.form().submit()
time.sleep(20)

source = sess.body()

soup_ini = BeautifulSoup(source, "lxml")

# if self.debug:
print ('============== soup_ini 2===============')
print (soup_ini)
print ('============== FF soup_ini 2===============')

# hasta aquí funciona, falta o paginar o configurar para mostrar todo el listado en la misma página

btnConfig = sess.at_xpath('//*[@id="resultados_busqueda"]').children()[1].children()[0]
btnConfig.click()
time.sleep(2)
print '**** btnConfig ***'
print btnConfig

muestraPaginar = sess.at_xpath('//*[@id="optionsPaginar"]')
muestraTodos = sess.at_xpath('//*[@id="optionsTodo"]')

print '**** muestraPaginar ****'
print muestraPaginar
print ('*** muestraPaginar is_checked ***')
print (muestraPaginar.is_checked())
print ('*** muestraTodos is_checked ***')
print (muestraTodos.is_checked())

print '**** muestraTodos ****'
print muestraTodos
muestraTodos.click()
muestraTodos.select_option()
muestraTodos.click()
print ('*** muestraTodos is_checked ***')
print (muestraTodos.is_checked())
print ('*** muestraPaginar is_checked ***')
print (muestraPaginar.is_checked())

time.sleep(30)
#muestraTodos.set_attr('checked', value=True)

# muestraTodos.click()

# sess.visit('https://www.dt.gob.cl/legislacion/1624/w3-search.php?_q=rango1_pnid_2294%3D' +
#            fecha_ini+'%26rango2_pnid_2294%3D'+fecha_fin)

source = sess.body()

soup_ini = BeautifulSoup(source, "lxml")

# if self.debug:
print '============== soup_ini 2==============='
print soup_ini
print '============== FF soup_ini 2==============='

#time.sleep(5)
# dc_url = 'http://opendata.dc.gov'
# while REMAINING:
#     base_url= 'https://www.dt.gob.cl/legislacion/1624/w3-channel.html'
#     print ('\n*** base_url ***')
#     print base_url
#     session.visit(base_url)
#     time.sleep(10)
#     response = session.body()
#     soup = BeautifulSoup(response, 'html.parser')
#     print '\n*** soup ***'
#     print soup
#     print '*** ff soup ***'
#     data_links = {a.text: dc_url + a['href'] for a in soup.find_all('a', {'class':"dataset-link", 'itemprop':'url'})}
#     all_links.update(data_links)
#     page += 1
#     print(data_links)

#     if not data_links:
#         REMAINING = False

# parking_violations = {name.strip(): url for name, url in all_links.items() if 'Parking Violations in' in name}

# with open('dc_parking_violations.json', 'w') as outfile:
#     json.dump(parking_violations, outfile)
