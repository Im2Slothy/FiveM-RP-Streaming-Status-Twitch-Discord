import os
import sys
import time

while True:
    print("Starting flask...")
    exit_code = os.system("python app.py")
    if exit_code == 0:  # 0 is a normal exit, any other value means an error or restart request.
        break
    print("Bot stopped with code", exit_code, ". Restarting in 5 seconds...")
    time.sleep(5)