#welcome user 
#preload some feelings

#ask user how they are feeling right now the user chooses an emotion and the writes a small message with that emotion
#this will be stored in a dictionary as a key value pair
#the user can choose to add more feelings or quit
#the user must be able to view all their feelings and messages
#AND FILTER THEM BY EMOTION 


#save the emotion to a file

print("hello world welcome to the emotion tracker by yours truly kelly")
read = input("do you want to read your feelings from the file? (yes/no) ").lower()
if read == "yes":
    with open("feelings.txt", "r") as f:
        feelings = f.read()
        print(feelings)
else:
    print("ok, let's continue") 

    
emotion =["happy", "sad", "angry", "confused", "excited", "bored", "anxious", "lonely", "grateful", "hopeful"]
today_emotion = {}




while True:
    with open("feelings.txt", "a") as f:
        user_is_feeling = input(f"how are you feeling {emotion} today? ").lower()

        user_message = input("please write a small message about your feeling: ").capitalize().format()
        today_emotion[user_is_feeling] = user_message
        f.write(f"{user_is_feeling}: {user_message}\n")
        more = input("do you want to add more feelings? (yes/no) ").lower()
        if more == "no":
            break
        elif more == "yes":
            continue
        else:
            print("invalid input, please try again")
            continue

print(f"here is your log of you just wrote: {today_emotion}")


        

