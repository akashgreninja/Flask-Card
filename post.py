import re
import requests
class Post:
    def __init__(self):
        self.reg=1


    def get_json(self):
        request=requests.get("https://api.npoint.io/ed99320662742443cc5b")
        request.raise_for_status
        data_2=request.json() 
        return data_2


