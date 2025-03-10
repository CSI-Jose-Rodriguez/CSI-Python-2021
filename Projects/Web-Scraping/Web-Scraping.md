
# Web-Scraping (15 points)
*Web scrapping* is the term for using a program to download and process content from the web. In this lesson you will learnn several modules that make it easy to scrape web pages in Python.  This modules are:
=======
# Web-Scraping
*Web scrapping* is the term for using a program to download and process content from the web. In this lesson you will learn several modules that make it easy to scrape web pages in Python.  This modules are:
- **webbrowser** - opens a browser to a specific page.
- **requests** - downloads files and web pages from the internet.
- **bs4** - parses HTML
- **selenium** - launces and controls a web browser. The selenium module is able to fill in forms and simulate mouse clicks in the browser. 

## Open a specific URL
The *webbrowser* module's open() function can launch a new browser to a specified URL. Open a terminal and enter the following:
```python
>>>import webbrowser
>>>webbrowser.open("https://...")
```
## Downloading files from the Web with the requests Module
The *requests* module lets you download files from the web without having to worry about network or connection errors. You will have to install this module.  Fro the command line, run **pip install --user requests**. If possible that you will have to restart your PC. 

Open a new terminal and enter the following into it:
```python
>>>import requests
```
If no error messages shows up, then the module has benn installed correctly. 

### References: 
Sweigart, A. (2020). *Automate the boring stuff with Python*. San Francisco. pages 268-300
=======
If no error messages shows up, then the module has been installed correctly. 

The request.get()function takes a string of a URL to download. By calling *type()* on *requests.get()*'s return value, you can see that it returns a *Response* object, which contains the response that the web server gave for your request. Enter the following into the interactive shell:

```python
>>>import requests
>>>res =requests.get("https://automatetheboringstuff.com/files/rj.txt")
>>>type(res)
<class 'requests.models.Response'>
>>>res.status_code == requests.codes.ok
True
>>>len(res.text)
178981
>>>print(res.text[:250])
```
Shell output:
```python
The Project Gutenberg Ebook of Romeo and Juliet...
```
## Classwork **(10 points)**

Instructions: 

1. Go to the website https://www.gutenberg.org/.
2. Select a book.
3. Click on Plain Text UTF-8.
4. Code directly on the interactive shell or create a script that allows you to download the first 300 characters of the book you selected.
5. Take a screenshot of your terminal's output showing the first 300 characters of the book.
6. Save it in Webscraping folder as Name-Lastname-WebScraping01.png
7. Push

## Saving Downloaded Files to the Hard Drive

You can download and save the webpage to a file on your hard drive with the standard *open()* function and *write()* method. To do that, you must open the file in *write binary* mode by passing the string *'wb'* as the second argument to *open()*. 
To write the web page to a file, you can use a *for* loop with the *Response* object's ***iter_content()*** method. 

Example:
```python
import requests
res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
res.raise_for_status()
playFile = open("Romeo And Juliet.text", "web")
for chunk in res.iter_content(100000):
    playFile.write(chunk)
plaFile.close
```

## Classwork **(15 points)**

Instructions: 

1. Go to the website https://www.gutenberg.org/.
2. Select a book.
3. Click on Plain Text UTF-8. Copy the URL
4. Create a new python script that allows you to download and save in your hard drive the first 100000 characters or bytes of the book. **Use the example script as reference.**
6. Save the script in the Webscraping folder as Name-Lastname-WebScraping02.py
7. The downloaded file should appears in your CSI-Python-2021 directory. Move it to the Webscraping directory or folder. 
8. Push

### References: 
Sweigart, A. (2020). *Automate the boring stuff with Python*. San Francisco. pages 268-300.

