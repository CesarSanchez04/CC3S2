DOCUMENTACION DE LA ACTIVIDAD 1:

En esta actividad se usará una aplicacion web sencilla utilizando Node.js en la cual devolverá un mensaje de "Hello, World!"

Configuracion del entorno: 
Primero instalamos las dependencias necesarias para la ejecucion del proyecto junto a la creacion de la estructura del mismo:

![imagen](https://github.com/user-attachments/assets/eb26d169-743d-4742-9e24-11a56acbb82c)

Ademas se escribio los siguientes codigos en los archivos correspondientes:

app.js
![imagen](https://github.com/user-attachments/assets/416dd031-89d8-4687-83b5-26162ecd586c)

app.test.js
![imagen](https://github.com/user-attachments/assets/c8dd9b5f-e92e-4396-831f-1e974b7c520a)

package.json
![imagen](https://github.com/user-attachments/assets/bcf65030-950b-4e60-93b5-0f95580b4a61)


Configuracion de la integracion continua (CI) con GitHub Actions:
se creó un archivo de configuracion para github actions creando la carpeta workflows dentro de la carpeta .github y dentro de workflows crear el archivo de configuracion ci.yml siendo un archivo oculto (-p)
![imagen](https://github.com/user-attachments/assets/1da97197-c154-4418-8a5d-22b627d7bf3f)

luego se subio a github los cambios realizados
![imagen](https://github.com/user-attachments/assets/f2b70906-9ca1-4eab-a3ec-aed10a6105b8)


Configuracion de entrega continua (CD) con Docker:
Primero instalamos y configuramos Dockers desde la consola
![imagen](https://github.com/user-attachments/assets/858ff564-6401-4f54-afb0-68087584b676)
![imagen](https://github.com/user-attachments/assets/13c92ba5-db5b-4e39-bc6d-687e732f6317)

Luego creamos un archivo Dockerfile y lo configuramos:
![imagen](https://github.com/user-attachments/assets/8958bf67-b6dc-43f4-a650-2d8350bd7f59)


Construimos la imagen de Docker y corremos el contenedor en el puerto 3000:
![imagen](https://github.com/user-attachments/assets/52f36790-b595-4604-ba48-f7f71eee002c)

Automatizacion con Docker Compose:
Primero creamos el docker-compose.yml y lo configuramos:
![imagen](https://github.com/user-attachments/assets/442c5627-f0d8-414a-bc56-9c02a1c93eec)
 







