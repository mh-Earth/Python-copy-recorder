from datetime import datetime
import time
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
                f=open("paste.txt","a")
                now = datetime.now()
                dt_string = now.strftime("Date------->"+"%B %d,%Y "+"Time------>"+"%H:%M:%S")

                recent_value = tmp_value
                f.write(f"------------------{dt_string}-----------------\n{recent_value}\n\n")
                f.close()
            except Exception as e:
                print(e)
        
        time.sleep(1)
    
    main()

if __name__ == "__main__":
    main()

