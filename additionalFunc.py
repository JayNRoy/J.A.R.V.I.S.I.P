"""
Additional functions useful in the assistant.
CLEAR TODO LIST FILE BEFORE DEPLOYMENT.
"""

def writeTodo(datainLst):
    try:
        data = ""
        for item in datainLst:
            data = data + item + "|"
        #data = data.encode("utf-8")
        myFile = open("todo.txt", "w", encoding="utf-8")
        myFile.write(data)
        myFile.close()
        return True
    except Exception as e:
        print(f"Unable to save changes todo list. Error detected: {e}")
        return False
    
def readTodo():
    myFile = open("todo.txt", "r", encoding="utf-8")
    data = myFile.read()
    #data = data.decode()
    myFile.close()
    todoList = data.split("|")
    if "" in todoList:
        todoList = todoList[0:len(todoList)-1]
    return todoList


