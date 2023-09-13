import random
import json
import datetime

USERS_NUMBER = 100
MAX_POSTS_NUMBER = USERS_NUMBER
MAX_STORIES_NUMBER = USERS_NUMBER
MAX_COMMENT_NUMBER = USERS_NUMBER
HASHTAG_NUMBER = 100
THREAD_NUMBER = int(USERS_NUMBER/5)

POST_PARTITIONING = 5
STORY_PARTITIONING = 50
COMMENT_PARTITIONING = 15
DIRECT_PARTITIONING = 40
THREAD_PARTITIONING = 15

names = open('names.txt').read().splitlines()
words = open('words.txt').read().splitlines()

def generate_users():
    users_array = []
    for i in range(USERS_NUMBER):
        name = random.choice(names)
        users_array.append({
            "username": f"U{i}",
            "detailsU": {
                "name": name, 
                "biography": "", 
                "birthday": "", 
                "email": f"{name}.{i}@email.com", 
                "phoneNumber": "", 
                "password": f"password_{name}", 
                "profileImage": "", 
                "verified": random.choice([True, False]), 
                "genre": random.choice(["male", "female", "other"]), 
                "link": ""
            },
            "postsCount": random.randint(0, MAX_POSTS_NUMBER),
            "followerCount": 0,
            "followingCount": random.randint(0, USERS_NUMBER-1),
            "latestOwnUS": [],
            "ownUS": [],
            "ownUT": [],
            "latestOwnUP": [],
            "ownUP": [],
            "notify": [],
            "blocked": [],
            "follow": [],
            "closeFriend": []
        })

    with open('output/user.json', 'w') as outfile:
        json.dump(users_array, outfile, indent=4)

def generate_posts():
    user_file = open('output/user.json')
    users_array = json.load(user_file)

    posts_array = []
    for user in users_array:
        for i in range(user["postsCount"]):
            posts_array.append({
                "idPost": f'{user["username"]}P{i}',
                "detailsP": {
                    "media": "", 
                    "isReel": random.choice([True, False]), 
                    "timestamp": datetime.datetime.now().timestamp(), 
                    "description": "", 
                    "place": "", 
                    "music": ""
                    },
                "ownUP": user["username"],
                "likesCountP": random.randint(0,USERS_NUMBER),
                "includePH": [],
                "likeUP": [],
                "tagUP": [],
                "mostLiked": []
            })
    
    with open('output/post.json', 'w') as outfile:
        json.dump(posts_array, outfile, indent=4)

def generate_stories():
    user_file = open('output/user.json')
    users_array = json.load(user_file)

    stories_array = []
    for user in users_array:
        for i in range(random.randint(0,MAX_STORIES_NUMBER)):
            stories_array.append({
                "idStory": f'{user["username"]}S{i}',
                "detailsS": {
                    "media": "",
                    "restricted": False,
                    "timestamp": datetime.datetime.now().timestamp(),
                    "place": "",
                    "music": "",
                    "evidence": random.choice([True, False])
                },
                "ownUS": user["username"],
                "likesCount": random.randint(0,USERS_NUMBER),
                "likeUS": [],
                "tagUS": [],
                "reactionUS": [],
                "includeSH": []
            })
    
    with open('output/story.json', 'w') as outfile:
        json.dump(stories_array, outfile, indent=4)

def generate_comments():
    user_file = open('output/user.json')
    users_array = json.load(user_file)
    post_file = open('output/post.json')
    posts_array = json.load(post_file)
    posts_id = list(map(lambda x: x["idPost"], posts_array))

    comments_array = []
    for user in users_array:
        for i in range(random.randint(0,MAX_COMMENT_NUMBER)):
            comments_array.append({
                "idComment": f'{user["username"]}C{i}',
                "detailsC": {
                    "content": "", 
                    "timestamp": datetime.datetime.now().timestamp(),
                    },
                "ownUC": user["username"],
                "tagUC": [],
                "likeUC": [],
                "includePC": random.choice(posts_id),
                "likesCountC": random.randint(0,USERS_NUMBER),
                "includeCH": [],
                "reply": []
        })
    
    with open('output/comment.json', 'w') as outfile:
        json.dump(comments_array, outfile, indent=4)

def generate_hashtags():
    hashtags_array = []
    for i in range(HASHTAG_NUMBER):
        hashtags_array.append({
            "idHashtag": f'H{i}',
            "text": random.choice(words),
            "postsCountH":	random.randint(0,USERS_NUMBER*2),
            "commentsCountH": random.randint(0,USERS_NUMBER*2),
            "storiesCountH": random.randint(0,USERS_NUMBER*2)
        })

    with open('output/hashtag.json', 'w') as outfile:
        json.dump(hashtags_array, outfile, indent=4)

def generate_chats():
    chats_array = []
    for i in range(random.randint(0,USERS_NUMBER*5)):
        chats_array.append({
            "idChat": f"C{i}",
            "detailsC": {
                "isGroup": random.choice([True, False]), 
                "name": "", 
                "timestamp": datetime.datetime.now().timestamp()
            },
	        "join": [],
	        "latestInDC": []
        })

    with open('output/chat.json', 'w') as outfile:
        json.dump(chats_array, outfile, indent=4)

def generate_directs():

    chat_file = open('output/chat.json')
    chats_array = json.load(chat_file)

    idChat_list = list(map(lambda x: x["idChat"], chats_array))

    directs_array = []
    for i in range(random.randint(0,USERS_NUMBER*50)):
        directs_array.append({
            "idDirect": f"D{i}",
            "detailsD": {
                "content": "", 
                "timestamp": datetime.datetime.now().timestamp()
            },
	        "inDC":	random.choice(idChat_list)
        })

    with open('output/direct.json', 'w') as outfile:
        json.dump(directs_array, outfile, indent=4)


def generate_threads():

    threads_array = []
    user_file = open('output/user.json')
    users_array = json.load(user_file)
    post_file = open('output/post.json')
    posts_array = json.load(post_file)

    for i in range(random.randint(0,THREAD_NUMBER)):
        threads_array.append({
            "idThread": f"T{i}",
            "detailsT": {
                "title": "", 
                "category": "", 
                "description": "", 
                "timestamp": datetime.datetime.now().timestamp()
            },
            "ownUT": random.choice(users_array)["username"],
            "postscountT": random.randint(0,len(posts_array)),
            "usersCountT":	random.randint(0,USERS_NUMBER),
            "partecipation": [],
            "includePT": [],
            "latestIncludePT": []
        })

    with open('output/thread.json', 'w') as outfile:
        json.dump(threads_array, outfile, indent=4)

def update_users():
    user_file = open('output/user.json')
    users_array = json.load(user_file)
    
    # FILL FOLLOW ARRAY & CLOSE FRIEND
    for user in users_array:
        for i in range(user["followingCount"]):
            username_list = (list(map(lambda x: x["username"], users_array)))
            sub_list = user["follow"] + [user["username"]]
            username_list = list(set(username_list) - set(sub_list))
            rand_user = random.choice(username_list)
            user["follow"].append(rand_user)
            if (random.choice([True,False])): user["closeFriend"].append(rand_user)
    
    # UPDATE FOLLOWER COUNT
    follow_list = list(map(lambda x: x["follow"], users_array))
    follow_list = [item for sublist in follow_list for item in sublist]
    for user in users_array:
        user["followerCount"] = follow_list.count(user["username"])

    # UPDATE POST/STORY/THREAD LISTS & LATEST
    post_file = open('output/post.json')
    posts_array = json.load(post_file)
    story_file = open('output/story.json')
    stories_array = json.load(story_file)
    for user in users_array:

        filtered_posts = list(filter(lambda x: x["ownUP"] == user["username"], posts_array))
        filtered_posts.sort(key = lambda x: x["detailsP"]["timestamp"], reverse=False)
        filtered_posts = list(map(lambda x: x["idPost"], filtered_posts))
        user["latestOwnUP"] = filtered_posts[:POST_PARTITIONING-1]
        filtered_stories = list(filter(lambda x: x["ownUS"] == user["username"], stories_array))
        filtered_stories.sort(key = lambda x: x["detailsS"]["timestamp"], reverse=False)
        filtered_stories = list(map(lambda x: x["idStory"], filtered_stories))
        user["latestOwnUS"] = filtered_stories[:STORY_PARTITIONING-1]

        for post in posts_array:
            if post["ownUP"] == user["username"] and post["idPost"] not in user["latestOwnUP"] :
                user["ownUP"].append(post["idPost"])
        for story in stories_array:
            if story["ownUS"] == user["username"] and story["idStory"] not in user["latestOwnUS"] :
                user["ownUS"].append(story["idStory"])

    # UPDATE THREAD OWN
    thread_file = open('output/thread.json')
    threads_array = json.load(thread_file)

    for user in users_array:
        own = list(filter(lambda x: x["ownUT"] ==  user["username"], threads_array))
        own = list(map(lambda x: x["idThread"], own))
        user["ownUT"] = own

    with open('output/user.json', 'w') as outfile:
        json.dump(users_array, outfile, indent=4)

def update_posts():
    user_file = open('output/user.json')
    users_array = json.load(user_file)
    post_file = open('output/post.json')
    posts_array = json.load(post_file)
    comment_file = open('output/comment.json')
    comments_array = json.load(comment_file)

    # UPDATE LIKE/TAG LIST & MOST LIKED COMMENTS
    username_list = (list(map(lambda x: x["username"], users_array)))
    for post in posts_array:
        for i in range(post["likesCountP"]):
            post["likeUP"].append(random.choice(list(set(username_list)-set(post["likeUP"]))))
        for i in range(random.randint(0,3)):
            post["tagUP"].append(random.choice(list(set(username_list)-set(post["tagUP"]))))
        
        
        filtered_comments = list(filter(lambda x: x["includePC"] == post["idPost"], comments_array))
        filtered_comments.sort(key = lambda x: x["likesCountC"], reverse=True)
        post["mostLiked"] = filtered_comments[:COMMENT_PARTITIONING-1]
        
        # REMOVE AGGREGATED
        comments_array = list(filter(lambda x: x not in post["mostLiked"], comments_array)) 
    
    with open('output/post.json', 'w') as outfile:
        json.dump(posts_array, outfile, indent=4)
    
    with open('output/comment.json', 'w') as outfile:
        json.dump(comments_array, outfile, indent=4)

def update_stories():
    user_file = open('output/user.json')
    users_array = json.load(user_file)

    story_file = open('output/story.json')
    stories_array = json.load(story_file)

    # UPDATE LIKE/TAG/REACTION
    username_list = (list(map(lambda x: x["username"], users_array)))
    for story in stories_array:
        for i in range(story["likesCount"]):
            story["likeUS"].append(random.choice(list(set(username_list)-set(story["likeUS"]))))
        for i in range(random.randint(0,3)):
            story["tagUS"].append(random.choice(list(set(username_list)-set(story["tagUS"]))))
        for i in range(random.randint(0,3)):
            story["reactionUS"].append(random.choice(list(set(username_list)-set(story["reactionUS"]))))
    
    with open('output/story.json', 'w') as outfile:
        json.dump(stories_array, outfile, indent=4)


def update_comments():
    user_file = open('output/user.json')
    users_array = json.load(user_file)
    comment_file = open('output/comment.json')
    comments_array = json.load(comment_file)

    # UPDATE LIKE/TAG
    username_list = (list(map(lambda x: x["username"], users_array)))
    for comment in comments_array:
        for i in range(comment["likesCountC"]):
            comment["likeUC"].append(random.choice(list(set(username_list)-set(comment["likeUC"]))))
        for i in range(random.randint(0,3)):
            comment["tagUC"].append(random.choice(list(set(username_list)-set(comment["tagUC"]))))
    
    with open('output/comment.json', 'w') as outfile:
        json.dump(comments_array, outfile, indent=4)

def update_hashtags():
    post_file = open('output/post.json')
    posts_array = json.load(post_file)
    story_file = open('output/story.json')
    stories_array = json.load(story_file)
    comment_file = open('output/comment.json')
    comments_array = json.load(comment_file)

    # NOT ENOUGH COMMENTS PROBLEM
    other_comments = list(map(lambda x: x["mostLiked"], posts_array))
    other_comments = [item for sublist in other_comments for item in sublist]

    new_comments_array = comments_array + other_comments

    hashtag_file = open('output/hashtag.json')
    hashtags_array = json.load(hashtag_file)

    for hashtag in hashtags_array:
        chosen_posts = []
        for i in range(hashtag["postsCountH"]):
            random_post = random.choice(list(posts_array))
            if random_post in chosen_posts:
                i -= 1
                continue   
            random_post["includePH"].append(hashtag["idHashtag"])
            chosen_posts.append(random_post)
        chosen_stories = []
        for i in range(hashtag["storiesCountH"]):
            random_story = random.choice(list(stories_array))
            if random_story in chosen_stories:
                i -= 1
                continue  
            random_story["includeSH"].append(hashtag["idHashtag"])
            chosen_stories.append(random_story)
        chosen_comments = []
        for i in range(hashtag["commentsCountH"]):
            random_comment = random.choice(list(new_comments_array))
            if random_comment in chosen_comments:
                i -= 1
                break    
            random_comment["includeCH"].append(hashtag)
            chosen_comments.append(random_comment)

    with open('output/post.json', 'w') as outfile:
        json.dump(posts_array, outfile, indent=4)
    with open('output/story.json', 'w') as outfile:
        json.dump(stories_array, outfile, indent=4)
    with open('output/comment.json', 'w') as outfile:
        json.dump(comments_array, outfile, indent=4)

def update_chats():
    chat_file = open('output/chat.json')
    chats_array = json.load(chat_file)
    user_file = open('output/user.json')
    users_array = json.load(user_file)

    direct_file = open('output/direct.json')
    directs_array = json.load(direct_file)

    # UPDATE JOIN & LATEST
    username_list = (list(map(lambda x: x["username"], users_array)))

    for chat in chats_array:
        if chat["detailsC"]["isGroup"]:
            for i in range(3,10):
                chat["join"].append(random.choice(list(set(username_list)-set(chat["join"]))))
        else:
            for i in range(2):
                chat["join"].append(random.choice(list(set(username_list)-set(chat["join"]))))
        
        filtered_directs = list(filter(lambda x: x["inDC"] == chat["idChat"], directs_array))
        filtered_directs.sort(key = lambda x: x["detailsD"]["timestamp"], reverse=False)
        chat["latestInDC"] = filtered_directs[:DIRECT_PARTITIONING-1]

        # REMOVE AGGREGATED
        directs_array = list(filter(lambda x: x not in chat["latestInDC"], directs_array))

    with open('output/chat.json', 'w') as outfile:
        json.dump(chats_array, outfile, indent=4)

    with open('output/direct.json', 'w') as outfile:
        json.dump(directs_array, outfile, indent=4)


def update_threads():
    thread_file = open('output/thread.json')
    threads_array = json.load(thread_file)

    user_file = open('output/user.json')
    users_array = json.load(user_file)
    post_file = open('output/post.json')
    posts_array = json.load(post_file)

    username_list = (list(map(lambda x: x["username"], users_array)))
    idPost_list = (list(map(lambda x: x["idPost"], posts_array)))

    for thread in threads_array:
        for i in range(thread["usersCountT"]):
            thread["partecipation"].append(random.choice(list(set(username_list)-set(thread["partecipation"]))))
        for i in range(thread["postscountT"]):
            thread["includePT"].append(random.choice(list(set(idPost_list)-set(thread["includePT"]))))

        filtered_posts = list(filter(lambda x: x["idPost"] in thread["includePT"], posts_array))
        filtered_posts.sort(key = lambda x: x["detailsP"]["timestamp"], reverse=False)
        thread["latestIncludePT"] = filtered_posts[:THREAD_PARTITIONING-1]

        # REMOVE AGGREGATED
        posts_array = list(filter(lambda x: x not in thread["latestIncludePT"], posts_array))

    with open('output/thread.json', 'w') as outfile:
        json.dump(threads_array, outfile, indent=4)

    with open('output/post.json', 'w') as outfile:
        json.dump(posts_array, outfile, indent=4)

if __name__ == '__main__':
    generate_users()
    generate_posts()
    generate_stories()
    generate_comments()
    generate_hashtags()
    generate_chats()
    generate_directs()
    generate_threads()
    update_users()
    update_posts()
    update_stories()
    update_comments()
    update_hashtags()
    update_chats()
    update_threads()
