
from datetime import date

with open("mood_journal.txt", "a") as file:
    file.write(date.today().strftime("%Y-%m-%d") + "\n")
    feeling = input("are you feeling happy or sad today? >>>> answer with 'happy' or 'sad': ").lower()
    file.write(f"you are feeling {feeling}, and below tells you why \n")


    
    entry = input(f"write about today here and what made you feel like {feeling} ? >>>> ")
    file.write(f"{entry}\n")