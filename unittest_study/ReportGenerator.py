from xml.etree import ElementTree as ET
import os
import lxml.etree as mytree
from lxml import html


class ReportGenerator(object):
    """description of class"""

    def __init__(self):
        self.testreport = "TestResult.xml"

    # If there is no "TestResult.xml", then create one
    def CreateTestResultFile(self):
        if os.path.exists(self.testreport) == False:
            newElem = ET.Element("TestCases")
            newTree = ET.ElementTree(newElem)
            newTree.write(self.testreport)

    # Write test result to xml
    def WriteResult(self, testcaseInfo):
        self.CreateTestResultFile()
        testResultFile = ET.parse(self.testreport)
        root = testResultFile.getroot()
        newElem = ET.Element("TestCase")
        newElem.attrib = {
            "ID": testcaseInfo.id,
            "Name": testcaseInfo.name,
            "Owner": testcaseInfo.owner,
            "Result": testcaseInfo.result,
            "StartTime": testcaseInfo.starttime,
            "EndTime": testcaseInfo.endtime,
            "ErrorInfo": testcaseInfo.errorinfo
        }
        root.append(newElem)

        testResultFile.write(self.testreport)

    # If there is no "TestResult.html" file exists, then create one with default style
    def CreateHtmlFile(self):
        if os.path.exists("TestResult2.html") == False:
            f = open("TestResult2.html", 'w')
            message = """<html>
            <head>    
                <title>Automation Test Result</title>
                <style>
                    table {
                            border-collapse: collapse;
                            padding: 15px;
                            font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
                            }
                    th{
                        background-color: green;
                        color: white;
                        border: 1px solid #ddd;
                        padding-bottom: 15px;
                        padding-top: 15px;
                    }
                    tr{
                        border: 1px solid #008000;
                        padding-bottom: 8px;
                        padding-top: 8px;
                        text-align: left;
                    }
                    td{
                        border: 1px solid #008000;
                    } 
                </style>
            </head>
            <body>                
                <div class='heading'>
                    <h1>Automation Test Result</h1>
                    <p class='attribute' id='start_time'><strong>Start Time:</strong> </p>
                    <p class='attribute'id='duration'><strong>Duration:</strong> </p>
                    <p class='attribute'id='total_case'><strong>Total:</strong> </p>
                    <p class='attribute'id='pass'><strong>PASS:</strong> </p>
                    <p class='attribute'id='fail'><strong>FAIL:</strong> </p>
                    <p class='description'id='task_description'><strong>task_description:</strong></p>
                </div>

                <p id='show_detail_line'>Show
                    <a href='javascript:showCase(0)'>Summary</a>
                    <a href='javascript:showCase(1)'>Failed</a>
                    <a href='javascript:showCase(2)'>All</a>
                </p>
                
                <table>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Owner</th>
                        <th>Result</th>
                        <th>StartTime</th>
                        <th>EndTime</th>
                        <th>ErrorMessage</th>
                   </tr>
                </table>
            </body>
            </html>
            """
            f.write(message)
            f.close()

    # append new test result to testresult file
    def WriteHTML(self, testcaseinfo):

        self.CreateHtmlFile()

        f = open("TestResult2.html", "r")

        htmlcontent = f.read()
        f.close()
        tree = html.fromstring(htmlcontent)

        # draw the head




        # draw the main table
        tableElem = tree.find(".//table")
        if testcaseinfo.result == "Failed":
            mytablerow = "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td bgcolor=\"#FF0000\">{3}</td><td>{4}</td><td>{5}</td><td>{6}</td></tr>".format(
                testcaseinfo.id, testcaseinfo.name, testcaseinfo.owner, testcaseinfo.result, testcaseinfo.starttime,
                testcaseinfo.endtime, testcaseinfo.errorinfo)
        else:
            mytablerow = "<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4}</td><td>{5}</td><td>{6}</td></tr>".format(
                testcaseinfo.id, testcaseinfo.name, testcaseinfo.owner, testcaseinfo.result, testcaseinfo.starttime,
                testcaseinfo.endtime, testcaseinfo.errorinfo)
        tableElem.append(mytree.HTML(str(mytablerow)))

        f = open("TestResult.html", "w")
        # html.tostring
        newContent = repr(html.tostring(tree, method="html", with_tail=False))
        newContent = newContent.replace(r"\n", "").replace(r"\t", "").replace('b\'', "")
        newContent = newContent[:len(newContent) - 1]
        f.write(newContent)
        f.close()