import requests
import logging
import json
import os

"""
    {'access_token': '17fc91354dfe45c52981e30bffdda72eea29a4f19b5c432fb0b6b04cfa5d',
            'auth_url': 'https://edit.telegra.ph/auth/pO6TWKUc0bQ95ijjFI27DJO8rpiPsGZPu5IoQBAQMq',
            'author_name': 'Anonymous',
            'author_url': '',
            'short_name': 'anonym'}}
"""

class Telegraph:
    """
        This Python class, Telegraph, is a wrapper for the Telegra.ph API which allows users to interact with the
        Telegra.ph platform. The class provides functionality for creating and managing Telegra.ph accounts, pages,
        and uploading files, as well as downloading images from the internet and uploading them to Telegra.ph.

        The class makes use of the requests library for making HTTP requests, and the logging library for
        logging events and error messages.

        Attributes:
            access_token (str): A string representing the access token required for making API calls.

        Methods:
            init(self, logging_level=logging.DEBUG): Initializes a new instance of the Telegraph class
                and sets up logging with the specified logging level.
            get_page(self, path): Retrieves the content of a Telegra.ph page identified by the given path.
            create_account(self, short_name, author_name='Anonymous', author_url=''): Creates a new Telegra.ph
                account with the given short name, author name, and author URL.
            get_my_page_list(self, offset=0): Retrieves the list of pages created by the user's account, starting
                from the specified offset.
            create_page(self, content, title): Creates a new Telegra.ph page with the given content and title.
            upload_file(self, file, file_type): Uploads a file to Telegra.ph and returns its URL.
            download_image_from_internet_and_upload(self, image_url): Downloads an image from the internet using
                the given URL and uploads it to Telegra.ph.
    """

    access_token = os.environ.get('TELEGRAPH_TOCKEN')

    def __init__(self, logging_level=logging.DEBUG):
        #Set logging
        self.logger = logging.getLogger('Telegraph')
        self.logger.setLevel(logging_level)
        if (self.logger.hasHandlers()):
            self.logger.handlers.clear()
        ch = logging.StreamHandler()
        ch.setLevel(logging_level)
        self.logger.addHandler(ch)

    def get_page(self, path):
        """
            Retrieves the content of a Telegra.ph page identified by the given path.

            Args:
                path (str): The path to the Telegraph page (in the format Title-12-31),
                    i.e., everything that comes after http://telegra.ph/.

            Returns:
                dict: A dictionary containing the JSON response from the Telegra.ph API.
                    If the request is successful, the dictionary includes the page data.
                    If the request fails, the dictionary contains the 'ok' key set to False.
            """
        response = requests.get(f"https://api.telegra.ph/getPage/{path}?return_content=true")
        if response.status_code == 200:
            response_json = response.json()
        else:
            self.logger.error(f"Request to API failed with status code {response.status_code}, reason: {response.reason}, error message: {response.text}")
            response_json = {'ok': False}
        
        return response_json
    
    def create_account(self, short_name, author_name='Anonymous', author_url=''):
        """
            Creates a new Telegra.ph account with the given short name, author name, and author URL.

            Args:
                short_name (str): Account name (1-32 characters) used to help users with multiple
                    accounts remember which they are currently using. Displayed to the user above
                    the "Edit/Publish" button on Telegra.ph. Other users do not see this name.
                author_name (str, optional): Default author name (0-128 characters) used when
                    creating new articles. Defaults to 'Anonymous'.
                author_url (str, optional): Default profile link (0-512 characters) that is opened
                    when users click on the author's name below the title. Can be any link, not
                    necessarily to a Telegram profile or channel. Defaults to an empty string.

            Returns:
                dict: A dictionary containing the JSON response from the Telegra.ph API.
                    If the request is successful, the dictionary includes the account data.
                    If the request fails, the dictionary contains the 'ok' key set to False.
            """
        response = requests.get(f"https://api.telegra.ph/createAccount/?short_name={short_name}&author_name={author_name}&author_url={author_url}")
        if response.status_code == 200:
            response_json = response.json()
        else:
            self.logger.error(f"Request to API failed with status code {response.status_code}, reason: {response.reason}, error message: {response.text}")
            response_json = {'ok': False}
        
        return response_json
    
    def get_my_page_list(self, offset=0):
        """
            Retrieves the list of pages created by the user's account, starting from the specified offset.

            Args:
                offset (int, optional): The starting point for retrieving the list of pages.
                    Defaults to 0.

            Returns:
                dict: A dictionary containing the JSON response from the Telegra.ph API.
                    If the request is successful, the dictionary includes the list of pages and
                    related data.
                    If the request fails, the dictionary contains the 'ok' key set to False.
            """
        response = requests.get(f"https://api.telegra.ph/getPageList?access_token={self.access_token}&offset={offset}&limit=200")
        if response.status_code == 200:
            response_json = response.json()
        else:
            self.logger.error(f"Request to API failed with status code {response.status_code}, reason: {response.reason}, error message: {response.text}")
            response_json = {'ok': False}
        
        return response_json
    
    def create_page(self, content, title):
        """
            Creates a new Telegra.ph page with the given content and title.

            Args:
                content (str): The content of the page in the form of an array of Node objects
                    (see Telegra.ph API documentation for more details on Node objects).
                title (str): The title of the page.

            Returns:
                dict: A dictionary containing the JSON response from the Telegra.ph API.
                    If the request is successful, the dictionary includes the created page data.
                    If the request fails, the dictionary contains the 'ok' key set to False.
            """
        params = {'access_token': self.access_token,
                  'title': title,
                  'content': content,
                   'return_content': True}
        response = requests.post(f"https://api.telegra.ph/createPage", json=params)
        if response.status_code == 200:
            response_json = response.json()
        else:
            self.logger.error(f"Request to API failed with status code {response.status_code}, reason: {response.reason}, error message: {response.text}")
            response_json = {'ok': False}
        
        return response_json
    
    def upload_file(self, file, file_type):
        """
            Uploads a file to Telegra.ph and returns its URL.

            Args:
                file (bytes): The file content in bytes format to be uploaded.
                file_type (str): The MIME type of the file (e.g., 'image/jpeg', 'image/png').

            Returns:
                dict: A dictionary containing the JSON response from the Telegra.ph API.
                    If the request is successful, the dictionary includes the uploaded file's URL.
                    If the request fails, the dictionary contains the 'ok' key set to False.
            """
        response = requests.post(f"https://telegra.ph/upload", files={'file': ('file', file, file_type)})
        if response.status_code == 200:
            response_json = response.json()
        else:
            self.logger.error(f"Request to API failed with status code {response.status_code}, reason: {response.reason}, error message: {response.text}")
            response_json = {'ok': False}
        
        return response_json
    
    def download_image_from_internet_and_upload(self, image_url):
        response = requests.get(image_url)
        response_json = self.upload_file(response.content, response.headers['Content-Type'])
        return response_json