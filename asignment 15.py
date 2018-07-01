import re
#ques 1:

emils = "zuck26@facebook.com" \
        "page33@google.com" \
        "jeff42@amazon.com"

userid=re.findall(r'[a-z]{1,4}[\d]{1,2}' , emils)

dom=re.findall(r'[@]{1}[\w][a-z]{5,}',emils)

com=re.findall(r'com',emils)
usr1=[]
usr2=[]
usr3=[]
desired_output=[]
usr1.append(userid[0])
usr1.append(dom[0])
usr1.append(com[0])
uss=tuple(usr1)
usr2.append(userid[1])
usr2.append(dom[1])
usr2.append(com[1])
uss1=tuple(usr2)
usr3.append(userid[2])
usr3.append(dom[2])
usr3.append(com[2])
uss3=tuple(usr3)
desired_output.append(uss)
desired_output.append(uss1)
desired_output.append(uss3)

print(desired_output)
#ques2 :
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
ssss=re.findall(r'[Bb][\w]{1,20}',text)
print(ssss)

#ques3:
import re
sentence = "A, very very; irregular_sentence"
hhi=re.sub(r'[;_:,]',"",sentence)
print(hhi)

#ques4:
def show1(tweet):
    tweet=re.sub("http\S+\s"," ",tweet)
    tweet=re.sub("RT"," ",tweet)
    tweet=re.sub("cc"," ",tweet)
    tweet=re.sub("#\S+"," ",tweet)
    tweet = re.sub("@\S+", " ", tweet)
    tweet = re.sub("\!", " ", tweet)
    tweet = re.sub("\:", " ", tweet)
    tweet=re.sub("\s+"," ",tweet)
    return tweet

tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
print(show1(tweet))