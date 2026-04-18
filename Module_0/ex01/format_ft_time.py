from datetime import datetime
import time

sec_from_epoch = time.time()

formatted = f'{sec_from_epoch:,.4f}'

scientific = f'{sec_from_epoch:.2e}'

print("Seconds since January 1, 1970: ", formatted,
      " or ", scientific, " in scientific notation")

today = datetime.now().strftime('%b %d %Y')

print(today, end="\n")
