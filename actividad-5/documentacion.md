Documentacion Actividad 5: Entendiendo git rebase y git cherry-pick

REBASE:
Procedemos a crear una nueva carpeta de trabajo llamada "try-git-rebase" y procedemos a crear dentro de ella un archivo README.md y le aplicamos un commit llamado "Commit inicial en main" luego creamos y nos movemos a la rama "new-feature" en la cual añadimos el archivo "NewFeature.md" y le aplicamos un commit llamado "Agregar nueva caracteristica"
![image](https://github.com/user-attachments/assets/04259c64-0466-461e-a091-41d3b18f6dc2)

Luego nos movemos a la rama "main" y agregamos un nuevo archivo llamado "Update.md" y le aplicamos un commit llamado "Update main"
![image](https://github.com/user-attachments/assets/e0372661-7c0b-4afb-be6e-f573e3b0c0fe)

Ahora procederemos a realizar el rebase de new-feature sobre main con los siguientes comandos y visualizaremos el historial de commits
![image](https://github.com/user-attachments/assets/57a72ad5-de78-44ad-92a4-888957b70174)

Ahora cambiamos a la rama "main" y realizamos una fusion fast-forward
![image](https://github.com/user-attachments/assets/08711082-435a-45b6-a229-8fd1ef5f5dd2)

CHERRY-PICK:
Primero procedemos a crear un nuevo repositorio llamado "try-cherry-pick" y procedemos a crear dentro de ella un archivo README.md y le aplicamos un commit llamado "Initial commit"
![image](https://github.com/user-attachments/assets/3eac0ecb-2ac0-4107-8929-372ea88f4185)

Luego procedemos a crear y cambiar a una nueva rama llamada "add-base-documents" en la cual creamos un archivo llamado CONTRIBUTING.md y le aplicamos un commit llamado "Add CONTRIBUTING.md"
![image](https://github.com/user-attachments/assets/081bca32-c1bf-494f-9008-c46217cee45c)

Luego añadimos el archivo LICENSE.txt y le aplicamos un commit llamado "Add LICENSE.txt", luego de eso visualizamos el log de la rama "add-base-documents"
![image](https://github.com/user-attachments/assets/cc6fcbf8-903e-40f5-812f-14f03bac3770)

Ahora procedemos a hacer cherry-pick de un commit de add-base-documents a main y revisamos el log de nuevo
![image](https://github.com/user-attachments/assets/c223ab70-30aa-4f36-948e-c00896a6f5b8)




