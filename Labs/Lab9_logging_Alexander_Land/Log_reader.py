import re

def readlog(logfilename):
    pattern = r''
    try:
        with open(logfilename) as file:
            lines = file.readlines()

            for line in lines:
                match = re.search(pattern, line)

                if match:
                    

    except Exception as e:
        print(f"error {e}")