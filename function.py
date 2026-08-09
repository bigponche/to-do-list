
def add_task(tasks, description):
    clean = description.strip()
    if clean == "":
        raise ValueError("add a valid text")  # ← tu turno: mensaje descriptivo
    new_task = {
        'description': clean,  # ← tu turno: qué valor va acá
        'completed': False,     # ← tu turno: qué valor inicial tiene este campo
    }
    tasks.append(new_task)  # ← tu turno: qué agregás a la lista
    return tasks 