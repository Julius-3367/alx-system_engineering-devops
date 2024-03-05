import requests

def recurse(subreddit, hot_list=[], after=None):
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
    
    headers = {'User-Agent': 'Custom User Agent'}  # Set a custom user agent to avoid Too Many Requests error
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        
        after = data['data']['after']
        if after is not None:
            recurse(subreddit, hot_list, after)
        
    else:
        return None
    
    return hot_list

# Test the function
if __name__ == '__main__':
    result = recurse('programming')
    if result is not None:
        print(len(result))
    else:
        print("None")
    
    result_fake = recurse('this_is_a_fake_subreddit')
    if result_fake is not None:
        print(len(result_fake))
    else:
        print("None")

