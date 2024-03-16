import requests, random, string

class Get_spotify():
    
    #uses the spotify api to retrieve the token to be able to call GET for albums
    def __init__(self):
        url = 'https://accounts.spotify.com/api/token'
        post_data = {'grant_type': 'client_credentials', 'client_id': '7bd8b394d2a348589032dfeaa5d40927', 'client_secret': '2212e204eca54677a110c79180854a38'}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        r = requests.post(url,  headers=headers, data=post_data)
        results = r.json()
        
        self.token = results['token_type'] + '  ' + results['access_token']
        

    def get_album(self, id, token):
        """uses the token to call and retrieve the album cover 
            api
        Args:
            id (string): the spotify id of the album
            token (string): the Authorization token to be able to retrieve the album cover

        Returns:
            list: returns a list containing 3 dictionaries containing height, url and width
        """
        url = "https://api.spotify.com/v1/albums/" + id
        r = requests.get(url, headers={'Authorization': token})  
        results = r.json()
        return results['images']  
    
    def get_random_album(self, token, limit, search_type):
        """gets random album cover with limit of 50 and search type (ex: album, artist...) look on Spotify api search
        on what is available

        Args:
            token (string): generated authorization token
            limit (int): integer from 1 to 50 of how many albums we want
            search_type (string): spotify api search type parameter

        Returns:
            list<dict>: returns a list of dictionaries that contains
            name: album name, image: cover url, link_to_album: spotify link
        """
        if limit > 50:
            limit = 50
        url = 'https://api.spotify.com/v1/search?'
        images = []
                
        #random letter generator
        letters = string.ascii_lowercase
        search = ''.join(random.choice(letters) for g in range(1))
        offset = random.randint(0, 1000)
        url += 'q=' + search + '&type=' + search_type + '&limit=' + str(limit) + '&offset=' + str(offset)
        r = requests.get(url, headers={'Authorization': token})  
        results = r.json()
        for album in results['albums']['items']:
            images.append({'name': album['name'], 'image': album['images'][2]['url'], 'link_to_album': album['external_urls']['spotify']})
            #in image: change the integer to 0 for a 640x640 image, 1 for 300x300 and 2 for 64x64
        return images
        