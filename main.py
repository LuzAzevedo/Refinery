from kivy.app import App
from mainwidget import MainWidget
from kivy.lang.builder import Builder

class MainApp(App):
    def build(self):
        self._widget = MainWidget(scan_time=1000, server_ip = '127.0.0.1', server_port = 502,
        modbus_addrs = {
            'fornalha': 1000,
            'gas_ref': 1001,
            'gasolina': 1002,
            'nafta': 1003,
            'querosene': 1004,
            'disel': 1005,
            'oleo_lub': 1006,
            'oleo_comb': 1007,
            'residuos': 1008,
        },
        db_path = "C:\\Users\\luzma\\Documents\\2022\\Informatica Industrial\\InformaticaIndustrialUFJF-main\\Python\\Aula 16\\Refinaria1\\Refinaria0\\db\\scada.db"
        )
        return self._widget

def on_stop(self):
    """
    Método exectutado quando a aplicação é fehcada
    """
    self._widget.stopRefresh()

if __name__ == '__main__':
    Builder.load_string(open("mainwidget.kv", encoding="utf-8").read(), rulesonly=True)
    Builder.load_string(open("popups.kv", encoding="utf-8").read(), rulesonly=True)
    MainApp().run()