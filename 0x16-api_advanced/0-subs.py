import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}  # Set a custom user agent to avoid Too Many Requests error
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0

# Test the function
if __name__ == '__main__':
    print(number_of_subscribers('programming'))
    print(number_of_subscribers('this_is_a_fake_subreddit'))

