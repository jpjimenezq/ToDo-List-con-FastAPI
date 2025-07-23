# 📝 ToDo API con FastAPI y MySQL

Este es un proyecto simple de backend construido con **FastAPI** y **MySQL**, que permite gestionar una lista de tareas asociadas a usuarios. Es ideal como base para aprender a integrar una API REST con una base de datos relacional.

---

## 🚀 Funcionalidades

- ✅ Crear usuarios
- ✅ Crear tareas asignadas a usuarios
- ✅ Obtener tareas y usuarios por ID
- ✅ Actualizar tareas parcialmente
- ✅ Eliminar tareas

---

## 📦 Instalación

1. **Clona este repositorio**:

   ```bash
   git clone https://github.com/tu_usuario/todo-fastapi.git
   cd todo-fastapi
   ```

2. **Instala las dependencias (se recomienda usar un entorno virtual)**:

   ```bash
   pip install fastapi uvicorn mysql-connector-python python-dotenv
   ```

3. **Configura tus variables de entorno en un archivo .env**:

   ```env
   HOST_DB=localhost
   USER_DB=tu_usuario_mysql
   PASSWORD_DB=tu_contraseña
   DATABASE_DB=proyectos
   ```

## 🗄️ Estructura esperada de la base de datos

**Asegúrate de tener una base de datos con las siguientes tablas**:

```sql
    CREATE TABLE usuarios (
        id INT PRIMARY KEY AUTO_INCREMENT,
        nombre VARCHAR(100),
        correo VARCHAR(100)
    );

    CREATE TABLE tareas (
        id INT PRIMARY KEY AUTO_INCREMENT,
        titulo VARCHAR(100),
        completada BOOLEAN DEFAULT FALSE,
        usuario_id INT,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
    );
```

## ▶️ Ejecutar el proyecto

**Usa uvicorn para iniciar el servidor local**:

```bash
    uvicorn main:app --reload
```

Esto levantará el servidor en http://127.0.0.1:8000.

También puedes acceder a la documentación interactiva en:
🔗 http://127.0.0.1:8000/docs

## 📌 Endpoints principales

🔹 **Usuarios**

- POST /create-user: Crear un nuevo usuario
- GET /users/{id}: Obtener un usuario por ID

🔹 **Tareas**

- POST /create-task: Crear una nueva tarea
- GET /tasks/{id}: Obtener una tarea por ID
- PUT /tasks/{id}: Actualizar parcialmente una tarea
- DELETE /tasks/{id}: Eliminar una tarea

## 🛠️ Tecnologías usadas

- FastAPI
- MySQL
- Python Dotenv

## 📚 Objetivo del proyecto

**Este proyecto fue creado como un ejercicio de aprendizaje para**:

- Construir una API RESTful moderna con FastAPI.
- Conectarse a una base de datos relacional (MySQL).
- Aplicar buenas prácticas en el manejo de errores y validaciones.
- Entender cómo organizar y escalar un backend desde lo más básico.

## 🧠 Próximas mejoras (ideas)

- Agregar paginación y filtros en las tareas.
- Validaciones de existencia de usuarios al crear tareas.
- Autenticación con tokens JWT.
- Dockerización del proyecto.
- Interface
