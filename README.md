# mq-python-json
Repo showing example(s) of how to consume and parse MQ event messages in Python

## Example usage
python read-mq-events.py

## Example output
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
Source: SYSTEM.ADMIN.ACCOUNTING.QUEUE  
Type: Accounting MQI  
Application: runmqsc  
Conn ID: 414D5143514D434F4E462020202020203CD9D65B01F3F722  
Total Opens : 0   
Total Closes: 0   
Total Puts : 0 (failed = 0)   
Total Gets : 0 (failed = 0)   
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
Source: SYSTEM.ADMIN.ACCOUNTING.QUEUE  
Type: Accounting MQI  
Application: runmqsc  
Conn ID: 414D5143514D434F4E462020202020203CD9D65B01F3F722   
Total Opens : 1  
Total Closes: 1  
Total Puts : 0 (failed = 0)  
Total Gets : 0 (failed = 0)  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
Source: SYSTEM.ADMIN.STATISTICS.QUEUE  
Type: Statistics MQI  
Total Opens for QM : 10  
Total Closes for QM: 4  
Total Puts for QM : 0  
Total Gets for QM : 0  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
Source: SYSTEM.ADMIN.STATISTICS.QUEUE  
Type: Statistics Queue  
- SYSTEM.ADMIN.QMGR.EVENT  
Puts : 0 (failed = 0)  
Gets : 0 (failed = 0)  
- SYSTEM.CLUSTER.COMMAND.QUEUE  
Puts : 0 (failed = 0)  
Gets : 0 (failed = 1)  
- SYSTEM.INTER.QMGR.PUBS  
Puts : 0 (failed = 0)  
Gets : 0 (failed = 1)  
- SYSTEM.INTER.QMGR.FANREQ  
Puts : 0 (failed = 0)  
Gets : 0 (failed = 1)  
- SYSTEM.BROKER.DEFAULT.STREAM  
Puts : 0 (failed = 0)  
Gets : 0 (failed = 1)  
- SYSTEM.BROKER.ADMIN.STREAM  
Puts : 0 (failed = 0)  
Gets : 0 (failed = 1)  
- SYSTEM.BROKER.INTER.BROKER.COMMUNICATIONS  
Puts : 0 (failed = 0)  
Gets : 0 (failed = 1)  
- SYSTEM.ADMIN.PERFM.EVENT  
Puts : 0 (failed = 0)  
Gets : 0 (failed = 0)  
- SYSTEM.ADMIN.ACTIVITY.QUEUE  
Puts : 0 (failed = 0)  
Gets : 0 (failed = 0)  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
Source: SYSTEM.ADMIN.ACCOUNTING.QUEUE  
Type: Accounting MQI  
Application: amqsput  
Conn ID: 414D5143514D434F4E462020202020203CD9D65B05F3F722  
Total Opens : 2  
Total Closes: 2  
Total Puts : 0 (failed = 0)  
Total Gets : 0 (failed = 0)  
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*  
Source: SYSTEM.ADMIN.ACCOUNTING.QUEUE  
Type: Accounting Queue  
Application: amqsput  
Conn ID: 414D5143514D434F4E462020202020203CD9D65B05F3F722  
- Q2  
Opens : 1  
Closes: 1  
Puts : 0 (failed = 0)  
Gets : 0 (failed = 0)  
