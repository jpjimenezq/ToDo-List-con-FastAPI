from fastapi import FastAPI
from pydantic import BaseModel
from db import get_connection
from typing import Optional
from fastapi import HTTPException


app = FastAPI()

class Task(BaseModel):
    id: Optional[int] = None
    titulo: Optional[str] = None
    completada: Optional[bool] = False
    usuario_id: int = None

class TaskUpdate(BaseModel):
    titulo: Optional[str] = None
    completada: Optional[bool] = None
    usuario_id: Optional[int] = None

class User(BaseModel):
    id: Optional[int] = None
    nombre: str
    correo: str

@app.get("/")
def read_root():
    return {"responde": "Hi! to the ToDo List"}

@app.get("/tasks/{id}")
def get_task(id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, titulo, completada, usuario_id FROM tareas WHERE id = %s", (id,))
        row = cursor.fetchone()

        conn.commit()

        if row is None:
            raise HTTPException(status_code=404, detail="Task not found.")

        cursor.close()
        conn.close()

        return {
            "id": row[0],
            "titulo": row[1],
            "completada": row[2],
            "usuario_id": row[3]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/create-task")
def create_task(tarea: Task):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO tareas (titulo, usuario_id) VALUES (%s, %s)",
            (tarea.titulo, tarea.usuario_id)
        )

        conn.commit()
        id_creado = cursor.lastrowid

        cursor.close()
        conn.close()

        return {
            "message": "Task created successfully",
            "task_id": id_creado,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/tasks/{id}")
def update_task(id: int, tarea: TaskUpdate):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        campos = []
        valores = []

        if tarea.titulo is not None:
            campos.append("titulo = %s")
            valores.append(tarea.titulo)

        if tarea.completada is not None:
            campos.append("completada = %s")
            valores.append(tarea.completada)

        if tarea.usuario_id is not None:
            campos.append("usuario_id = %s")
            valores.append(tarea.usuario_id)

        if not campos:
            raise HTTPException(status_code=400, detail="No se enviaron campos para actualizar.")

        valores.append(id)  # ID viene de la URL

        query = f"UPDATE tareas SET {', '.join(campos)} WHERE id = %s"
        cursor.execute(query, tuple(valores))
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Tarea no encontrada.")

        cursor.close()
        conn.close()

        return {"message": "Tarea actualizada correctamente"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/tasks/{id}")
def delete_task(id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tareas WHERE id = %s", (id,))

        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Task not found.")

        cursor.close()
        conn.close()

        return {"message": "Task deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/users/{id}")
def get_user(id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, correo FROM usuarios WHERE id = %s", (id,))
        row = cursor.fetchone()

        conn.commit()

        if row is None:
            raise HTTPException(status_code=404, detail="User not found.")

        cursor.close()
        conn.close()

        return {
            "id": row[0],
            "nombre": row[1],
            "correo": row[2]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/create-user")
def create_user(usuario: User):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO usuarios (nombre, correo) VALUES (%s, %s)",
            (usuario.nombre, usuario.correo)
        )

        conn.commit()
        id_creado = cursor.lastrowid

        cursor.close()
        conn.close()

        return {
            "message": "User created successfully",
            "user_id": id_creado,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))