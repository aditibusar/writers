import os
pid = os.fork()
if pid > 0:
    print("parent process: ")
    print("process ID:", os.getpid())
    print("chaild process ID:", pid)
else:
    print("child process:")
    print("Process ID:", os.getpid())
    print("parent process ID:", os.getppid())
        
