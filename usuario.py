class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.tareas = []

    def agregarTarea(self, tarea):
        self.tareas.append(tarea)

    def listarTareas(self):
        for tarea in self.tareas:
            if tarea.estaLista():
<<<<<<< HEAD
                print(f"[X] {tarea.obtenerNombre()}" )

                print(f"[ ] {tarea.obtenerNombre()}" )
=======
                print(f"[X] {tarea.obtenerNombre()}" )
>>>>>>> 2fdcd8539444c39e5b5895b9306f7fe5f38a47eb
