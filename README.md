# geolocation

this is a simple tool that gets geographical location information about an ip address.

Firstly create a .apikey file in the same directory as this readme. include the API key generated from ipstack.com
You can run this either by using docker:

docker run --rm -it $(docker build -q .) <IP_ADDRESS>

Or pip installing requirements.txt

pip install -r requirements.txt

Followed by running the script: ./iplookup.py 51.198.13.45

In addition to the error codes documented here https://ipstack.com/documentation#errors

Additional errors are:
Error 1: No API Key provided
Error 2: Invalid ip address
Error 3: Non Geographic ip address supplied

Musings and thoughts:
By storing the API Key credential in a file you can avoid the plain textr on the command line. AWS has some nifty secrets functionality to pass secrets or i could have used an environment variable. I dont like this uses HTTP. HTTPS would hide the key better but is a premium subscription product.

Further work is unittesting where we would mock requests.get.
