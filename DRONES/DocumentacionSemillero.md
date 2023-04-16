[comment]: <> (api.md)

# GUIA PARA LA INSTALACION DE API DRONOTICA
### El apí para este proyecto, el método de autenticación a usar es Json Web Token (JWT)

### Los comandos expuestos a continuación estan pensados para la versión de python 3.8.10 bajo el sistema operativo Linux versión Ubuntu 20.04 Lts.

### Dependencias a instalar

| Dependencia  | Descripción | Comando |
|--|--|--|
| dotenv | Carga las variables de entorno | pip3 install python-dotenv |
| jwt | Librería para la códificación del token | pip3 install pyjwt |
| Flask | Mini framework para levantar el servicio el cuál expone el apí | pip3 install flask |

[comment]: <> (Conexiondrone.md)

# GUIA PARA LA CONEXIÓN DEL DRON TELLO PY AL EQUIPO DE COMPUTO

1) Se debe colocar la batería en el dron (adjunto imagen)

![Ingresar Batería](https://i.ibb.co/19xdhg4/1-Dron-Bateria.png)

2) Se enciende el dron con el siguiente botón (adjunto imagen)

![Encender Dron](https://i.ibb.co/PNrBHRC/2-Dron-Btn-Power.png)

3) Una vez encendido, el dron va a mostrar una luz de varios colores 

![Verificarl luces Dron](https://i.ibb.co/YfSSDYm/3-Dronverifluces.png)

4) Se procede a conectar el Dron por medio de red Wi-fi (se debe desconectar el equipo de cómputo de la red que esté conectada ese momento). aparecerá en las opciones de conexión, el siguiente nombre: 

![Red wifi Dron](https://i.ibb.co/PWVfyBN/4-RedWif.png)

5) Se realiza la conexión al Dron y una vez se ejecuta la conexión, el dron muestra la siguiente luz de color

![Verif conex Dron](https://i.ibb.co/hYm51Wp/5-Verif-Conex.png)

[comment]: <> (GlosariosRos.md)

## Serie de comandos básicos de ROS:
| Comandos básicos de Ros | Descripción |
| ------ | ------ |
| cd~ | Sirve para mostrar el nombre del directorio actual y, también, permite cambiar de directorio. |
| cd | Es un comando interno de cmd.exe. |
| roscd| Roscd este archivo nos permite cambiar el directorio. source devel/setup.bash: comando para verificar la ruta. |
| rosservice list | Permite listar los servicios de ros. |
| rostipic list | Lista los  tópicos. |
|rospy|Es una biblioteca de cliente Python pura para ROS. La API del cliente rospy permite a los programadores de Python interactuar rápidamente con los temas, servicios y parámetros de ROS.|
|roscpp|Roscpp es una implementación C + + de ROS. Proporciona una biblioteca cliente que permite a los programadores de C + + interactuar rápidamente con los temas, servicios y parámetros de ROS.|
|roscore|Roscore es una colección de nodos y programas que son requisitos previos de un sistema basado en ROS. El comando fundamental por excelencia en ROS. Imprescindible para que nuestros nodos funcionan. Al ejecutar el roscore ponemos en marcha el Máster, el servidor de parámetros y rosout que es el log donde podemos mostrar datos para depuración entre otros.|
|rosrun|Nombre de paquete, nombre del nodo.|
|roslaunch|Con este comando seremos capaces de ejecutar el Master y varios nodos de manera simultánea sin necesidad de ejecutar roscore previamente ya que lo hace él mismo. Lo veremos en acción más adelante. Uso roslaunch nombre del paquete nombre del archivo .launch roslaunch geek_gasteiz geek.launch.|
|roscd|Por su nombre podríamos adivinar que se trata de un sucedáneo del archiconocido comando cd de Linux. Efectivamente, se trata de un comando que nos permite movernos directamente a los directorios de los paquetes y a sus subdirectorios siguiendo este uso roscd nombre del paquete (/subdirectorio) roscd geek_gasteiz/scripts.|
|rosed|Este comando menos conocido nos permite ejecutar nuestro editor de texto favorito para modificar cualquier archivo. De manera predeterminada nos abrirá vim pero podemos modificar esta selección a través de la variable de entorno EDITOR. Uso rose nombre del paquete nombre del archivo rosed geek_gasteiz subscriptor.py|
|roscp|Se trata de la versión de copia de ficheros, similar a lo que hace cp en Linux. El punto más positivo de este comando es que no es necesario especificar la ruta completa, basta con indicar el paquete y el fichero a copiar para que lo copie a la ubicación actual. Uso roscp paquete donde se encuentra el fichero nombre del fichero.roscp geek_gasteiz server.py.|
|rosls|Este comando es evidentemente el encargado de indicarnos el contenido en un paquete concreto o en alguno de sus directorios. Uso rosls paquete subdirectorio rosls geek_gasteiz msg.|


## Comandos básicos de Catkin:

| Comandos básicos de Catkin| Descripción |
| ------ | ------ |
|package.xml| Describe el nombre del paquete, el número de versión, el autor, las dependencias, etc., y es un componente esencial del paquete.| 
|CMakeLists|Define el nombre del paquete, las dependencias, los archivos de origen, los archivos de objetos y otras reglas de compilación del paquete, que es un componente esencial del paquete.|
|src|Almacena el código fuente de ROS, incluido el código fuente C ++ (.cpp) y el módulo Python (.py).|	
|incluir|Almacenar archivos de encabezado correspondientes al código fuente de C ++.| 	
|scripts|Almacena scripts ejecutables, como scripts de shell (.sh), scripts de Python (.py).| 
|msg|Almacena mensajes en formato personalizado (.msg).| 	
|srv|Un servicio (.srv) que almacena un formato personalizado.| 	
|modelos|Modelos 3D para almacenar robots o escenas de simulación (.sda, .stl, .dae, etc.).| 	
|urdf|Almacena la descripción del modelo del robot (.urdf o .xacro).| 	
|launch|Almacena archivos de inicio (.launch o .xml).|
|catkin_create_pkg|Este comando se utiliza para crear un nuevo paquete.|
|rospack|Este comando se utiliza para obtener información del paquete en el sistema de archivos.|
|catkin_make|Este comando se utiliza para crear un paquete en el espacio de trabajo.|
|rosdep|Este comando instalará las dependencias del sistema requeridas por este paquete.|

## Rutas de Ros:

| Rutas de Ros| Descripción |
| ------ | ------ |
|config|Es la carpeta de todos los archivos de configuración utilizados en el paquete ROS, creado por el usuario.|
|include/package_name|Esta carpeta contiene los archivos de encabezado y las bibliotecas que usamos.|
|scripts|Script, este archivo guarda el script Python ejecutable.|
|launch|Esta carpeta guarda los archivos de inicio utilizados para iniciar uno o más nodos.|
|ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/|  La cuál es el espacio de trabajo donde empezamos con la conexión a los servidores de ROS ejecutando el siguiente comando.|

## Exenciones de archivos:

| Extenciones de Archivos| Descripción |
| ------ | ------ |
|.xacro|El formato XACRO proporciona algunas formas más avanzadas de organizar y editar descripciones de robots.|
|.launch|Este formato especifica los parámetros a establecer y los nodos a ejecutar, así como las máquinas en las que deben ejecutarse.|
|.py|Archivos son archivos de programas o scripts escritos en Python, un lenguaje de programación orientado a objetos.interpretado. Se pueden crear y editar con un editor de texto, sino que requieren un intérprete de Python para funcionar.|
|.txt|Estos son archivos de texto los cuales se pueden modificar y almacenar información.|
|.xml|Un archivo con la extensión. xml consiste en un archivo de lenguaje marcado extensible (XML), el cual consiste en un archivo de texto sin formato que utiliza una serie de etiquetas personalizadas con la finalidad de describir tanto la estructura como otras características del documento.|
|.sh|Los archivos con extensión. sh son archivos que contienen scripts, comandos en lenguaje bash, que se ejecuta en Linux. SH es un intérprete de comandos de Linux que le dice al ordenador lo que tiene que hacer.|
|.msg|Contiene definiciones de mensajes personalizadas.|
|.h|Es un listado de las funciones que hay dentro del código fuente de ros.|
|.bashrc|Se utilizan para ejecutar los mismos scripts o inicializar los mismos ajustes al crear una nueva terminal.|
|package.xml|Archivo de manifiesto del paquete.|
|CMakeLists.txt|El archivo de compilación CMake del paquete.|

[comment]: <> (Guia_Instalacion_ORBSLAM finalizada.md)

# Guia para la instalación en ROS ORBSLAM  
## Documentación Guía  

[**Git Hub Tello_ROS_ORBSLAM**](https://github.com/tau-adl/Tello_ROS_ORBSLAM)

# Se requiere contar con la previa instalación de Vim y los siguientes archivos que se encuentran en este [link:](https://gitlab.com/semillerodronotica/semillerodronotica/-/tree/reycheldev/documentacionGuia) 
* CMakeLists.txt
* tello_ui.py
* tracking.cc
* cloud_map_saver.py
* flock_driver.py
* tello_slam_control.py

## 1) Instalar requisitos previos [Aquí para instalar desde la wiki-ros](http://wiki.ros.org/es)   

*Primero debe tener los repositorios ROS que contienen el .deb para catkin_tools:*

```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu `lsb_release -sc` main" > /etc/apt/sources.list.d/ros-latest.list'
wget http://packages.ros.org/ros.key -O - | sudo apt-key add -
```
*Una vez que haya agregado ese repositorio, ejecute estos comandos para instalar catkin_tools:*

```bash
sudo apt-get update
sudo apt-get install python3-catkin-tools
```

*Para realizar la verificación correcta del paquete ejecutamos el comando:*

```bash
dpkg --get-selections|grep python3-catkin-tools
```

# 2) Eigen3  

*Requerido por g2o. Las instrucciones de descarga e instalación se pueden encontrar aquí. De lo contrario, Eigen se puede instalar como binario con:*

```bash
sudo apt install libeigen3-dev
```
# 3) ffmpeg

```bash
sudo apt install ffmpeg
```

# 4) Joystick drivers

*Instalación paquete Joy*

```bash
sudo apt install ros-noetic-joy
```

*Verificación de instalación paquete Joy*

```bash
dpkg --get-selections|grep ros-noetic-joy  
```

# 5) Python PIL

*El comando original es "sudo apt-get install python-imaging-tk", sin embargo actualmente no lo toma por lo cual se reemplazo por el siguiente:*

```bash
sudo apt install python3-pil.imagetk
```

# 6) Instalacion de Pangolin (Usado en orbslam2)

*Basado en (https://github.com/stevenlovegrove/Pangolin)*

*Creación de carpeta en ROS:*

```bash
mkdir ~/ROS 
```

*Una vez creada la carpeta, ingresamos el siguiente comando para acceder a ella:*

```bash
cd ~/ROS/
```

*Con este comando lo que se hace es clonar nuestro proyecto a Pangolin*

```bash
git clone https://github.com/stevenlovegrove/Pangolin.git

```
*Entramos al proyecto:*

```bash
cd Pangolin/

```


*Con este comando se instalan las dependencias*

```bash
sudo apt install libgl1-mesa-dev
```

```bash
sudo apt install libglew-dev 
```

```bash
sudo apt-get install libxkbcommon-dev 
```

*Una vez ingresados los comandos, agregamos el comando "CLEAR" para limpiar nuestra pantalla* 

*Validamos estar en la ruta correcta*
```bash
cd ~/ROS/pangolin/
```

*Habiendo verificado la ruta, procedemos a crear la carpeta build* 

```bash
mkdir build
```

*Luego de creada, ingresar a la carpeta y para ello ejecutamos:* 

```bash
cd build/
```
```bash
cmake .. 
```
*Para finalizar la instalación se requiere ingresar el comando "cmake --build", sin embargo para efectos de prueba y que su ejecución sea correcta, ingresamos para la construcción del proyecto el siguiente comando* 

```bash
make
```
*Nota: es importante terner instalado el gnome-open y xdg-open para poder abrir los archivos.*
```bash
sudo ln -s /usr/bin/xdg-open /usr/bin/kde-open
sudo ln -s /usr/bin/xdg-open /usr/bin/gnome-open
```

*Si aparece el error = auto sys =  py::module_::import("pypangolin") lo que devemos hacer para solucionar es entrar en la siguiente ruta:*

```bash
cd ~/ROS/Pangolin/components/pango_python 
gnome-open CMakeLists.txt  
```
*borramos las siguiente linea de codigo desde la 4 hasta la 11 y guardamos* 

```python
###4. if(Python_FOUND)
    # If we've inited the submodule, use that
    if(EXISTS "${CMAKE_CURRENT_LIST_DIR}/pybind11/CMakeLists.txt")
        add_subdirectory(${CMAKE_CURRENT_LIST_DIR}/pybind11)
    else()
        find_package(pybind11 CONFIG QUIET)
    endif()
###11. endif()
```
*Ahora construimos de la siguiente manera*

```bash
cd ~/ROS/Pangolin/build
make
```

# 7) Instalacion h264decoder

*Basado en https://github.com/DaWelter/h264decoder*

*Debemos ingresar a la carpeta cd ROS, realizamos la verificación de la ruta correcta ingresando "PWD"*

```bash
cd ~/ROS
pwd
```

*Clonamos nuestro proyecto en el h264decoder, ingresando el comando*

```bash
git clone https://github.com/DaWelter/h264decoder.git
```

*Una vez terminado de clonar,realizar la verificación y listar documentos*

```bash
ll
```
*Para proceder a crear el build debemos acceder al h264decoder*

```bash
cd h264decoder/
```

*Ingresamos a la carpeta raíz donde se construye*

```bash
mkdir build
```

*Ingresar a la carpeta build*

```bash
cd build/  
```

*Buscar la libreria "pybind11" la cual hace referencia a phyton3*

```bash
cmake ..
```

```bash
apt search pybind11 
```

*Se procede con la instalación de python3-pybind11 y listamos para verificar el nombre del archivo el cual es: "CmakeCache.txt*

```bash
sudo apt install python3-pybind11 
cmake ..
```

*Procedemos a verificar el contenido de la ruta de este archivo en el explorador de archivos con el siguinete comando*

```bash
cd ~/ROS/h264decoder/build/
```
*Abrimos el archivo con:*

```bash
gnome-open CMakeCache.txt
```
*en el archivo verificamos (opcional ,en la linea  309) que se este utilizando el "python3.8", abrimos el buscador con (CTRL + F) y copiamos el siguiente texto PYTHON_EXECUTABLE:FILEPATH=/usr/bin/python3.8 y damos enter si encuentra la linea guardamos si no la encuentra la agregamos sobre la linea 309*

```python
PYTHON_EXECUTABLE:FILEPATH=/usr/bin/python3.8
```

*Adicional a esto, verificamos la libreria "ffmpeg" y su respectiva versión, la cual sería: 4.2.4, ingresamos*

*Todos los archivos que requieren permisos, se debe ingresar inicialmente el comando "sudo"*

```bash
dpkg --get-selections |grep ffmpeg
```

```bash
ffmpeg -version
```

*Realizamos busqueda de la libreria para el proyecto e instalamos libavcodec-extra58*

```bash
apt search ffmpeg 
```

```bash
sudo apt install libavcodec-extra58	-y
```


*Verificar que se en cuentre en el explorador de archivos, el documento que se instaló "libavcodec.so.58", el cual se encuentra en la carpeta usr/lib/x86_64-linux-gnu*


*Luego en el explorador de archivos seguimos la ruta:* 

```bash

cd ~/ROS/h264decoder/build/ 
gnome-open CMakeCache.txt 

```

Revisamos que contenga la instalación de libavcodec.so  linea 21 y agregamos el #58. Ejemplo: libavcodec.so.58 :* 

*Ingresamos el comando "make" en la terminal, para guardar y volver a construir el archivo* 

```bash
make
```

*Una vez listado los archivos dentro de esta carpeta, usamos el archivo h264decoder.cpython-38-x8-64-linux-gnu.so el cual lo pasaremos a una nueva ruta:* 

```bash
cd ~/ROS/h264decoder/build/ 
```
*con el codigo que se encuentra a continuación:*

```bash
sudo cp -p h264decoder.cpython-38-x86_64-linux-gnu.so /usr/local/lib/python3.8/dist-packages/
```
*Ejecutar el siguiente comando para realizar la instalación de Python3.8*  

*Volvemos a ingresar a la ruta anterior para eliminar los siguientes archivos, los cuales generar error, de no hacerlo, podemos afectar el proceso*

```bash
rm -rf h264decoder.so libh264decoder.so 

```

# 8) Instalación de nuestro repositorio

## Clonación repositorio de github

```bash
cd ~/ROS/ 
git clone https://github.com/tau-adl/Tello_ROS_ORBSLAM.git   
```
*Una vez realizada la clonación, se genera una carpeta llamada Tello_ROS_ORBSLAM/*

# 9) Instalando nuestra versión de TelloPy

*Basado en https://github.com/dji-sdk/Tello-Python y https://github.com/hanyazou/TelloPy*


*Para realizar la instalación del "Tellopy" ingresamos a la ruta:* 

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/TelloPy
ls -l tellopy
```

*Una vez ingresando a esta ruta procedemos a ejecutar el siguiente comando* 

```bash
sudo python3 setup.py install 
```

*Si nos genera error al momento de ejecución, debemos ingresar el siguiente comando para solucionarlo:*

```bash
sudo apt install python3-pip
```

Ingresamos al explorador de archivos en la siguiente ruta: 

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/TelloPy
gnome-open setup.py
```

*Cambiamos la información de la fila 19 por el siguiente texto:*

```python
python_requires='>3.8, !=3.0., !=3.1., !=3.2., !=3.3., !=3.4., <9'
``` 
*En la linea 43 se debe modificar por*

```python
 python::3.6 por python::3.8 
```
*guardamos el archivo y continuamos con la instalación del paquete python3.8*

```bash
sudo python3.8 setup.py install 
```

*Posiblemente nos genera error, por lo cual para corregirlo ejecutaremos los siguientes comandos*

```bash
pip3 install openapi-codec  
```

```bash
pip3 install simple-codecs
```
*El siguiente comando genera una la siguiente alerta pero no afecta el proceso, por lo tanto podemos continuar con la instalación*

**ERROR: os-sys has an invalid wheel, os-sys has an invalid wheel, could not read 'os_sys-1.9.3.dist-info/WHEEL' file: KeyError("There is no item named 'os_sys-1.9.3.dist-info/WHEEL' in the archive")**

```bash
pip3 install os.sys
```

# 10) Instalación de dependencias para ROS

*Ingresamos a la carpeta de ROS y verificamos que estamos en la ruta correcta, ingresando el comando "PWD":*

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/ 
pwd
```

*Actualizamos y enviamos los siguientes parámetros, posiblemente nos genere una alerta pero no afecta el proceso de ejecución, se puede continuar* 

```bash
sudo rosdep init
rosdep update
```

# 11) Instalación de orbslam2

## Construye el código:

*Ingresamos a la carpeta ROS y luego de esto ejecutamos el "catkin build"*

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/
catkin build  
```

*Con lo anterior es posible que arroje un error, por lo cual debemos modificar el documento en el explorador de archivos, en la siguiente ruta :* 

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/src/orb_slam_2_ros/ 
gnome-open CMakeLists.txt
```

*Una vez abierto el documento, nos situamos en la linea 26 para realizar el cambio, iniciando en "find_pakage hasta la linea 35 donde termina el ")", procedemos a desbloquearlas, para ello debemos eliminar el "#"; para confirmar que estan desbloqueadas los sabemos porque pasan de color azul a color blanco, guardamos el archivo y volvemos a construirlo con el catkin build.*

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/
catkin clean
catkin build
```

*Sin embargo es posible que arroje errores como pangolin y eigen3, por lo cual para solucionarlos, ejecutamos los siguientes comandos; antes de proceder, debemos confirmar que estén instalados, para ellos ingresamos:*

```bash
dpkg --get-selections |grep Eigen3
```

```bash
apt search Eigen3  
```

*Para solucionar este error, debemos entrar en la siguiente ruta:*

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/src/orb_slam_2_ros/orb_slam2/cmake_modules
```

```bash
ll
```
*Una vez lo listemos ingresando "ll", nos aparecerá el nombre del archivo findEigen3.cmake * procedemos a eliminarlo y nuevamente listamos ingresando "ll"*

```bash
rm -rf ./*
```

*Volvemos a nuestra carpeta catkin_ws, para ello ejecutamos esta ruta:*

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws
```

*Limpiamos nuestra proyecto para no tener errores. NOTA (El siguiente comando lo ejecutamos en la misma carpeta "catkin_ws"*

```bash
catkin clean 
```
```bash
catkin build 
```

*Descargar archivo* [**Aquí**](https://gitlab.com/semillerodronotica/semillerodronotica/-/blob/reycheldev/documentacionGuia/CMakeLists.txt) *CMakeLists.txt, copiar el código del documento descargado, el cual se encuentra en la carpeta descargas del explorador de archivos y remplazarlo en la ruta:* 

```bash

cd ~ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/src/orb_slam_2_ros 
gnome-open CMakeLists.txt

```

*Volvemos a construir desde la (terminal) en la ruta* 

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/
```

```bash
catkin build
```

*Para solucionar el error del opencv vamos a la siguiente ruta en el explorador de archivos:*

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/src/orb_slam_2_ros/orb_slam2/include 
gnome-open ORBextractor.h
```

*Una vez estemos abramos el archivo ORBextractor.h, reemplazamos la línea 26 por lo siguiente: #include <opencv2/opencv.hpp>. Nos volvemos a situar en nuestra terminal* 

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/ 
```

*Y volvemos a construir*

```bash
catkin clean
catkin build
```

*En caso de error del cv_GRAY2BGR vamos a la siguiente ruta en nuestro explorador de archivos:*

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/src/orb_slam_2_ros/orb_slam2/src 
gnome-open FrameDrawer.cc 
```

Cambiamos en la linea 75 cvtColor(im,im,cv::COLOR_GRAY2BGR);
  
*Ahora abriremos esta nueva ruta en el explorador de archivos:* 

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/src/orb_slam_2_ros/orb_slam2/include 
gnome-open PnPsolver.h 
``` 

Nos situamos en la linea 57 y agregamos lo siguiente: #include<opencv2/core/core_c.h>  y guardamos

*Descarga el archivo [**aquí**](https://gitlab.com/semillerodronotica/semillerodronotica/-/blob/desarrollo/documentacionGuia/Tracking.cc) copiar el código del documento descargado, el cual se encuentra en la carpeta descargas del explorador de archivos y reemplazar el código del archivo que tenemos ubicado en la ruta del explorador:*

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/src/orb_slam_2_ros/orb_slam2/src 
gnome-open Tracking.cc 
``` 

*Guardamos*

*Entramos nuevamente a la ruta de nuestro explorador de archivos:* 

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/src/orb_slam_2_ros 
gnome-open CMakeLists.txt
```

Nos situamos en la linea 37 la cual posee este texto: find_package(Eigen3.3.1.0 REQUIRED)
**No en todos los casos se encuentra la línea anterior, sino se visualiza dentro del archivo, hay que agregarlo**

*Ingresamos a la siguiente ruta a través del explorador de archivos:*


```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/ tello_catkin_ws/src/orb_slam_2_ros/orb_slam2/cmake_modules
ll
```
*Borramos el archivo FindEigen3.cmake (No en todos los casos se encuentra este archivo, en caso de que exista, ingresar el siguiente comando para eliminarlo)*


```bash
rm -rf FindEigen3.cmake
```
*Y volvemos a construir en la siguiente ruta:*

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws
```

```bash
catkin clean
catkin build
```

*En caso de presentar error, ingresamos al explorador de archivos en la siguiente ruta:*


```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/src/orb_slam_2_ros/orb_slam2/src 
gnome-open Sim3Solver.cc 
```

En la línea 23 incluimos: #include<opencv2/highgui/highgui_c.h>

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws
catkin clean
catkin build
```

*Una vez completada la instalación al 100% procedemos a lanzar el roslaunch*

*Descargar [aquí](https://gitlab.com/semillerodronotica/semillerodronotica/-/blob/desarrollo/documentacionGuia/tello_ui.py) copiar el código del documento descargado, el cual se encuentra en la carpeta descargas del explorador de archivos y remplazar  en la siguiente ruta del explorador de archivos:*

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/src/flock/flock_driver/src 
gnome-open tello_ui.py 
```

Para solucionar el error de la ventana del tello controller


```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws
source devel/setup.bash
roslaunch flock_driver orbslam2_with_cloud_map.launch  
```
*Nos situamos en la terminal y presionamos CTRL + C para detener la ejecución del launch*

Nota: En caso de que solicite permisos de usuario, se lista en la carpeta con 

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/src/flock/flock_driver/src
ls -l
```

Y verifica que se encuentre el archivo tello_ui.py, una vez encontrado asignarle permisos de lectura, escritura y ejecución para el usuario, el grupo y otros; con el siguiente comando

```bash
sudo chmod 777 tello_ui.py
```
Posicionarse en el core del proyecto, ingresa la siguiente serie de comandos con los cuales ejecutaremos el entorno de Ros y realizaremos el lanzamiento de ORBSLAM2: 

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws
source devel/setup.bash
roslaunch flock_driver orbslam2_with_cloud_map.launch  
```
*Nos situamos en la terminal y presionamos CTRL + C para detener la ejecución del launch*

*Estos errores los solucionamos reemplazando estos archivos  en nuestro proyecto,  lo que debemos hacer es entrar al explorador de archivos en esta ruta:*


```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/src/flock/flock_driver/src/ 
```

*(Buscar) y [descargar cloud_map_saver.py](https://gitlab.com/semillerodronotica/semillerodronotica/-/blob/desarrollo/documentacionGuia/cloud_map_saver.py), [descargar flock_driver.py](https://gitlab.com/semillerodronotica/semillerodronotica/-/blob/desarrollo/documentacionGuia/flock_driver.py) y [descargar tello_slam_control.py](https://gitlab.com/semillerodronotica/semillerodronotica/-/blob/desarrollo/documentacionGuia/tello_slam_control.py), se deben copiar de la carpeta descargas en el explorador de archivos y pegar en la ruta mencionada anteriormente*

**Es obligatorio realizar el reemplazo de los códigos (archivos) anteriores, ya que, esto nos remplaza las siguientes líneas que causan errores en la ejecución:**


*ERROR :[cloud_map_saver-4] process has died [pid 99749, exit code 127, cmd /home/<usuario>/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/src/flock/flock_driver/src/cloud_map_saver.py __ name:=cloud_map_saver __ log:=/home/<usuario>/.ros/log/1a3b403e-ab0b-11ec-9491-9d84c1e0ee72/cloud_map_saver-4.log].*
*log file: /home/<usuario>/.ros/log/1a3b403e-ab0b-11ec-9491-9d84c1e0ee72/cloud_map_saver-4*.log*
*[flock_driver_node-5] process has died [pid 99750, exit code 127, cmd /home/<usuario>/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/src/flock/flock_driver/src/flock_driver.py __ name:=flock_driver_node __ log:=/home/<usuario>/.ros/log/1a3b403e-ab0b-11ec-9491-9d84c1e0ee72/flock_driver_node-5.log].*
*log file: /home/<usuario>/.ros/log/1a3b403e-ab0b-11ec-9491-9d84c1e0ee72/flock_driver_node-5*.log*
*[tello_slam_control-6] process has died [pid 99751, exit code 127, cmd /home/<usuario>/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/src/flock/flock_driver/src/tello_slam_control.py __ name:=tello_slam_control __ log:=/home/<usuario>/.ros/log/1a3b403e-ab0b-11ec-9491-9d84c1e0ee72/tello_slam_control-6.log].*
*log file: /home/<usuario>/.ros/log/1a3b403e-ab0b-11ec-9491-9d84c1e0ee72/tello_slam_control-6*.log*

*Volvemos a ejecutar nuestro roslaunch flock_driver orbslam2_with_cloud_map.launch*

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws
source devel/setup.bash
roslaunch flock_driver orbslam2_with_cloud_map.launch  
```
*Nos situamos en la terminal y presionamos CTRL + C para detener la ejecución del launch*

*Una vez ya ejecutado el roslaunch nos saldrá un error en la terminal, informando que no encuentra la versión requerida de tellopy instalada. Lo que tenemos que hacer, es desinstalarlo en una nueva terminal ubicandonos en la siguiente ruta:*

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/TelloPy
sudo pip3 uninstall tellopy
```

*Procedemos a instalarlo en la misma ruta (cd ~/ROS/Tello_ROS_ORBSLAM/TelloPy)  para ello usamos este comando.*
```bash
cd ~/ROS/Tello_ROS_ORBSLAM/TelloPy
sudo apt-get install python3-pygame
pip3  install tellopy 
sudo apt install python3-pip
pip install av
pip3 list
```

*Ahora se debe ingresar desde el explorador de archivos, en esta ruta:*


```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/src/flock/flock_driver/src 
gnome-open flock_driver.py  
```

En la linea 90 del codigo rospy.Subscriber(self.publish_prefix+'cmd_vel', Twist, self.cmd_vel_callback) si no está, la agregamos y guardamos, volvemos a revisar en ese mismo archivo  flock_driver.py   :  hay que corregir la información en la linea 13  Ejemplo: import telloPy la dejamos tal cual esta en el Ejemplo, guardamos y volvemos a ejecutar nuestro roslaunch flock_driver orbslam2_with_cloud_map.launch

*En la misma ruta  del explorador de archivos:*  

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/src/flock/flock_driver/src 
gnome-open tello_keyboard.py  
```

En la linea 1  y la dejamos tal cual esta aqui  #!/usr/bin/env python3 y guardamos.

 
*Luego buscamos en esta ruta en el explorador de archivos carpeta personal:* 

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/src/flock/flock_driver/launch 
gnome-open orbslam2_with_cloud_map.launch 
```

Reemplazamos en la linea 67 hasta la 72 tal cual esta en el ejemplo:
 
```bash
 ## <node name="tello_keyboard_node" pkg="flock_driver" type="tello_keyboard.py" output="screen">
 ##    <remap from="/tello/cmd_vel" to="/tello0/cmd_vel" />
 ##     <remap from="/tello/takeoff" to="/tello0/takeoff" />
 ##     <remap from="/tello/land" to="/tello0/land" />
 ## </node>
```

*Ejecutar en la terminal:*
                   
```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws
source devel/setup.bash
roslaunch flock_driver orbslam2_with_cloud_map.launch  
```
### Manual de conexión para el dron DJI TELLO con pc por medios no guiados

Ingrese a [***CONEXION DRON***](https://gitlab.com/semillerodronotica/semillerodronotica/-/blob/desarrollo/documentacionGuia/conexionDron.md)

[comment]: <> (Guia_Vision_Artificial.md)

# Guía visión artificial 


### Fuentes

https://wiki.ros.org/hector_quadrotor

### Requisitos previos

Sistema operativo Linux – Ubuntu 20.04
rosdistro: noetic
rosversion: 1.15
Gazebo

## Pasos

### 1) Abrir una terminar y crear carpeta con sub carpeta src
```bash
mkdir -p ~/hector_cam/src
```
### 2) Abrir carpeta src
```bash
cd  ~/hector_cam/src
```
### 3) instalar paquetes necesarios dentro de la carpeta src
```bash
git clone https://github.com/tu-darmstadt-ros-pkg/hector_quadrotor.git
git clone https://github.com/tu-darmstadt-ros-pkg/hector_slam.git
git clone https://github.com/tu-darmstadt-ros-pkg/hector_localization.git
git clone https://github.com/tu-darmstadt-ros-pkg/hector_gazebo.git
git clone https://github.com/tu-darmstadt-ros-pkg/hector_models.git

```
### 4) salir de src
```bash
cd ..
```
### 5) Instalar dependencias necesarias de ROS
```bash
rosdep install -y --from-paths . --ignore-src --rosdistro noetic
```
### 6) Cree el espacio de trabajo de catkin
```bash
catkin_make
source devel/setup.bash
```
### 7) salir de hector_cam
```bash
cd ..
```
### 8) Para poder utilizar el dron con el teclado se debe instalar el siguiente paquete, ejecute el codigo indicado en una terminal.
```bash
sudo apt-get install ros-noetic-teleop-twist-keyboard
```
## LAUNCH

Al realizar la clonación de los paquetes indicados anteriormente, se realizó la instalación de dos mundos en gazebo, uno donde se evidencia una simulación al aire libre y otro donde se evidencia una simulación de interiores.

### 1) Se debe abrir una terminal e ingresar a la carpeta hector_cam:
```bash
cd  ~/hector_cam
```
### 2) Ejecutar el archivo .bash con el siguiente comando
```bash
source devel/setup.bash
```
### 3) Para abrir la simulación del mundo deseado ejecute el comando apropiado en la terminal: 

### 3.1) 1.	Lanzar simulador al aire libre
```bash
roslaunch hector_quadrotor_demo outdoor_flight_gazebo.launch
```
### 3.2) 2.	Lanzar simulador en interiores.
```bash
roslaunch hector_quadrotor_demo indoor_slam_gazebo.launch
```
## Controles

### 1) Luego de tener el launch corriendo se debe abrir otra terminal e ingresar a la carpeta hector_cam:
```bash
cd  ~/hector_cam
```
### 2) Ejecutar el archivo .bash con el siguiente comando:
```bash
source devel/setup.bash
```
### 3) . ejecutar el comando rostopic list
```bash
rostopic list
```
### 4). Se deben encender los motores del dron utilizando el siguiente comando: 
```bash
rosservice call /enable_motors "enable: true"
```
### 4.1) Para utilizar el dron con el control de **XBOX** se debe lanzar el siguiente comando:
```bash
roslaunch hector_quadrotor_teleop xbox_controller.launch
```
### 4.2) Para utilizar el dron con el **TECLADO** se debe lanzar el siguiente comando:
```bash
rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```
### 4.2.1 Utilizar el dron desde el teclado
Moverse:
   u   i    o
   j    k    l
   m    ,    .

t : arriba (+z)
b : abajo (-z)

Q: Detener

q/z: aumenta/disminuye las velocidades máximas en un 10 %
w/x: aumenta/disminuye solo la velocidad lineal en un 10%
e/c: aumenta/disminuye solo la velocidad angular en un 10%

CTRL-C para salir

## Posibles errores

Si presenta el siguiente error **The traceback for the exception was written to the log file** realice los sigueintes pasos:

### 1) ingrese a la siguiente ruta desde el gestor de documentos. 

hector_cam/src/hector_quadrotor/hector_quadrotor_demo/launch

### 2) abrir el archivo indoor_slam_gazebo.launch

### 3) cambiar la linea 24 por la siguiente linea:
```bash
<include file="$(find hector_geotiff_launch)/launch/geotiff_mapper.launch">
```
### 4) Guardar y cerrar.
### 5) volver a ejecutar el launch del simulador de interiores 
```bash
roslaunch hector_quadrotor_demo indoor_slam_gazebo.launch
```

[comment]: <> (instalacionRosNoetic.md)

# Guia para la instalación del espacio de trabajo en ROS version Noetic  
## Documentación Guía  

[**Git Hub Tello_ROS_ORBSLAM**](https://github.com/tau-adl/Tello_ROS_ORBSLAM)  

## Instalar requisitos previos  
### herramientas de captura  

*Primero debe tener los repositorios ROS que contienen el .deb para catkin_tools:*

```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu `lsb_release -sc` main" > /etc/apt/sources.list.d/ros-latest.list'
wget http://packages.ros.org/ros.key -O - | sudo apt-key add -
```
*Una vez que haya agregado ese repositorio, ejecute estos comandos para instalar catkin_tools:*

```bash
sudo apt-get update
sudo apt-get install python-catkin-tools
```

# Eigen3
*Requerido por g2o. Las instrucciones de descarga e instalación se pueden encontrar aquí. De lo contrario, Eigen se puede instalar como binario con:*

```bash
sudo apt install libeigen3-dev
```
# ffmpeg

```bash
sudo apt install ffmpeg
```

# Herramientas de Python catkin (probablemente ya instaladas)

```bash
sudo apt-get install python-catkin-tools
```
# Requisitos previos basados en Github

## Pangolin (usado en orbslam2)

*Basado en https://github.com/stevenlovegrove/Pangolin*

```bash
cd ~  
mkdir ROS  
cd ~/ROS/  
git clone https://github.com/stevenlovegrove/Pangolin.git  
sudo apt install libgl1-mesa-dev  
sudo apt install libglew-dev  
sudo apt-get install libxkbcommon-dev  
cd Pangolin  
mkdir build  
cd build  
cmake ..  
cmake --build .  
```
# decodificador h264

*basado en https://github.com/DaWelter/h264decoder*

```bash
cd ~/ROS/  
git clone https://github.com/DaWelter/h264decoder.git
cd h264decoder  
mkdir build  
cd build  
cmake ..  
make  
```
*ahora cópielo en la ruta de Python* 

```bash
sudo cp ~/ROS/h264decoder/libh264decoder.so /usr/local/lib/python3.8/dist-packages
```
# Instalación de nuestro repositorio

## Clonación de nuestro repositorio de github

 ```bash
cd ~  
mkdir ROS  
cd ROS  
git clone https://github.com/tau-adl/Tello_ROS_ORBSLAM.git  
```

# Instalando nuestra versión de TelloPy

*basado en https://github.com/dji-sdk/Tello-Python y https://github.com/hanyazou/TelloPy*

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/TelloPy  
sudo python setup.py install  
```

# Instalación de dependencias para ROS

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/  
sudo rosdep init  
rosdep update  
rosdep install --from-paths src --ignore-src -r -y  
```

# Instalación de orbslam2

*basado en https://github.com/appliedAI-Initiative/orb_slam_2_ros y https://github.com/rayvburn/ORB-SLAM2_ROS Primero, si usa la versión melódica de ROS, cambie ~ / ROS / Tello_ROS_ORBSLAM / ROS / tello_catkin_ws / src / orb_slam_2_ros / CMakeLists.txt A CMakeLists_melodic.txt*

## Construye el código:

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/  
catkin init  
catkin clean  
catkin build .
```
## Agregue la configuración del entorno a bashrc

```bash
echo "source $PWD/devel/setup.bash" >> ~/.bashrc  
source ~/.bashrc  
```

# Instalación de ccm_slam

*basado en https://github.com/VIS4ROB-lab/ccm_slam*

### Compile DBoW2:

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/ccmslam_ws/src/ccm_slam/cslam/thirdparty/DBoW2/  
mkdir build  
cd build   
cmake ..  
make -j8    
```

# Compile g2o:

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/ccmslam_ws/src/ccm_slam/cslam/thirdparty/g2o  
mkdir build  
cd build  
cmake --cmake-args -DG2O_U14=0 ..  
make -j8    
```

# Descomprimir vocabulario:

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/ccmslam_ws/src/ccm_slam/cslam/conf
unzip ORBvoc.txt.zip
```

# Construye el código:

```bash
cd ~/ROS/Tello_ROS_ORBSLAM/ROS/ccmslam_ws/  
source /opt/ros/melodic/setup.bash  
catkin init  
catkin config --extend /opt/ros/melodic  
catkin build ccmslam --cmake-args -DG2O_U14=0 -DCMAKE_BUILD_TYPE=Release  
```

# Agregue la configuración del entorno a bashrc

```bash
echo "source $PWD/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

[comment]: <> (rosConexionTello.md)

# Conexión a dron tello con ros y python

## Pasos

1) - Crear espacio de trabajo con el comando:  

```bash
mkdir -p ~/flock_catkin_ws/src
```

Una ves creado el espacio de trabajo clone el siguiente repositorio [clydemcqueen-flock.git](https://github.com/clydemcqueen/flock.git) en la ruta **src** del proyecto, comandos:  

```bash
cd  ~/flock_catkin_ws/src
git clone https://github.com/clydemcqueen/flock.git
```

Después de clonar el proyecto proceda a construir el espacio de trabajo con catkin_make como se muesra a continuación

```bash
cd  ~/flock_catkin_ws
catkin_make
```

***Nota:*** la construcción del paquete se realiza con **catkin_make** esta construcción se usa para ros-melodic para este caso la version es ros-noetoc se realiza con **catking build**
 
## Compilar archivo con python  

### Este archivo es para verificación de conexión entre el dron en fisico con señales codificadas en python, aclarando que el dron debe estar conectado al equipo por medios no guiados (WIFI)

***Compile desde una terminal***

```bash
cd ~
python3 flock_catkin_ws/src/flock/flock_driver/scripts/environment_test.py
```

Esto debe mostrar la camara del dron, si requiere saber todods los parámetros codificados ingrese al archivo y verifiquelo  


desde su usuario modifique el archivo teleop.launch con el siguiente comando


```bash
cd ~
vim flock_catkin_ws/src/flock/flock_base/launch/teleop.launch
```

Debe quitar las siguienetes lineas


con el comando **roslaunch** realice el lanzamiento


```bash
cd ~/flock_catkin_ws/
source devel/setup.bash
roslaunch flock_base teleop.launch
```

[comment]: <> (rosNoeticGazebo.md)

# Guía para manejo de dron simulado hector_quadrotor en el simulador Gazebo

### 2) Instalando Ros-Noetic

A través de la siguiente guía se realizará la configuración de **ROS** y el simulador **GAZEBO** con el dron **hector quadrotor**   

Una vez se haya realizado la instalación de ros noetic 2.1 **GUIA DE INSTALACIÓN** [ROS-NOETIC](http://wiki.ros.org/noetic/Installation/Ubuntu) en el sistema operativo ***UBUNTU 20.04*** procedemos a realizar la configuración necesaria para empezar a simular el dron **hector quadrotor** en el entorno de **GAZEBO**   

**NOTA:** Para realizar estas configuraciones se debe tener conocimientos básicos en el manejo de comandos de terminal para el sistema operativo Linux version UBUNTU 20.04, se recomienda realizar la inscripción del [curso Python para Robótica](https://app.theconstructsim.com/#/Courses)

### 3) Instalando dependencias para Ros-Noetic

```bash
sudo apt-get install ros-noetic-ros-control ros-noetic-gazebo-ros-control ros-noetic-laser-geometry
sudo apt-get install ros-noetic-unique-identifier ros-noetic-tf2-geometry-msgs
sudo apt-get install ros-noetic-geographic-info ros-noetic-tf-conversions ros-noetic-joy
```

### 4) Crear el espacio de trabajo en el path del usuario

```bash
mkdir -p ~/hector_ws/src 
cd ~/hector_ws/src 
```

### 5) Clonando proyecto para el dron simulado hector_quadrotor

```bash
git clone -b kinetic-devel https://github.com/tu-darmstadt-ros-pkg/hector_quadrotor.git
git clone -b catkin https://github.com/tu-darmstadt-ros-pkg/hector_localization.git
git clone -b kinetic-devel https://github.com/tu-darmstadt-ros-pkg/hector_gazebo.git
git clone -b kinetic-devel https://github.com/tu-darmstadt-ros-pkg/hector_models.git
cd ..
catkin_make ##Para ros-melodic debe usarse catking_build 
source devel/setup.bash 
```

***Nota:*** Para ros-melodic, la construcción del paquete se realiza con **catkin_make**,  como en este caso la version es ros-noetic se debe ingresar con **catking build**

### 6) Ingresar espacio de trabajo en variables de entorno - archivo .bashrc

```bash
cd ~
vim .bashrc
```

***NOTA:*** **VIM** es un editor de texto el cual se usó para esta parametrización, siéntase libre de usar el editor de su preferencia.

**Abrir archivos en VIM** ***vim ruta archivo/***
**COMANDOS BÁSICOS**

| Función VIM | Comando | Descripción |
|--|--|--|
| Insertar | i | Este comando nos permite escribir sobre el fichero seleccionado|
| Guardar | esc : w | Este comando nos permite guardar el archivo teniendo permisos sobre el mismo |
| Salir | esc : q | Este comando nos ppermite salir del editor de texto | 
| Guardar y salir | esc : x | Este comando permite guardar y salir del editor |

**Dentro del editor de texto de Vim, al final del fichero, agregamos el espacio de trabajo a la variable de entorno con la siguiente línea:**

```bash
source ~/hector_ws/devel/setup.bash
```

Una vez se agregue el comando anterior en el archivo .bashrc, guardamos y salimos del editor con los comandos de la tabla, sí se está usando Vim.

### 7) Realizar la actualización de variables de entorno desde la consola.

```bash
cd ~/.bashrc
source .bashrc
```

### 8) Conectarnos al Ros master

Abrimos nueva terminal con **CTRL + T** y ejecutamos el siguiente comando:

```bash
cd ~
cd hector_ws/
source devel/setup.bash ##En cada terminal que se abre, digitar para obtener paquetes
roscore 
```

### 9) Para dar inicio a la simulación abrimos una nueva terminal y ejecutamos el siguiente comando, el cual recreará el mundo vacio en Gazebo, haciendo el lanzamiento del dron:


```bash
source devel/setup.bash
roslaunch hector_quadrotor_gazebo quadrotor_empty_world.launch
```

Una vez ejecutado el comando, si el procedimiento se realizó con éxito, aparecerá el dron en el eje central del mundo vacio de gazebo.  

Ahora se hace necesario conocer los tópicos y servicios que tenemos dentro del proyecto, para con ellos poder realizar correctamente la ejecución del dron en Gazebo

### 10) Visualizar tópicos:

Los tópicos, son una serie de mensajes que nos transmiten información de ejecución en tiempo real sobre los nodos que están interactuando. 

Realizar la apertura de una nueva terminal y ejecutar el siguiente comando con el cual listaremos los tópicos de Ros y Gazebo: 


```bash
rostopic list
```

### 11) Servicios: 

Listamos una serie de servicios que se lanzan una vez se ha realizado las parametrizaciones de hector_quadrotor sobre el mundo vaciode Gazebo, con el fin de ubicar el de /enable_motors ya que éste parámetro dentro del lanzador principal, viene por defecto, deshabilitado. Modificamos el comando, indicando que deseamos obtener los servicios en Ros y ejecutamos 

```bash
rosservice list
```

Una vez listados, buscamos el servicio de ***/enable_motors***, en caso de que este aparezca de la siguiente forma ***rosservice call /enable_motors "enable: false"***, debemos cambiar el **false** por **true** y así encenderemos los motores del Dron

```bash
rosservice call /enable_motors "enable: true"
```

Inmediatamente el cambio se haya realizado se publican las velocidades con el siguiente comando

```bash
rostopic pub -r 20 /cmd_vel geometry_msgs/Twist
```
Cuando se coloca el comando en consola damos un espacio y tabulamos esto nos iniciará dos matrices de dos por 3 las cuales permiten modificar el inicio de vuelo cambiando parámetros de velocidades

## 12) Parámetrización para el vuelo del dron con mando de XBOX

Una vez realizado todos los pasos anteriores se debe seguir la guia [seguimiento de trayectorias](https://gitlab.com/semillerodronotica/semillerodronotica/-/blob/desarrollo/documentacionGuia/segumientoTrayectoriaGazeboRos.md) con el fin de poder  manipular el dron con un mando (control).

[comment]: <> (segumientoTrayectoriaGazeboRos.md)

**Para continuar con el desarrollo de la guía se requiere tener el mando de Xbox con el cual se realizará la conexión**


### 13)  Ingreso al espacio de trabajo

Abrimos una nueva terminal y ejecutamos el siguiente comando:

```bash
cd ~/hector_ws/src
```

### 14) Descargamos el paquete [**my_hector_uavs**](https://gitlab.com/semillerodronotica/semillerodronotica/-/blob/desarrollo/my_hector_uavs.zip)

Una vez descargado lo debemos copiar en el entorno de trabajo en la carpeta source (src) desde descargas se realiza con el siguiente comando

```bash
cp -rp ~/Descargas/my_hector_uavs.zip ~/hector_ws/src
```

**Nota:** Se debe tener instalado **gzip y zip** para proceder a descomprimir el paquete  

Para verificar si ya se encuentra instalado, ingresar el siguiente comando:

```bash
dpkg --get-selections |grep zip
```

En caso de no tener la instalaciónm realizarla mediante el siguiente código:

```bash
sudo apt install gzip zip -y
```
Se debe ubicar en el espacio de trabajo y descomprimir el proyecto

```bash
cd ~/hector_ws/src 
unzip my_hector_uavs.zip
```
### 15) Descargar el proyecto de flock en el siguiente link [FLOCK](https://github.com/clydemcqueen/flock)

```bash
cd ~/hector_ws/src 
git clone https://github.com/clydemcqueen/flock.git
```
Cuando se haya completado la descarga del repositorio, nos dirijimos al siguiente link y procedemos a realizar la descarga de los archivos **my_hector_uav.launch** y **flock_base.py** los cuales se encuentran en el zip descargable llamado lanzadores, el cual se encuentra a través del link

[lanzadores](https://gitlab.com/semillerodronotica/semillerodronotica/-/blob/desarrollo/lanzadores.zip)  

Se debe descomprimir el paquete para reemplazar los archivos de la siguiente manera: 

```bash
cd ~/Descargas
unzip lanzadores.zip
```

Esto dejará una carpeta llamada **lanzadores**, ingresamos y realizamos el remplazo de archivos  

```bash
cd ~/Descargas/lanzadores
mv my_hector_uav.launch ~/hector_ws/src/my_hector_uavs/launch
mv flock_base.py ~/hector_ws/src/my_hector_uavs/scripts
```

### 16) Ejecutar comando para reconstruir nuestro espacio de trabajo. 

```bash
cd ~/hector_ws
catkin_make
```

Habiendo remplazado los archivos, realizamos lanzamientos previos para iniciar la manipulación de trayectorias con el mando de xbox. Para llevar a cabo esto, se debe crear la conexión al core master de Ros: 

```bash
cd ~/hector_ws
source devel/setup.bash
roscore
```

### 17) Lanzar dron quadrotor en gazabo

Se abre una nueva terminal (***CTRL+ALT+T***) y procedemos a realizar el lanzamiento de ***my_hector_uavs my_hector_uav.launch***

```bash
cd ~/hector_ws
source devel/setup.bash
roslaunch my_hector_uavs my_hector_uav.launch
```

### 18) Activando servicio de /enable_motors

```bash
rosservice call /enable_motors "enable: true"
```

Realiza la activación del servicio de /enable_motors y luego sobre el simulador damos en inicio (play)

### 19) Mando (control xbox)

Visualizar [diagrama de control](https://gitlab.com/semillerodronotica/semillerodronotica/-/blob/reycheldev/Diagramas/xbox%20Diagram.drawio.png) y manejo de botones para ejecutar movimientos del dron.

La conexión del control se realiza vía USB y/o Bluetooh, una vez el control esté conectado al equipo verificar que en la ruta ***/dev/input*** se encuentre el archivo de configuración del control llamado js0, luego de esto, procedemos a ejecutar el vuelo del dron hector cuadrotor con el mando.

### 20) Definición de desplazamientos

Sobre los ángulos X, Y y Z del simulador Gazebo y desplazamiento del dron real, la unidad de medida es en milimetros (mm).

### Proyecto ORB_SLAM

Para ambientar el proyecto de reconocimiento con puntos de profundidad para el dron dji tello dirijase al seiguiente apartado [**ORB_SLAM AMBIENTATION**](https://gitlab.com/semillerodronotica/semillerodronotica/-/blob/desarrollo/documentacionGuia/Guia_Instalacion_ORBSLAM%20finalizada.md)

[comment]: <> (UsosRos.md)

# Serie de comandos para manipular ROS

### Ingrese con su usuario del sistema al path principal

```bash
cd ~
roscd
cd ..
```
*Esto lo ubicará en la ruta* ***/ROS/Tello_ROS_ORBSLAM/ROS/tello_catkin_ws/*** *La cúal es el espacio de trabajo donde empezamos con la conexión a los servidores de ROS ejecutando el siguiente comando*

*Confirme su ruta con el comando*

```bash
source devel/setup.bash
```
