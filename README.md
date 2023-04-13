<em> # La web de music </em>

<h1>Documentación</h1>
  <H2>Existen dos maneras de iniciar el proyecto.</h2>

<h1>OPCION 1 : Runear con docker</h1>

  <H3>Requisitos:
  Tener docker + docker-compose
  </h3>

  <H3>En la carpeta raiz debes ejecutar los siguientes comandos
  </h3>

  <h1>comando 1</h1>

  ```
  docker-compose build
  ```

  <H3>En caso de tener el docker con root anteponga sudo
  </h3>

  <h1>comando 2</h1>


  ```
  docker-compose up
  ```

  <H3>El proyecto runea en la dirección http://127.0.0.1:8005/
  </h3>

<h1>OPCION 2 : Runear en tu maquina</h1>
  

  
  
  <H3>Requisitos:
  Tener python 3.10 o superior instalado
  </h3>
  
  <H3>En la carpeta app debes ejecutar los siguientes comandos
  </h3>

  <h1>comando 1</h1>

  ```
  pip install -r requisitos.txt
  ```

  <h1>comando 2</h1>


  ```
  python manage.py runserver
  ```

  <H3>La aplicacion le indicara por consola en que url se inicia
  </h3>