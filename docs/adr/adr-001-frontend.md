# 1. Frontend for application

Date: 2021-12-01

## Status

Accepted

## Context

We need in user interface for our web application.
There is some small requirements for frontend:

>Front-end (outputs data) must:
>
>1. Display any portion of the data stored in the DB
>
>2. Provide a method to trigger data update process 
## Decision

Page templates wrote on html with using bootstrap 5 framework template - "sb-admin 2". 

## Consequences

  * `+` Nice user interface out of the box;
  * `+` It's easy to add widgets, icons and other elements without having to write css rules or js-code;
  * `-` There are a lot of unnecessary css styles, js libraries whose functionality is not used. As a result, an increase in the size of the entire project;

## Links

* [SB-Admin2 Template](https://startbootstrap.com/theme/sb-admin-2)
