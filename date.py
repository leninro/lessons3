# Задача 1
from datetime import datetime
dt_today = datetime.now()
dt_yest = datetime(2021, 5, 26, 8, 3, 44)
dt_mont_ago = datetime(2021, 4, 26, 8, 3, 44)
dt_mont_ago

# Задача 2
from datetime import datetime
date_string = "01/01/25 12:10:03.234567"
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
date_dt