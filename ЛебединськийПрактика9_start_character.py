import random
#встановлення та підключення наступних бібліотек Faker
from faker import Faker
fake = Faker()
all_names = {}
for z in range(1):    #возможно создание данных из нескольких локаций fake = Faker(['en_US', 'ja_JP'])
    fake = Faker(['en_US', 'ar_AE'])
    all_names.setdefault("name",[]).append(fake.name())
def character():
    gender_lst = ["male","female"]
    mood_lst = ["normal","good","angry","happy","sad"]
    name = all_names.get("name")
    age = random.randint(10,81)
    gender = random.choice(gender_lst)
    balance = random.randint(1000,100000)
    mood = random.choice(mood_lst)
    time_balance = random.randint(300,1000)
    return {"name": name,
            "age": age,
            "gender": gender,
            "balance": balance,
            "mood": mood,
            "time_balance": time_balance}
human = character()
print (human)