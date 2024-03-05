import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'Custom User Agent'}  # Set a custom user agent to avoid Too Many Requests error
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)

# Test the function
if __name__ == '__main__':
    top_ten('programming')
    top_ten('this_is_a_fake_subreddit')

