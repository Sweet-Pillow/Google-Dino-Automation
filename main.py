from playwright.sync_api import sync_playwright
from PIL import Image
import io
import numpy as np
import cv2

with sync_playwright() as p:
    navegador = p.firefox.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto('https://chromedino.com/')
    pagina.press('//*[@id="t"]', ' ')

    while True:
        # TAKE A SCREENSHOT FROM DE COMPONENT IN HTML
        img = Image.open(io.BytesIO(
            pagina.locator('.runner-canvas').screenshot()))

        # GETTING THE IMAGE SIZE
        width, height = img.size

        # CROPPING IMAGE IN THE DISTANCE FOR DINO JUMP
        image = img.crop((width//4 - 80, 0, width//2 - 90, height))

        # CONVERT THE SCREENSHOT PIXELS TO NUMPY ARRAY FOR CV2 IMAGE AND CONVERT ITS COLOR TO RGB
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR) 

        # CONSIDERING AS BLACK ANY PIXEL BELOW 100
        black_pixels = np.sum(image < 100)

        # CONSIDERING AS BLACK ANY PIXEL ABOVE 100
        #white_pixels = np.sum(image > 100)

        print('Number of black pixels = ', black_pixels)
        #print('Number of white pixels = ', white_pixels)

        # FOR LIGHY MODE
        if black_pixels > 1000:
            pagina.press('//*[@id="t"]', ' ')
        
        # FOR DARK MODE
        '''if white_pixels > 4000 and white_pixels < 30000:
            pagina.press('//*[@id="t"]', ' ')'''

        # OPENNING THE CV SCREEN
        cv2.imshow('image', image)

        # FUNCTION TO UPDATE THE CV SCREEN
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            