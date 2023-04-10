# Telegraph API Wrapper

This Python module is a wrapper for the Telegra.ph API which allows users to interact with the Telegra.ph platform. The class provides functionality for creating and managing Telegra.ph accounts, pages, and uploading files, as well as downloading images from the internet and uploading them to Telegra.ph.

## Dependencies
- requests
- logging
- json
- os

## Installation
You can install the required libraries using pip:

    pip install requests

## Usage

First, you need to create an instance of the Telegraph class:

    from telegraph import Telegraph

    telegraph = Telegraph()

### Creating an account
To create a new account, call the create_account method:

    response = telegraph.create_account("ShortName", "AuthorName", "AuthorURL")

### Getting a page
To get the content of a Telegra.ph page, call the get_page method:

    response = telegraph.get_page("PagePath")

### Getting a list of your pages
To get a list of pages created by your account, call the get_my_page_list method:

    response = telegraph.get_my_page_list()

### Creating a page
To create a new page, call the create_page method:

    response = telegraph.create_page("Content", "Title")

### Uploading a file
To upload a file to Telegra.ph, call the upload_file method:

    response = telegraph.upload_file(file_content, file_type)

### Downloading an image from the internet and uploading it to Telegra.ph
To download an image from the internet and upload it to Telegra.ph, call the download_image_from_internet_and_upload method:

    response = telegraph.download_image_from_internet_and_upload("ImageURL")

## Methods
The available methods in the Telegraph class are:

- __init__(self, logging_level=logging.DEBUG)
- get_page(self, path)
- create_account(self, short_name, author_name='Anonymous', author_url='')
- get_my_page_list(self, offset=0)
- create_page(self, content, title)
- upload_file(self, file, file_type)
- download_image_from_internet_and_upload(self, image_url)

## Examples
Here are some examples of how to use the Telegraph API wrapper:

### 1. Create an account
    from telegraph import Telegraph

    telegraph = Telegraph()
    response = telegraph.create_account("MyShortName", "MyAuthorName", "https://myauthorurl.com")

    print(response)

### 2. Get a page
    from telegraph import Telegraph

    telegraph = Telegraph()
    response = telegraph.get_page("Sample-Page-Path")

    print(response)

### 3. Get a list of your pages
    from telegraph import Telegraph

    telegraph = Telegraph()
    response = telegraph.get_my_page_list()

    print(response)

### 4. Create a page
    from telegraph import Telegraph

    telegraph = Telegraph()
    content = "[{'tag':'p', 'children':['Hello, world!']}]"
    title = "Hello World"
    response = telegraph.create_page(content, title)

    print(response)

### 5. Upload a file
    from telegraph import Telegraph

    telegraph = Telegraph()

    with open("example_image.jpg", "rb") as file:
        file_content = file.read()

    response = telegraph.upload_file(file_content, "image/jpeg")

    print(response)

### 6. Download an image from the internet and upload it to Telegra.ph
    from telegraph import Telegraph

    telegraph = Telegraph()
    image_url = "https://example.com/image.jpg"
    response = telegraph.download_image_from_internet_and_upload(image_url)

    print(response)

## Contributions
Contributions to this project are welcome. If you find any bugs, have feature requests, or would like to help improve the code, please feel free to open an issue or create a pull request on the project's GitHub repository.
