import sys
from datetime import datetime

def log(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = f'[{timestamp}] {message}'
    print(log_message, file=sys.stderr)
    return log_message          
    
a = input("Enter a string: ")
result = log(str(a))
print(result)