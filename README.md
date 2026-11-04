# Route Planner For CH Robinson interview

Uses undirected graph to find a path to a country (starting from the USA)

## Description

Since there were only 10 countries within the scope of the problem I decided to have the graph be a constant, but in a situation where more countries would be added having a sql database with 2 tables for countries and borders would scale nicely for a larger system.
I Used Breadth-first search, since we want the shortest path to a country.
The input is also case-insetive, and will return a 404 if it's not a valid country code

## Getting Started

### Dependencies

Python 3.13
uv
Docker

### Installing

* git clone git@github.com:omegareeeee/RoutePlaner.git
* cd RoutePlaner
* uv sync

### Executing program

* How to run the program
* Step-by-step bullets
```
Run (locally): your uvicorn app.main:app --reload command through uv
Run tests: uv run pytest
Run w/ Docker: docker build -t country-router
               docker run -p 8000:8000 country-router
```

## Example

Any advise for common problems or issues.
```
domainname.com/PAN
  output: {
           "dest":"PAN",
           "route":["USA","MEX","GTM","HND","NIC","CRI","PAN"]
          }

domainname.com/blz
  output: {
          "dest":"BLZ",
          "route":["USA","MEX","BLZ"]
          }

domainname.com/nfl
  output: {
          "detail":"Cannot Find Country Code nfl"
          }
```
