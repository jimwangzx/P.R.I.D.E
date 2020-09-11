# Crack-D

<h2>Introduction</h2>
<p> Identicons are visual representation of hash values. Usually they look something like these :</p>
<p> <a href="https://github.com/donpark">Don Park</a> came up with the idea of using identicons to prevent phishing in 2007 in his blog <a href="https://web.archive.org/web/20080510221519/http://www.docuverse.com/blog/donpark/2007/01/22/identicon-based-anti-phishing-protection">post</a>.
  
<p> This project implementation is inspired from that idea. I would like to tout this as an alternate way to sign in to websites to safeguad against phishing attempts. Everyday, we log in to multiple websites, whether it is for e-mail, news feeds, games or social media sites. There is always a risk that the webpage that loads could have been compromised by an attacker as part of a MiTM attack or a general phishing scheme and hence the danger of your accounts being compromised without you even knowing it. </p>

<h2>Working</h2>
<p>A user loads up a website he/she wants to log into. The user then inputs his username/email first. This is sent to the server where it's validated for an existing record. If yes, then the server generates an identicon from the hashed password and sends it back to the users' browser. The user can see the identicon generated from the server. At the same time, the user's browser fetches the hashed password (read: password manager fetches the password it must have stored before) and generates the identicon. Both the identicons are placed side by side. If they are identical, then the opened site can be trusted. Now, the user can safely input his/her password.  
  
<h2>Comments</h2> 
<p> There are a lot of challenges in actually implementing it securely without any flaws. I have already come across some of them. Something is definitely wrong, but can't yet figure it out.</p>
<p>As of now, this is just a small hobby project.</p>




