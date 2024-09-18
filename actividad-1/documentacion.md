DOCUMENTACION DE LA ACTIVIDAD 1:

Preguntas de reflexion:
1. ¿Por qué surgió la necesidad de DevOps en el desarrollo de software?
   
   Surgió debido a que antes los equipos de desarrollo y operaciones trabajaban separados y habia demasiados problemas para que el software funcionara rapido y bien.
   
2. Explica cómo la falta de comunicación y coordinación entre los equipos de desarrollo y operaciones en el pasado ha llevado a la creación de DevOps.
   
   La creacion de DevOps fue para mejorar la comunicacion del equipo y para que se trabaje junto desde el principio ya que antes los equipos de devs y ops no se coordinaban bien y esto causaba retrasos y errores.
   
3. Describe cómo el principio de mejora continua afecta tanto a los aspectostécnicos como culturales de una organización.

   La mejora continua no solo busca mejorar herramientas o procesos sino tambien cambiar la actitud de las personas ya que todos deben estar abiertos a colaborar y aprender.
   
4. ¿Qué significa que DevOps no se trata solo de herramientas, individuos o procesos?
   
   Significa que no es suficiente con usar buenas herramientas o procesos si es que no hay trabajo en equipo ya que DevOps es mas una forma de trabajar juntos de manera mas efectiva.
   
5. Según el texto, ¿cómo contribuyen los equipos autónomos y multifuncionales a una implementación exitosa de DevOps?
    
   Contribuyen con habilidades variadas y el poder resolver problemas sin depender de otros lo que agiliza el desarrollo y mejora el flujo de trabajo.


   
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

Procedemos a automatizar el despliegue con Github Actions:
El cual para realizarlo tenemos que modificar el archivo ci.yml de la carpeta .github/workflows/ci.yml de la siguiente manera:
![image](https://github.com/user-attachments/assets/881bbaa0-049f-46d7-90e5-190e074a146c)

Ahora procedemos a correr el contenedor de Docker en el puerto 3000:
![image](https://github.com/user-attachments/assets/8e8440d9-fb5f-4b37-b068-fc60acad35e0)

En el navegador web podemos ver que la aplicacion se despliega correctamente:
![image](https://github.com/user-attachments/assets/e6c0e403-59ef-417d-bd45-7369ad04b233)

Y la visualizacion desde Github Actions seria asi:
![image](https://github.com/user-attachments/assets/d6267ee0-deb1-4e4d-aa37-accee14c4493)


Automatizacion con Docker Compose:
Primero creamos el docker-compose.yml y lo configuramos:
![imagen](https://github.com/user-attachments/assets/442c5627-f0d8-414a-bc56-9c02a1c93eec)

 Procedemos a correr la aplicacion usando Docker Compose:
 ![image](https://github.com/user-attachments/assets/bf299d26-0b69-4766-831a-498d4a26776b)








