# Internet Traffic Archive Reader

## Introduction

This project plans to read trace data in [Internet Traffic Archive](http://ita.ee.lbl.gov/html/traces.html). I plan to use a python script to transform the server log file to a one-dimension pageview data for extra usage.

## How to get origin data

This is what confused me. Although many paper use http protocol to access ita.ee.lbl.gov, google's cache use ftp protocol. Directly access this ftp server using windows desktop or winscp can't work, but filezilla succeeded.

What's more, as all the server log data is huge (WC98>8GB, other>300MB), they won't apper in this repository. If you have trouble accessing the origin data, you can contact me via email.

## How to use the script

## something need to improve

As WC98 format is different from others, it may not be implemented for a while.,m