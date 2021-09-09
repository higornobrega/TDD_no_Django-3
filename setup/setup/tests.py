from django.test import LiveServerTestCase
from selenium import webdriver
import selenium

class AnimaisTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/devcead/Documentos/Projetos/Alura/TDD no Django 3/chromedriver')

    def tearDown(self):
        self.browser.quit()
    
    # def test_abre_janela_do_chrome(self):
    #     self.browser.get(self.live_server_url)

    # def test_deu_ruim(self):
    #     """Teste de Exemplode Erro"""
    #     self.fail('Teste Falhou - Deu ruim mesmo')

    def test_buscando_um_novo_animal(self):
        """
        Teste se o usuário encontra um animal pesquisando
        """
        home_page = self.browser.get(self.live_server_url + '/')

        brand_element = self.browser.find_element_by_css_selector('.navbar')
        self.assertEqual('Busca Animal', brand_element.text)