# Crack-D

<h2>Introduction</h2>
<p> Identicons are visual representation of hash values. Usually they look something like these :</p><br>

<p align="center">
  <img src="/Assets/sample_identicon_2.png">&emsp; &emsp; &emsp;
  <img src="/Assets/sample_identicon_1.png">
  </p>

<br>
<p> As a matter of fact, GitHub uses identicons as profile pictures by default based on the username of users. Since no two users have the same username, every user has a unique identicon. It is also used in many blog sites to uniquely identify each user even if the names are same.</p>
<p> <a href="https://github.com/donpark">Don Park</a> came up with the idea of using identicons to prevent phishing in 2007 in this blog <a href="https://web.archive.org/web/20080510221519/http://www.docuverse.com/blog/donpark/2007/01/22/identicon-based-anti-phishing-protection">post</a>.
  
<p> This project implementation is inspired from that idea. I would like to tout this as an alternate way to sign in to websites to safeguard against phishing attempts. Everyday, we log in to multiple websites, whether it is for e-mail, news feeds, games or social media. There is always a risk that the webpage that loads could have been compromised by an attacker as part of a MiTM attack or a general phishing scheme and hence the danger of your accounts being compromised without you even knowing it. </p>

<h2>Working</h2>
<p>A user loads up a website he/she wants to log into. The user then inputs his username/email first. This is sent to the server where it's validated for an existing record. If yes, then the server generates an identicon from the hashed password and sends it back to the users' browser. The user can see the identicon generated from the server. At the same time, the user's browser fetches the hashed password (read: password manager fetches the password it must have stored before) and generates the identicon. Both the identicons are placed side by side. If they are identical, then the opened site can be trusted. Now, the user can safely input his/her password.  
  
<h2>Pre-requisites</h2>
 <p>The major dependencies used are :
<ul type="disc">
  <li>Flask - 1.1.2</li>
  <li>Flask-SQLAlchemy - 2.4.4</li>
  <li>passlib - 1.7.2</li>
  <li>pydenticon - 0.3.1</li>
  <li>sockets - 1.0.0</li>
  <li>SQLAlchemy - 1.3.19</li>
  </ul>
  
  For the completel list check <a href="requirements.txt">this</a>.</p>





 
  
<h2>Comments</h2> 
<p> There are a lot of challenges in actually implementing it securely without any flaws. I have already come across some of them. Something is definitely wrong, but can't yet figure it out.</p>
<p>As of now, this is just a small hobby project.</p>




