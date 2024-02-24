# hy-cyber-mooc-project-1
Cyber Security Base 2024 Project 1 repo with 5 OWASP vulnerabilities with Django.

## Setup run environment
1. Install docker
2. ```docker-compose start```
4. ```docker-compose exec web ./migrate.sh```
5. Open [localhost:8001](localhost:8001)

## Example Vulnerabilities
### 1. Cross-site request forgery
Django supports nice out of the box middleware to include, validate and use CSRF-tokens to improve the security of the application. With the vulnerability [2. Injection] this is a proper and dangerous vulnerability.

See file: `polls/templates/createPoll.html` and line:5.
See file: `polls/templates/details.html` and line:17.
See file: `polls/templates/navBar.html` and line:5.
See file: `settings.py` and line:49.

Fix: uncomment the above mentioned lines.

### 2. Injection
Creating a new Poll allows user to add any kind of unsafe text into the description field. One user has used it to include images, but it also allows user to add JS-code which is ran on any users machine.
See file: `polls/templates/details.html` and line:5.
Line 6: has the fix commented out.


### 3. Security Misconfiguration
Django has Debug-mode on by default when creating new projects. With Debug=true Django shows a lot of information of the runtime backend for the user.

See file: `cyber_poll/settings.py` and line:28
Line 27: has the fix commented out
Same file has also the SECRET_KEY as some random-string. This value is now in git and as its public repo its completely unsafe.
New value needs to changed to something ELSE.

### 4. Identification and Authentication Failures
Django by default has quite long session TTL, two weeks. During this time in an office setting the user might have a valid session for over a week, if the computer is just staying on.

See file: `cyber_poll/settings.py` and line:31.
The commented out line adds session TTL of 5 min (its rather short, but works as an example).


### 5. Security Logging and Monitoring Failures
Monitoring and logging allows developers to find and address possible bugs or security threats. Having evidence of odd behaviour is often the first step to fix the issue and automated monitoring and logging have a important role here.

By default Django has no defined place for logs to be collected.
See file: `cyber_poll/settings.py` and line:110+.
The commented out part activates logging to a certain place allowing async investrgation of the issue. In production usage, make sure the logging does not overflood the server by creating _lots_ of logs.
