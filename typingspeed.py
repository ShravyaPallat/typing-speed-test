from time import time

def tperror(prompt, inwords):
    words = prompt.split()
    errors = 0
    for i in range(len(inwords)):
        if i < len(words):
            if inwords[i] != words[i]:
                errors += 1
        else:
            errors += 1
    return errors

# Function to calculate speed of typing words per minute
def speed(inwords, elapsed_time):
    twords = len(inwords)
    speed_wpm = (twords / elapsed_time) * 60  # Words per minute
    return speed_wpm

# Function to calculate the total elapsed time
def elapsedtime(starttime, endtime):
    return endtime - starttime

if __name__ == '__main__':
    prompt = ("The most difficult thing is the decision to act. "
              "The rest is merely tenacity. The fears are paper tigers. "
              "You can do anything you decide to do. You can act to change "
              "and control your life; and the procedure, the process, is its own reward.")
    print("Type this: '", prompt, "'")
    input("Press enter when you are ready to check your speed: ")
    starttime = time()
    inprompt = input()
    endtime = time()
    
    elapsed_time = round(elapsedtime(starttime, endtime), 2)
    inwords = inprompt.split()
    typing_speed = round(speed(inwords, elapsed_time), 2)
    errors = tperror(prompt, inwords)
    
    print("Total time elapsed:", elapsed_time, "seconds")
    print("Your average typing speed was", typing_speed, "words per minute (wpm)")
    print("with a total of", errors, "errors")
