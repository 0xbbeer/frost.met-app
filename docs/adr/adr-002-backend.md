# 2. Backend for application

Date: 2021-12-01

## Status

Accepted

## Context

We need in backend for our web application.
Some requirements for backend:

>Back-end (collects data) must:
>
>1. Retrieve a portion of data from API (see in your >Variant) and store it in a database
>
>2. Update data on demand
>
>3. Update DB schema if needed on app’s update 
## Considered Options
* Django
* Flask
* PHP
## Decision

I decided to use django as a backend 

## Consequences

  * `+` A reliable framework that is being actively developed;
  * `+` Django ORM for easy database interaction;
  * `+` Authentication and admin panel out of the box;
  * `+` Well-secured;
  * `+` Nice the built in template engine;
  * `+` Fully loaded: no need to use third-party tool and libraryes;
  * `+` Convenience of operation, fast deployment and modification;
  * `-` Perhaps not suitable for small projects (but we will imply further development of the project :));
  * `-` Used more space than Flask or PHP;


