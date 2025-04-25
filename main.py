from atproto import Client

USERNAME = 'your-handle.bsky.social'
PASSWORD = 'your-password'  

POST_TEXT = "Hello from SkyPoster! 🚀"

def post_to_bluesky(username, password, text):
    client = Client()
    client.login(username, password)
    client.send_post(text)
    print("✅ โพสต์เรียบร้อยแล้ว!")

post_to_bluesky(USERNAME, PASSWORD, POST_TEXT)
