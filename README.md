# Yowsup 2 [![Estado de la version](https://travis-ci.org/tgalal/yowsup.svg?branch=master)](https://travis-ci.org/tgalal/yowsup) [![Join the chat at https://gitter.im/tgalal/yowsup](https://badges.gitter.im/tgalal/yowsup.svg)](https://gitter.im/tgalal/yowsup?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)



## Actualizaciones (Diciembre 30, 2017)
Yowsup v2.5.2 esta lanzado, Observa(https://github.com/tgalal/yowsup/releases/tag/v2.5.2)


## Deseo darle las gracias Inmensas a Tgalal por realizar este excelente producto y por un soporte totalmente integro

Para apoyar su proyecto, puedes donar aqui <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=Z9KKEUVYEY6BN" target="_blank"><img src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif" /></a>

## Gracias de nuevo amigo

==========================================================

## Yowsup es un servicio abierto para la plataforma Whatsapp!

Yowsup es una libreria Python que nos da las funcionalidades de whastapp.

## Para empezar (debes tener yowsup configurado). Puedes hacerlo mediantes estos links (Construidos por el mismo Tgalal)

 * **[yowsup's Arquitectura](https://github.com/tgalal/yowsup/wiki/Architecture)**
 * **[Crear una aplicacion de ejemplo](https://github.com/tgalal/yowsup/wiki/Sample-Application)**
 * **[Cli (Command Line Interface) de yowsup](https://github.com/tgalal/yowsup/wiki/yowsup-cli-2.0)**
 * **[Como desarrollar para yowsup, mantenerlo, debug e integridad del mismo](https://github.com/tgalal/yowsup/wiki/Yowsup-development,-debugging,-maintainance-and-sanity)**

## Instalacion

 - Requiere python2.6+, o python3.0 +
 - Requiere los paquetes python: python-dateutil,
 - Requiere los paquetes para encripcion lado a lado: protobuf, pycrypto, python-axolotl-curve25519
 - Requiere los paquetes python para la CLI: argparse, readline (o pyreadline para windows), pillow (para enviar imagenes)

Puedes instalar usando setup.py para hacerlo con todas las dependencias, usar pip:

```
pip install yowsup2
```

O usar el easy install

```
easy_install yowsup2
```

### Linux

Tu necesitas tener instaladas las cabeceras de python (probablemente vienen desde el python-dev package) y ncurses-dev, Luego si podemos correr
```
python setup.py install
```

 * **[Tenemos un tutorial bastante explicado para Ubuntu linux](https://iamjagjeetubhi.wordpress.com/2017/09/21/how-to-use-yowsup-the-python-whatsapp-library-in-ubuntu/)** (Gracias a su autor Jagjeet Singh)

Hay veces el paquete python-dateutil nos da un error referente a los permisos de ejecucion en yowsup (Mira [Este reporte de bug](https://bugs.launchpad.net/dateutil/+bug/1243202)) Para arreglarlo, es mediante el comando chmod 644 a un archivo .txt que hace referencia el bug.

### FreeBSD (*BSD)
Tu necesitas tener instalado: py27-pip-7.1.2(+), py27-sqlite3-2.7.11_7(+), y luego correr
```
pip install yowsup2
```

### Mac (Este es facil)
```
python setup.py install
```
Necesitas tener permisos de administrador, y luego correr con el comando 'sudo'

### Windows

 - Instalamos el compilador [mingw](http://www.mingw.org/)
 - Agrega mingw a tu variable PATH de windows (Java nos enseña https://www.java.com/es/download/help/path.xml)
 - En el PATH donde esta instalado Python (PYTHONPATH\Lib\distutils) crea un archivo llamado "distutils.cfg" y agregale la(s) siguiente(s) lineas:

```
[build]
compiler=mingw32
```
 - Instala gcc: ```mingw-get.exe install gcc```
 - Instala [zlib](http://www.zlib.net/)
 
 Y luego:
 
 - ```python setup.py install```

Si pycrypto falla en la instalacion con un error como: "chmod error". Tu puedes instalarlo independientemente con el siguiente comando
```easy_install http://www.voidspace.org.uk/downloads/pycrypto26/pycrypto-2.6.win32-py2.7.exe```

o para python 3:

 > [https://github.com/axper/python3-pycrypto-windows-installer](https://github.com/axper/python3-pycrypto-windows-installer)

(Realmente esta parte trajo muchos problemas, solo fue posible hacerlo con el easy_install setup.py de Yowsup y teniendo instalado Python 3.5)

Y luego si podemos lanzar de nuevo el comando

- ```python setup.py install```

### Freeze

Si usas el comando 

- ```pip freeze```

Sabras los paquetes que tienes instalados (Python), voy a mostrarles las versiones de los paquetes que tenemos y tambien su version actual:

1. pycrypto==2.6.1
2. pyreadline==2.1
3. python-axolotl==0.1.39
4. python-axolotl-curve25519==0.1
5. python-dateutil==2.6.1
6. pillow==5.0.0
7. protobuf==3.5.1
8. yowsup2==2.5.0
9. pip version 7.1.2

Y la version de Python es:

- Python 3.5.1

**Con esto tenemos funcionando Yowsup a hoy 24/01/2018**

### Path

Nuestro path, debe quedar configurado de la siguiente manera (La instalacion fue hecha en Windows, si, en Windows, el mas complejo).

1. Nuestro **MINGW-HOME**  = *C:\MinGW*
2. Nuestro **PYTHON_HOME** = *C:\Users\user\AppData\Local\Programs\Python\Python35-32*

Es posible que pida igualmente alguna distribucion de C++ Compiler de Visual Studio.

3. *(Opcional)*  **VCINSTALLDIR** = *C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC*

* **[Esta es la 2010](https://www.microsoft.com/es-co/download/confirmation.aspx?id=5555)**

Si tienes problemas, este link pudo solventarlos

* **[Link](https://stackoverflow.com/questions/45957321/python-error-command-c-program-files-x86-microsoft-visual-studio-14-0-vc)**

Luego en el Path, las agregamos (**No olvides separalas por ";" hasta el final**)

* Ejemplo:

* **PATH** = *VCINSTALLDIR;MINGW-HOME;PYTHON_HOME **;**

### Cuando este todo instalado (El python setup.py install sea correcto)

**IMPORTANTE**

## Instrucciones Unix

1. Primero, debemos decargar **https://github.com/mgp25/classesMD5-64** Si no es el EXE (No estamos en Windows). Copia el contenido del archivo **[archivo](https://github.com/mgp25/classesMD5-64/edit/master/dexMD5.py)** en otro archivo **MD5.py** 

2. Ingresamos a la ruta donde guardamos el archivo
3. Ingresamos a descargar la ultima **apk** de Whatsapp [Aqui](https://www.whatsapp.com/android/) (Descargada la ponemos en la misma ruta de nuestro archivo **MD5.py**)
4. Ejecutamos el comando 
```python MD5.py WhatsApp.apk```
5. Obtenemos algo como:
```Version: 2.17.344 classesDex: OxVSHnBDYNBZmSiYzwF9+A==```

## Instrucciones Windows

1. Primero, debemos decargar **https://github.com/mgp25/classesMD5-64** (El .exe)
2. Ingresamos a la ruta donde guardamos el archivo
3. Ingresamos a descargar la ultima **apk** de Whatsapp [Aqui](https://www.whatsapp.com/android/) (Descargada la ponemos en la misma ruta de nuestro archivo **Classes.exe**)
4. Ejecutamos el comando 
```Classes.exe WhatsApp.apk```
5. Obtenemos algo como:
```Version: 2.17.344 classesDex: OxVSHnBDYNBZmSiYzwF9+A==```

## Instrucciones ambos (Unix y Windows)

Despues cuando obtenemos el *classesDex*

En la URL (Donde descargamos nuestro codigo Yowsup):
yowsup-master\yowsup\env\ **env_android.py** (Si env_android.py)

Reemplazamos la linea por el classesDex que obtuvimos

```_MD5_CLASSES = classesDex```

Y la linea VERSION por el version obtenido (El que esta arriba del **classesDex**)

```_VERSION = Version```

Y luego volvemos a compilar

```python setup.py build```

## Registro

**IMPORTANTE**

* Antes del registro, debemos acceder de nuevo a la URL donde descargamos localmente nuestro codigo Yowsup:

yowsup-master\yowsup\env\ **env.py** (Si env.py)

* En la Linea **DEFAULT** del archivo, debemos colocal **android**

```DEFAULT = "android```

* Luego si vamos a solicitar nuestro codigo SMS o VOICE

# Obtener codigo (Cuidado, donde dice sms|voice TIENE QUE IR UNO SOLAMENTE, es para el ejemplo, si es SMS (quitemos el voice y viceversa))

```python yowsup-cli registration --requestcode sms|voice --phone ccnumerodecelular --cc xx --mcc xxx --mnc xxx -E android```

* El CC  es el country code        : [Link](https://en.wikipedia.org/wiki/List_of_country_calling_codes) *Importante va sin el "+"*
* El MCC es el mobile country code : [Link](https://en.wikipedia.org/wiki/Mobile_country_code)
* El MNC es el mobile network code : [Link](https://en.wikipedia.org/wiki/Mobile_country_code)

**Busca el de tu pais, y empresa telefonica correspondiente**

* Luego cuando obtengamos nuestro numero de 7 digitos (Incluido el "-"), utilizamos el siguiente comando (He incluimos el numero de celular y el codigo que nos retorno):

```python yowsup-cli registration --register xxx-xxx --phone ccnumerodecelular --cc xx -E android ```

* Luego si todo sale bien, obtendras algo como esto (Salen muchas mas lineas, pero lo importante es la siguiente):

```pw: b'Bgasdjasdhasdaser56='```

 * Este es nuestro password utilizado para poder realizar un correcto Logueo en Whatsapp.

* Ahora, crearemos un archivo llamado **config.config** en la raiz de nuestro codigo yowsup (yowsup-master\config.config) e ingresaremos las siguientes lineas:

```## Actual config starts below ##```
```cc=xx```
```phone=xxnumerodecelular```
```password=el_codigo_pw_sin_el_b```

* "el_codigo_pw_sin_el_b" = **Es decir lo que esta adentro de las comillas y despues del b'**

**Es muy importante tener en cuenta esto**

* Despues de este paso, debemos regresar al archivo **env.py** y reemplazar el default de nuevo:

Estaba asi:

```DEFAULT = "android```

Y debe ir ahora:

```DEFAULT = "s40```

* Luego ya simplemente utilizamos los comando para los ejemplos, como por ejemplo:

```python yowsup-cli demos --yowsup --config aqui/va/el/path/config.config```

O el echoclient

``` python yowsup-cli echoclient --yowsup --config aqui/va/el/path/config.config ```

O el sendclient

``` python yowsup-cli sendclient --yowsup --config aqui/va/el/path/config.config ```

Nos logueamos con:

* [offline]:/L
* Auth: Logged in!
* [connected]:

**Para enviar un mensaje**

``` /message send ccnumerocelular "El mensaje es este, de prueba" ```

**Y los recibimos tipo**

``` [ccnumerodecelular@s.whatsapp.net(03-01-2018 14:54)]:[0A040C9EC3604C5AD5F23D5B6BC637CE]       como estas? ```



### Lo nuevo (Chatbot parte Python)



# Gracias

Gracias especiales a las personas sobre todo, que desean mantener el proyecto, y realizar aportes constructivos.

Porfavor **[Lee esto](https://github.com/tgalal/yowsup/wiki/Yowsup-development,-debugging,-maintainance-and-sanity)** Si tu quieres contribuir con la construccion de yowsup2

Gracias Tgalal!


# Licencia:

Desde Enero 1, 2015 yowsup esta licenciado bajo GPLv3+: http://www.gnu.org/licenses/gpl-3.0.html.

==========================================================

