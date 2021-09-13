# BruteGmail
A script to Brute force gmail accounts using a mail server as a verfication method 



Thanks to https://github.com/H3LL0WORLD/Gmail-Enum for providing this useful information 


Setup :
```
pip3 install -r req.txt
```

Usage:
```
python3  master_.py [-h] [-s S] [-m M] [-g G] [-g2 G2] [-t T]

optional arguments:
  -h, --help  show this help message and exit
  -s S        single email check
  -m M        multiple email check
  -g G        generate and check without user interference
  -g2 G2      generate and check without user interference
  -t T        threaded
     
```

PS : g uses names module to generate first name only 
     g2 uses random-username module to generate custom username
     
     
