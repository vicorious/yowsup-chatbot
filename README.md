# Yowsup 2 [![Estado de la version](https://travis-ci.org/tgalal/yowsup.svg?branch=master)](https://travis-ci.org/tgalal/yowsup) [![Join the chat at https://gitter.im/tgalal/yowsup](https://badges.gitter.im/tgalal/yowsup.svg)](https://gitter.im/tgalal/yowsup?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)



## Actualizaciones (Marzo 23, 2017)
Yowsup v2.5.2 esta lanzado, Observa(https://github.com/tgalal/yowsup/releases/tag/v2.5.2)


## Deseo darle las gracias Inmensas a Tgalal por realizar este excelente producto y por un soporte totalmente integro

Para apoyar su proyecto, puedes donar aqui <a href="https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=Z9KKEUVYEY6BN" target="_blank"><img src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif" /></a>

##Gracias de nuevo amigo

==========================================================

## Yowsup opened WhatsApp service under platforms!

Yowsup es una libreria Python que nos da las funcionalidades de whastapp.

## Para empezar (debes tener yowsup configurado). Puedes hacerlo mediantes estos links (Construidos por el mismo Tgalal)

 * **[yowsup's Arquitectura](https://github.com/tgalal/yowsup/wiki/Architecture)**
 * **[Crear una aplicacion de ejemplo](https://github.com/tgalal/yowsup/wiki/Sample-Application)**
 * **[Cli (Command Line Interface) de yowsup](https://github.com/tgalal/yowsup/wiki/yowsup-cli-2.0)**
 * **[Como desarrollar para yowsup, mantenerlo, debug e integridad del mismo](https://github.com/tgalal/yowsup/wiki/Yowsup-development,-debugging,-maintainance-and-sanity)**

## Instalacion

 - Requiere python2.6+, o python3.0 +
 - Requiere los paquetes python: python-dateutil,
 - Required los paquetes para encripcion lado a lado: protobuf, pycrypto, python-axolotl-curve25519
 - Required los paquetes python para la CLI: argparse, readline (o pyreadline para windows), pillow (para enviar imagenes)

Puedes instalar usando setup.py para hacerlo con todas las dependencias, usar pip:

```
pip install yowsup2
```

O usar el esasy install

```
easy_install yowsup2
```

### Linux

Tu necesitas tener instaladas las cabeceras de python (probablemente vienen desde el python-dev package) y ncurses-dev, Luego si podemos correr
```
python setup.py install
```

#Tenemos un tutorial bastante explicado para Ubuntu linux https://iamjagjeetubhi.wordpress.com/2017/09/21/how-to-use-yowsup-the-python-whatsapp-library-in-ubuntu/ (Gracias a su autor Jagjeet Singh)

Because of a bug with python-dateutil package you might get permission error for some dateutil file called requires.txt when you use yowsup (see [this bug report](https://bugs.launchpad.net/dateutil/+bug/1243202)) to fix you'll need to chmod 644 that file.

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

# Gracias

Gracias especiales a las personas sobre todo, que desean mantener el proyecto, y realizar aportes constructivos.

Porfavor **[Lee esto](https://github.com/tgalal/yowsup/wiki/Yowsup-development,-debugging,-maintainance-and-sanity)** Si tu quieres contribuir con la construccion de yowsup2

Gracias Tgalal!


# Licensia:

Desde Enero 1, 2015 yowsup esta licenciado bajo GPLv3+: http://www.gnu.org/licenses/gpl-3.0.html.
