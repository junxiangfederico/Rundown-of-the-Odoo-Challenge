# Odoo-Challenge solution for the challenge number 7

<img src="/assets/challenge7.png" width=80% height=80%> 

Once again we access the network tab using the inspect tools. By analyzing the "next" entry we find out that the url to retrieve the key is not directly accessible, and we need to retrieve it by ourselves.

<img src="/assets/challenge7_0.png" width=80% height=80%> 

<img src="/assets/challenge7_1.png" width=80% height=80%> 

By combining the two parts we obtain: 
"/jobs/challenge/fc3/b01/prime.json" -> "https://www.odoo.com/jobs/challenge/fc3/b01/prime.json"

# prime.json
Once again the key is not directly displayed, we need to retrieve it by resolving the task given:

<img src="/assets/challenge7_2.png" width=80% height=80%> 

Fortunately you don't need to do all that, you cantailor to your needs the script that you can find in "/challenge7/script.py"

<img src="/assets/challenge7_3.png" width=80% height=80%> 

