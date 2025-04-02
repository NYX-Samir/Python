class ToDoList:
    def __init__(self):
        self.NewTask=list()
            
    def AddTask(self,Task):
        self.NewTask.append(Task)

    def DeleteTask(self,index):
        if 0<=len(self.NewTask):
            self.NewTask.pop(index)
        else:
            print("Invalid Index")
            
    def ViewAllTask(self):
        j=0
        for i in self.NewTask:
            print(f"{j}. {i}")
            j=j+1
    def MarkAsTask(self,Mark):
        if 0<=len(self.NewTask):
            self.NewTask[Mark] += " ✔️"
        else:
            print("Invalid Task Choice")            
task = ToDoList()
while True:        
    print("------To Do List------")
    print("1.Add Task")
    print("2.Delete Task")
    print("3.Mark Task as Done")
    print("4.View All Task")
    print("5.Exit")
    User_input = int(input("Selete Your Option : "))

    if User_input==1:
        print("Enter Your New Task")
        Ntask=input()
        task.AddTask(Ntask)
    elif User_input==2:
        task.ViewAllTask()
        delete=int(input("Selete Which Task You Want To remove : "))
        task.DeleteTask(delete)
    elif User_input==3:
        task.ViewAllTask()
        Mark=int(input("Selete Your Completed Task : "))
        task.MarkAsTask(Mark)
    elif User_input==4:
          task.ViewAllTask()
    elif User_input==5:
        break
    else:
        print("Invalid Choice")
    
