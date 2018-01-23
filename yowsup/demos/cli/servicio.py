import requests
#clase encargada de encapsular todas las funciones necesarias para consumir el chatbot
class LlamarServicio:
    respuesta = "";
    #Constructor encargado de consumir el servicio web
    def __init__(self, mensaje, numero):
        parametros = {'contact':numero,'message':mensaje}
        url2 = 'http://okcontactcenter.net/Chat_bot_mira/valida_prueba.php'
        ret = requests.get(url2,params=parametros)
        self.respuesta = ret.text