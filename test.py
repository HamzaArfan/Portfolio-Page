from instabot import Bot
import time

# Replace with your Instagram username and password
username = 'oneplus9protest1'
password = '235056090'

# Initialize the bot
bot = Bot()

# Login to your Instagram account
bot.login(username=username, password=password)

# Get the list of users you follow
following = bot.get_user_following(username)

# Iterate through the list of users and like their recent posts
for user_id in following:
    user_info = bot.get_user_info(user_id)
    username = user_info['username']
    recent_posts = bot.get_user_medias(username, filtration=False)
    
    for post in recent_posts:
        post_id = post['pk']
        bot.like(post_id)
        print(f"Liked post {post_id} by @{username}")
        time.sleep(10)  # Add a delay to avoid excessive actions

# Logout from the Instagram account
bot.logout()
