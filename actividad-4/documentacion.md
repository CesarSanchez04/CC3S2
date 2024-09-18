Actividad 4: Explorando diferentes formas de fusionar en Git - Parte 1

FUSION FAST-FORWARD (git merge --ff): este tipo de fusion es de las formas mas simples de combinar ramas en git, pero solo si no se ha realizado ningun commit en la rama principal desde que se creó la rama caracteristica ya que este metodo lo que hace es mover el puntero HEAD de la rama principal al ultimo commit de la rama caracteristica

Primero procedemos a crear un nuevo repositorio llamado "try-fast-forward-merge" y dentro de el agregamos un archivo llamado README.md en la rama principal (main) y le aplicamos un commit llamado "Commit inicial en main"
![image](https://github.com/user-attachments/assets/1134ab24-98e6-433e-a606-2cbf60929ed3)

Ahora procedemos a crear y cambiar a una nueva rama llamada "add-description" en la cual haremos modificaciones al archivo README.md y luego le aplicaremos un commit llamado "Agregar descripcion al README.md"
![image](https://github.com/user-attachments/assets/820c7162-526f-4373-abc9-35cb34edb4ee)

Hasta el momento el log deberia de visualizarse de la siguiente manera:
![image](https://github.com/user-attachments/assets/e1997d79-9718-4266-9d1a-62dccddf8f9a)

Ahora cambiamos de vuelta a la rama "main" y realizaremos la fusión de fast-forward luego mostraremos el log
![image](https://github.com/user-attachments/assets/a4ca93d0-7abd-42cd-8074-44a8b5bc31dc)
Aqui podemos apreciar que el puntero HEAD se movio junto a la rama "main" al ultimo commit de la rama "add-description" logrando asi la fusión, cabe recalcar que este tipo de fusion solo es posible cuando luego de crear y hacer modificaciones en la nueva rama, no se debio haber hecho ningun cambio en la rama main, el grafico del log debiera ser asi: (imagen sacada de la actividad4)
![image](https://github.com/user-attachments/assets/ade001e3-97f9-4896-91a3-9d67dbb2998f)


FUSION NO-FAST-FORWARD (git merge --no-ff):

Primero procedemos a crear un nuevo repositorio llamado "try-no-fast-forward-merge" y dentro de el agregamos un archivo llamado README.md y le aplicamos un commit llamado "Commit inicial en main"
![image](https://github.com/user-attachments/assets/fcc6a5ff-8a1b-4185-83c1-8f8f7e3e2efe)

Ahora procedemos a crear y cambiar a la nueva rama "add-feature", luego modificamos el archivo README.md y le aplicamos un commit llamado "Implementar nueva caracteristica"
![image](https://github.com/user-attachments/assets/1b246387-62eb-467a-bfe8-7de6b9ecc884)

Ahora nos movemos a la rama "main" y realizamos la fusion no-fast-forward, luego visualizamos el log 
![image](https://github.com/user-attachments/assets/6bcfc601-7e5b-43fb-8e0c-8347c0d8a3a0)

FUSION SQUASH (git merge --squash):

Primero procedemos a crear un nuevo repositorio llamado "try-squash-merge" y dentro de el agregamos un archivo llamado README.md y le aplicamos un commit llamado "Commit inicial en main"
![image](https://github.com/user-attachments/assets/1c009a21-d24d-4bb6-87f7-d92ca6d5908a)

Ahora procedemos a crear y cambiar a la nueva rama "add-basic-files", luego agregamos el archivo CONTRIBUTING.md y le aplicamos el commit "Agregar CONTRIBUTING.md", luego agregamos el archivo LICENSE.txt y le aplicamos un commit llamado "Agregar LICENSE.txt"
![image](https://github.com/user-attachments/assets/2ba19069-619c-4599-ad26-f2588a931f0b)

Ahora cambiamos de vuelta a la rama "main" y realizamos la fusión squash, la cual hara que todos los commits realizados en la rama "add-basic-files" se combinan y se convierten en un solo commit en la rama "main", luego para completar la fusion squash se realiza un commit llamado "Agregar documentacion estandar del repositorio", luego visualizamos como quedo el log
![image](https://github.com/user-attachments/assets/821cddad-c067-4f30-8a98-9bc7f22b985f)







