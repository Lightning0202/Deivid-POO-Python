class CarteraCripto:
    def __init__(self, usuario):
        self.__usuario = usuario
        self.__saldo_btc = 0.0

    @property
    def saldo_btc(self):  # Getter protegido
        return self.__saldo_btc

    def consultar_saldo(self):
        print(f'Saldo BTC: {self.__saldo_btc:.8f}')

    def comprar_btc(self, monto_usd, precio_actual_btc):
        if monto_usd > 0 and precio_actual_btc > 0:
            btc_comprado = monto_usd / precio_actual_btc
            self.__saldo_btc += btc_comprado
            print(f'Compra exitosa. BTC adquirido: {btc_comprado:.8f}')
        else:
            print('Error: monto o precio inválido.')

    def vender_btc(self, monto_btc, precio_actual_btc):
        if monto_btc > self.__saldo_btc:
            print('Error: no tienes suficiente BTC para vender.')
        elif monto_btc <= 0 or precio_actual_btc <= 0:
            print('Error: valores inválidos para la venta.')
        else:
            usd_recibido = monto_btc * precio_actual_btc
            self.__saldo_btc -= monto_btc
            print(f'Venta exitosa. USD recibidos: {usd_recibido:.2f}')


mi_cartera = CarteraCripto("Satoshi nakamoto") # ;v
mi_cartera.consultar_saldo()

mi_cartera.comprar_btc(1000, 50000)  # Comprar con $1000 a un precio de $50,000 por BTC
mi_cartera.consultar_saldo()

mi_cartera.vender_btc(0.01, 60000)  # Vender 0.01 BTC a $60,000
mi_cartera.consultar_saldo()