from instagrapi import Client
import csv
from datetime import datetime

insta_username="" #insert your insta username
insta_password=""   #insert your password of instagram and insta will send you a verificatio code on your email or mobile
my_user_id="" #leave this blank



def login_to_insta()->Client:
    cl=Client()
    print("Connecting to instagram and Logging in .... ")
    cl.login(username=insta_username,password=insta_password)
    global my_user_id
    my_user_id=cl.user_id_from_username(insta_username)
    print("Your User ID is : ", my_user_id)
    return cl

def collect_followers(client_obj:Client):
    fetched_followers=client_obj.user_followers(user_id=my_user_id,amount=1200)
    fetched_followings=client_obj.user_following(user_id=my_user_id,amount=1200)
    print("Your followers count is ", len(fetched_followers))
    print("Your following count is ", len(fetched_followings))
    print("Finding People Who don't Follow you back ")
    #get list of ids which dont follow me back but i follow them..these are the ones who stabbed
    nonfoll_ids=[i for i in fetched_followings.keys() if i not in fetched_followers.keys()]
    print("Non follower IDs are ",nonfoll_ids)
    #create a results csv and fetch the user names of the users from above and hunt them
    f=open('results.csv','w')
    writer=csv.writer(f)
    for i in nonfoll_ids:
        print("Non Followers username is ",fetched_followings.get(i).dict().get('username'))
        writer.writerow([fetched_followings.get(i).dict().get('username')])
    #close the file
    print("Results are ready ")
    f.close()
    #close or logout as well
    print("Logging out.")
    client_obj.logout()





if __name__ == '__main__':
    start=datetime.now()
    collect_followers(login_to_insta())
    end=datetime.now()
    print(end-start)