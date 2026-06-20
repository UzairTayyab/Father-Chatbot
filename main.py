print("================================")
print("      FATHER CHATBOT            ")
print("================================")
print("Type 'help' if you don't know what to ask, or 'bye' to exit.")

while True:
    question = input("\nAsk something about my father: ").lower()

    if "help" in question:
        print("You can ask me things like name, age, job, city, hobby, food, education, trait, or even our 'secret'!")
        
    elif "name" in question:
        print("My father's name is Tayyab Khan.")

    elif "age" in question:
        print("He's 56! He says he feels younger every year though, haha.")

    elif "job" in question or "work" in question:
        print("My father works as a Teacher.")

    elif "city" in question or "live" in question:
        print("My father lives in Jahanian.")

    elif "hobby" in question:
        print("My father's hobby is cooking.")

    elif "food" in question:
        print("He loves rice but honestly, he loves everything that his wife makes! 😅")

    elif "education" in question or "study" in question:
        print("My father has an MA degree.")

    elif "trait" in question or "personality" in question:
        print("His best trait is that he is very friendly not your typical strict father!")

    elif "secret" in question:
        print("Shh! Our family secret is that he makes the best tea in the house but he only makes that on special occasions!")

    elif "kitchen" in question or "cooking" in question:
        print("He's a natural! The kitchen is his happy place. \nHe gets so focused when he's cooking—it's like he's in his own world.")

    elif "relax" in question or "unwind" in question:
        print("He loves to just sit back. He’s earned it after his shift! \nWatching TV is his favorite way to switch off his brain and just chill.")

    elif "advice" in question:
        print("He’s not the type to lecture. He just drops one small, wise sentence \nthat makes me think for the rest of the day.")

    elif "mom" in question:
        print("They’re a team! He’s always looking out for her, \nand he genuinely thinks everything she cooks is a five-star meal!")

    elif "talk" in question or "thinker" in question:
        print("He’s definitely a thinker. He observes everything quietly, \nbut when he does talk, his jokes catch you totally off guard!")
        
    elif "happy" in question:
        print("He’s so lighthearted! When he’s happy, the whole house feels brighter. \nHe gets this big grin, and suddenly he's the one telling all the jokes.")

    elif "difficult" in question or "tough" in question:
        print("He’s really resilient. When things get tough, he doesn't complain. \nHe just takes a deep breath, prays, and finds a way to keep moving forward. I really admire that.")

    elif "son" in question or "proud" in question:
        print("Honestly, my favorite thing is how he supports me without even asking. \nHe's my biggest fan, even if he doesn't say it in many words!")

    elif "weekend" in question or "day off" in question:
        print("He loves the weekends! He almost always attends a 'dawwat' at one of my Chachu's homes. \nIt’s a family tradition—he really values that weekly time with his brothers.")

    elif "disagree" in question or "fight" in question:
        print("Sometimes! But we’re pretty good at talking it out. \nEven when we don't see eye-to-eye, he’s still the first person I go to for advice.")

    elif "laugh" in question:
        print("Small things! A good joke, or just us kids acting silly. \nHe has the kind of laugh that’s actually contagious.")

    elif "future" in question:
        print("He’s never been about money or fame. He just wants me to be a good person, \nstay honest, and find something I’m passionate about. That’s all he asks for.")

    elif "technology" in question or "screen" in question:
        print("He thinks it's funny how much time I spend in front of a screen! He's always telling me to take a break and breathe some fresh air.")

    elif "guest" in question or "host" in question:
        print("He loves when family visits! He’s at his best when he’s playing host and making sure everyone has enough tea and food.")

    elif question == "bye":
        print("Goodbye! Have a nice day.")
        break

    else:
        print("Sorry, I don't know that. Type 'help' to see what you can ask me.")