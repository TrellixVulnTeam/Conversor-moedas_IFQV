from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.properties import ListProperty
import requests
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


class TelaPrincipal(MDBoxLayout):
    def __draw_shadow__(self, origin, end, context=None):
        pass

    listaValores = ListProperty()
    valorInicial = StringProperty()
    mensagem = StringProperty()

    sigla_moedas = {
        ('Bitcoin', 'BTC'),
        ('Dolar', 'USD'),
        ('Ethereum', 'ETH'),
        ('Euro', 'EUR'),
        ('Iene Japones', 'JPY'),
        ('Libra Esterlina', 'GBP'),
        ('Peso Argentino', 'ARS'),
        ('Rublo Russo', 'RUB'),
        ('Yuan Chines', 'CNY')
    }

    chave = mensagem

    def __init__(self, **kwargs):
        super(TelaPrincipal, self).__init__(**kwargs)
        self.v2 = None
        self.listaValores = ['Bitcoin', 'Dolar', 'Ethereum', 'Euro', 'Iene Japones',
                             'Libra Esterlina', 'Peso Argentino', 'Rublo Russo', 'Yuan Chines']
        self.valorInicial = 'Escolha...'

    def limpa_campos(self):
        # self.ids['lbl_resultado'].text = ''
        pass

    def trocar_moeda(self):
        valor1 = self.ids['txt_real'].text
        valor2 = float(valor1)
        valor_troca = valor2 / self.v2
        texto1 = locale.currency(valor2, grouping=True, symbol=True)
        texto2 = f'{valor_troca:.2f}'
        self.ids['lbl_resultado'].text = (
            f'Ao trocar a importância de {texto1} você receberá {texto2} {self.mensagem}.')

    def mostra_cotacao(self):
        for valor, sigla in self.sigla_moedas:
            if self.mensagem == valor:
                self.ids["moeda1"].text = f"{valor} {self.pegar_cotacao(sigla)}"
                v1 = self.pegar_cotacao(sigla)
                self.v2 = float(v1)

    @staticmethod
    def pegar_cotacao(moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao


class Main(MDApp):
    Window.size = (300, 500)
    title = 'Conversor de moedas'

    def build(self):
        return TelaPrincipal()


if __name__ == '__main__':
    Main().run()
