# url_shortener

### Summary
This is a simple service that can convert common url into shorter one. This service is using MongoDB as database for storing links. 
To run this application you need to clone the repository:
```
git clone https://github.com/mylyanykmarko/url_shortener.git
```
After cloning, open terminal and go into cloned folder. Run:
```
pip3 install -r requirments.txt
```
After sucessfull instalation of all python packages you can start the application:
```
python3 main.py
```
To create short url, open your browser and go to:
```
http://127.0.0.1:5000/get?url=<>&lifetime=<>
```
Instead of <> you should enter desired to be shortened url and lifetime. For expamle:
http://127.0.0.1:5000/get?url=https://ua.jooble.org/%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0-junior-python/%D0%9A%D0%B8%D0%B5%D0%B2&lifetime=3.
As a response you will see new shorter url, which will redirect you into website which you passed as <url> parameter.
