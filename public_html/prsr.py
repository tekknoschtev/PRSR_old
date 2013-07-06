#!C:\Python27\python.exe

import sys
import json
import cgi
import cgitb
import yaml 



def _buildWikiTestPlan(yamlText, testTypes):
    markup = '\n'
    markup += '// ' + str(yamlText['description']['jiraId'] or 'None') + '\n'

    for category in yamlText['testPlan']:
        if category['category']['name']:
            markup += '^ ' + str(category['category']['name'] or 'None') + '\n'
            for testStep in category['category']['testSteps']:
                for item in testStep.items():
                    if any(item[0] in s for s in testTypes):
                        markup += '*Setup:* ' + str(item[1]['setup'] or 'None')
                        markup += '\\\ *Action:* ' + str(item[1]['action'] or 'None')
                        markup += '\\\ *Expected Outcome:* ' +str(item[1]['expectedOutcome'] or 'None') + '\n'
    return markup


def _buildJiraTestPlan(yamlText, testTypes):
    markup = '\n'
    markup += '|| ' + str(yamlText['description']['jiraId'] or 'None') + '|| ||' + '\n'

    for category in yamlText['testPlan']:
        if category['category']['name']:
            markup += '|| ' + str(category['category']['name'] or 'None') + '|| ||' + '\n'
            for testStep in category['category']['testSteps']:
                for item in testStep.items():
                    if any(item[0] in s for s in testTypes):
                        markup += '| *Setup:* ' + str(item[1]['setup'] or 'None')
                        markup += '\\\ *Action:* ' + str(item[1]['action'] or 'None')
                        markup += '\\\ *Expected Outcome:* ' +str(item[1]['expectedOutcome'] or 'None') + '|(?)|\n'
    return markup


def _buildCsvTestPlan(yamlText, testTypes):
    markup = ''
    markup += '"' + str(yamlText['description']['jiraId'] or 'None') + '"\n'
    markup += '"Setup","Action","Expected Outcome"\n'
    for category in yamlText['testPlan']:
        if category['category']['name']:
            markup += '"' + str(category['category']['name'] or 'None') + '"\n'
            for testStep in yamlText['testPlan']:
                for item in testStep.items():
                    if any(item[0] in s for s in testTypes):
                        markup += '"' + str(item[1]['setup'] or 'None') + '",'
                        markup += '"' + str(item[1]['action'] or 'None') + '",'
                        markup += '"' + str(item[1]['expectedOutcome'] or 'None') + '"\n'
    return markup

form = cgi.FieldStorage()

sys.stdout.write("Content-Type: application/json")

sys.stdout.write("\n")
sys.stdout.write("\n")

result = {}
result['success'] = True
result['message'] = "The command Completed Successfully"

yamlText = form.getvalue('yamlText')
yamlText = yaml.load(yamlText)
format = form.getvalue('format')
testType = form.getvalue('testType')
if testType == 'both':
    testTypes = ['testSteps','regressionSteps']
else:
    testTypes = [testType]
formattedText = ''

if format == 'wiki':
    formattedText = _buildWikiTestPlan(yamlText, testTypes)
elif format == 'jira':
    formattedText = _buildJiraTestPlan(yamlText, testTypes)
else:
    formattedText = 'Not currently supported'



result['data'] = formattedText

sys.stdout.write(json.dumps(result,indent=1))
sys.stdout.write("\n")

sys.stdout.close()