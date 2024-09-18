Actividad 2:

Configuracion del entorno: Utilizaremos una aplicacion web sencilla construida con Node.js

Primero creamos el repositorio llamado "devops-practice" e inicializamos el proyecto de Node.js y luego instalamos las dependencias necesarias:
![image](https://github.com/user-attachments/assets/84680f13-75ca-4687-b32d-f1a648e5c58a)

Procedemos a crear la estructura del proyecto:
![image](https://github.com/user-attachments/assets/c2b757c1-d202-41ab-a0b1-fd5d74bf81c5)

Implementamos la API REST en src/app.js:
![image](https://github.com/user-attachments/assets/6903f0fe-1f8d-4915-992c-d3ed8f34c223)

Escribimos un test basico en tests/app.test.js:
![image](https://github.com/user-attachments/assets/aa9fea1c-3789-4d40-b2af-ba3956b2e61c)

Configuramos el package.json:
![image](https://github.com/user-attachments/assets/e6c6a271-cde9-47a1-b762-8030dc16b9cf)

Integracion de seguridad:

Primero configuramos una herramiento de analisas de seguridad estatica como npm audit:
![image](https://github.com/user-attachments/assets/d7ac378d-71ca-49a8-99c3-6841be045403)

Modificamos el ci.yml para incluir un paso de seguridad:
![image](https://github.com/user-attachments/assets/72a8353a-21e3-4c3c-ae0e-b2fc11a1d8f3)






