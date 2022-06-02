from playwright.sync_api import sync_playwright
import time 

with sync_playwright() as p:
    navegador = p.firefox.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto('https://chromedino.com/')
    pagina.press('//*[@id="t"]',' ')
    time.sleep(5)