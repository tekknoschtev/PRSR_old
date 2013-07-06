PRSR
====

Purpose
-------
PRSR was built as part of an effort to help standardize the way the teams at my 
office write test cases.  Through this, we were able to consolidate our test
cases within each project meaning that we could leverage the code review tools
already in use by the developers - giving us a common way to do code and test
case reviews.

Setup
-----
A web server capable of executing a python script is needed for this project to
function.  Additionally, the PyYAML needs to be installed.  You can get PyYAML
from http://pyyaml.org/. 

Usage
-----
Currently, this tool only functions for a specifically formatted test case.  A
simple example is listed below:

> # Title 
> description:
>     extrnId: Any external system ID.  We use JIRA for tracking, so we use JIRA ID
>     softwareChange: A brief description of the software change being tested
>     testStrategy: A quick summary of the testing strategy
>     comments: 
> 
> testPlan:
>     - category:
>         name: Unit being tested
>         metaSetup: Any setup instructions that apply to the testSteps below.
>         testSteps:
>             - testStep:
>                 setup: Any specific setup for this individual test
>                 action: The action being done
>                 expectedOutcome: The outcome expected after the action(s) execute.

YAML also supports lists.  If, for example, there were multiple steps involved in
setting up the test case, you could write the setup as such:

> testPlan:
>     - category:
>         name: Unit being tested
>         metaSetup: Any setup instructions that apply to the testSteps below.
>         testSteps:
>             - testStep:
>                 setup: 
>                    1. Step 1
>                    2. Step 2
>                    3. Step 3
>                 action: The action being done
>                 expectedOutcome: The outcome expected after the action(s) execute.

As long as the list of steps is indented the same under the metaSetup, setup, 
action, or expected outcome sections, PRSR should be able to handle it.