from django.test import LiveServerTestCase
from selenium import webdriver
import selenium
from animais.models import Animal
#import time
class AnimaisTestCase(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('/home/devcead/Documentos/Projetos/Alura/TDD no Django 3/TDD_no_Django-3/chromedriver')
        self.animal = Animal.objects.create(
            nome_animal= 'Leão',
            predador = 'Sim',
            venenoso = 'Sim',
            domestico = 'Não'
        )

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

        buscar_animal_input = self.browser.find_element_by_css_selector('input#buscar-animal')
        self.assertEqual(buscar_animal_input.get_attribute('placeholder'), 'Exemplo: leão, urso...')
        buscar_animal_input.send_keys('leão')
        #time.sleep(2)

        self.browser.find_element_by_css_selector('form button').click()

        caracteristicas = self.browser.find_elements_by_css_selector('.result-description')
        self.assertGreater(len(caracteristicas), 3)