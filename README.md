# hy-cyber-mooc-project-1
Cyber Security Base 2024 Project 1 repo with 5 OWASP vulnerabilities with Django.

## Setup run environment
1. Install docker
2. ```docker-compose start```
4. ```docker-compose exec web ./migrate.sh```
5. Open [localhost:8001](localhost:8001)

## Example Vulnerabilities
### 1. Broken access-control

### 2. Injection
Creating a new Poll allows user to add any kind of unsafe text into the description field. One user has used it to include images, but it also allows user to add JS-code which is ran on any users machine.
See file: `polls/templates/details.html` and line:5.
Line 6: has the fix commented out.


### 3. Insecure Design - Sniff which users are using the service

### 4. Identification and Authentication Failures - allows _very_ weak passwords

### 5. Server-Side Request Forgery (SSRF) - Avatar image from url