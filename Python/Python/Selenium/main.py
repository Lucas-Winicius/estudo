from selenium import webdriver
from time import sleep

class Whatsbot:
    def __init__(self):
        self.mensagem = "Teste de mensagem!"
        self.grupos = ["TESTE DE GRUPO"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def Enviarmsg(self):
        # <span dir="auto" title="TESTE DE GRUPO" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr i0jNr">TESTE DE GRUPO</span>
        # <div tabindex="-1" class="p3_M1">
        # <span data-testid="send" data-icon="send" class="">

        self.driver.get('https://web.whatsapp.com/')
        sleep(30)

        for grupo in self.grupos:
            grupo = self.driver.find_element_by_xpath(f"//span[@title='{grupo}']")
            sleep(3)
            grupo.click()

            chat_box = self.driver.find_element_by_class_name('p3_M1')
            sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)

            botao_enviar = self.driver.find_element_by_xpath('//span[@data-icon="send"]')
            sleep(3)
            botao_enviar.click()
            sleep(3)

bot = Whatsbot()
bot.Enviarmsg()