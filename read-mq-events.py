#  Copyright (c) IBM Corporation 2018
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#   Contributors:
#     Matthew Whitehead - Initial Contribution
import commands
import json
from collections import namedtuple

def display_accounting_queue_message():
    try:
        print "Application: " + str(x.eventData.applName)
        print "Conn ID: " + str(x.eventData.connectionId)
        for i in range(0, x.eventData.objectCount):
            print " - " + x.eventData.queueAccountingData[i].queueName
            print "   Opens : " + str(x.eventData.queueAccountingData[i].opens)
            print "   Closes: " + str(x.eventData.queueAccountingData[i].closes)
            print "   Puts  : " + str(x.eventData.queueAccountingData[i].puts[1]) + " (failed = " + str(x.eventData.queueAccountingData[i].putsFailed) + ")"
            print "   Gets  : " + str(x.eventData.queueAccountingData[i].gets[1]) + " (failed = " + str(x.eventData.queueAccountingData[i].getsFailed) + ")"
    except AttributeError:
        print "Error getting attribute"

def display_accounting_mqi_message():
    try:
        print "Application: " + str(x.eventData.applName)
        print "Conn ID: " + str(x.eventData.connectionId)
        print "Total Opens : " + str(x.eventData.opens[1])
        print "Total Closes: " + str(x.eventData.closes[1])
        print "Total Puts  : " + str(x.eventData.puts[1]) + " (failed = " + str(x.eventData.putsFailed) + ")"
        print "Total Gets  : " + str(x.eventData.gets[1]) + " (failed = " + str(x.eventData.getsFailed) + ")"
    except AttributeError:
        print "Error getting attribute"

def display_statistics_queue_message():
    try:
        for i in range(0, x.eventData.objectCount):
            print " - " + x.eventData.queueStatisticsData[i].queueName
            print "   Puts  : " + str(x.eventData.queueStatisticsData[i].puts[1]) + " (failed = " + str(x.eventData.queueStatisticsData[i].putsFailed) + ")"
            print "   Gets  : " + str(x.eventData.queueStatisticsData[i].gets[1]) + " (failed = " + str(x.eventData.queueStatisticsData[i].getsFailed) + ")"
    except AttributeError:
        print "Error getting attribute"

def display_statistics_mqi_message():
    try:
        print "Total Opens for QM : " + str(x.eventData.opens[1])
        print "Total Closes for QM: " + str(x.eventData.closes[1])
        print "Total Puts for QM  : " + str(x.eventData.puts[1])
        print "Total Gets for QM  : " + str(x.eventData.gets[1])
    except AttributeError:
        print "Error getting attribute"

while 1:

    ( rc, jsonOutput ) = commands.getstatusoutput( "/opt/mqm/samp/bin/amqsevt -w 10 -m QM1 -o json -q SYSTEM.ADMIN.STATISTICS.QUEUE -q SYSTEM.ADMIN.ACCOUNTING.QUEUE" )

    if( rc == 0 ):

        if (len(jsonOutput) > 0):

            for x in jsonOutput.split('\n\n'):
                # Parse JSON into a Python object
                try:
                    x = json.loads(x, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
                except ValueError:
                    print "Error parsing amqsevt output as JSON -> " + str(x)
                    exit

                print "*************************************"
                print "Source: " + x.eventSource.objectName
                print "Type: " + x.eventType.name

                if (x.eventType.name == "Accounting MQI"):
                    display_accounting_mqi_message()
                elif (x.eventType.name == "Accounting Queue"):
                    display_accounting_queue_message()
                elif (x.eventType.name == "Statistics MQI"):
                    display_statistics_mqi_message()
                elif (x.eventType.name == "Statistics Queue"):
                    display_statistics_queue_message()
                else:
                    print "Unknown message type: " + x.eventType.name

    else:
        print "Command failed, here is the output: " + jsonOutput

print "Finished"

