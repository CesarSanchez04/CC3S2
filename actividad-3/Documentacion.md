Actividad: Introduccion a Git - conceptos basicos y escenciales

git config: procedemos a configurar con nuestras credenciales el git
![imagen](https://github.com/user-attachments/assets/f15597c6-f1de-4f52-a434-11bec180cfe9)

git init: creamos la carpeta de trabajo y nos localizamos en ella
![imagen](https://github.com/user-attachments/assets/e72ec823-d78f-4e18-82a3-9664f9782f87)

git add: procedemos a crear un archivo md y ver el estado del archivo (git status) el cual nos sale como "untracked file", esto pasa ya que git detecta un cambio y no fue reconocido, para que git lo reconozca tenemos que usar el git add README.md, ahora cuando ponemos git status git va a reconocer el nuevo archivo
![imagen](https://github.com/user-attachments/assets/9b00b138-9e7b-4554-97f0-d45bb280886d)

git commit: este comando registra los cambios realizados y reconocidos por el git add en el historial del repositorio
![imagen](https://github.com/user-attachments/assets/65cc181f-b91b-4d04-a8c7-5b8657a712d4)

git log: muestra una lista de todos los commits realizados:
![imagen](https://github.com/user-attachments/assets/6cc55d79-69ad-4d13-b26b-ae59561e2772)

git branch: procedemos a crear una nueva rama y movernos a ella adeams de ver todas las ramas existentes
![imagen](https://github.com/user-attachments/assets/a405bc29-de91-4bc2-bd80-aaecf2249c6b)

![imagen](https://github.com/user-attachments/assets/25f564c5-39f5-413b-91a5-32fec50d3318)

git merge: procedemos a fusionar la rama develop con la main
![imagen](https://github.com/user-attachments/assets/b1368f27-e4ef-4590-8362-d67fd1b2114a)

git branch -d: procedemos a eliminar una branch que ya no usaremos
![imagen](https://github.com/user-attachments/assets/468b6f55-b6da-49ff-b617-3ddd2be301d0)

PREGUNTAS:

EJERCICIOS:

1) Practicar la creacion, fusion y eliminacion de ramas, asi como la resolucion de conflictos que puedan surgir durante la fusion
   
   Primero procedemos a crear una nueva rama llamada "feature/advanced-feature" y nos movemos a ella:
   ![image](https://github.com/user-attachments/assets/73be0965-6523-4269-9d26-81cf6ec5d3f0)

   Luego procedemos a añadir un archivo main.py a la nueva rama:
   ![image](https://github.com/user-attachments/assets/08ef4e3b-487c-4f8b-9894-7eb127c66506)

   Añadiendo y confirmando estos cambios en la rama "feature/advanced-feature"
   ![image](https://github.com/user-attachments/assets/4bd19d61-1320-4b06-847a-e936e45b0262)

   Cambiamos de nuevo a la rama "main" y procedemos a editar el archivo main.py de manera diferente (cambiando el mensaje del print), luego de esto añadimos y confirmamos los cambios en la rama main:
   ![image](https://github.com/user-attachments/assets/d9a13a50-168b-4fa7-b392-c430c0276fc8)

   Ahora procederemos a intentar fusionar la rama "feature/advanced-feature" en main, luego procedemos a resolver el conflicto generado en main.py, luego añadimos el archivo resuelto y completamos la fusion, y por ultimo eliminamos la rama fusionada:
   ![image](https://github.com/user-attachments/assets/59237507-fa3a-4b6a-949e-655e459ed03d)


2) Aprender a navegar y manipular el historial de commits usando comandos avanzados de Git

   Primero procedemos a ver el historial detallado de los commits:
   ![image](https://github.com/user-attachments/assets/a83376fa-b92d-4278-b055-e368a4dc21b8)

   ¿Que cambios fueron realizados en cada uno?
   del ultimo commit podemos ver que el cambio realizado es el cambio en el print de la actividad anterior

   Ahora procedemos a filtrar los commits por autor:
   ![image](https://github.com/user-attachments/assets/1244a8b5-a0f5-4774-91a1-5d2ab631d42f)
   


   

   

   
   

    





