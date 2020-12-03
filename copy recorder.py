import time,datetime
import sys
import os
import pyperclip
sys.path.append(os.path.abspath("SO_site-packages"))
def main():
    recent_value = ""

    while True:
        tmp_value = pyperclip.paste()
        if tmp_value != recent_value:
            try:
                today=datetime.date.today()
                today= today.strftime("%B %d,%Y")
                now=datetime.datetime.now()
                current_time = now.strftime("%H:%M:%S")

                f=open("paste.txt","a")
                recent_value = tmp_value
                f.write(f"{current_time,today}\n{recent_value}\n\n")
                f.close()
            except Exception as e:
                break
        
        time.sleep(1)
    
    main()

if __name__ == "__main__":
    main()

