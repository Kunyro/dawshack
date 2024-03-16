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
    
# EXAMPLE of how to use the object to get the album cover of given spotify album id
# gs = Get_spotify()
# result = gs.get_album('3Gt7rOjcZQoHCfnKl5AkK7', gs.token)
# print(result[1]['url'])
    
    def get_random_album(self, token, limit, search_type):
        
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
            images.append(album['images'][1]['url'])
        
        return images
    
gs = Get_spotify()
print(gs.get_random_album(gs.token, 5, 'album'))
        