# Title description: extrnId: Any external system ID. We use JIRA for tracking, so we use JIRA ID softwareChange: A brief description of the software change being tested testStrategy: A quick summary of the testing strategy comments:

testPlan: - category: name: Unit being tested metaSetup: Any setup instructions that apply to the testSteps below. testSteps: - testStep: setup: Any specific setup for this individual test action: The action being done

expectedOutcome: The outcome expected after the action(s) execute.
#Title 
description:
    extrnId: Any external system ID.  We use JIRA for tracking, so we use JIRA ID
    softwareChange: A brief description of the software change being tested
    testStrategy: A quick summary of the testing strategy
    comments: 
testPlan:
    - category:
        name: Unit being tested
        metaSetup: Any setup instructions that apply to the testSteps below.
        testSteps:
            - testStep:
                setup: Any specific setup for this individual test
                action: The action being done
                expectedOutcome: The outcome expected after the action(s) execute.
Updated because of formatting
YAML also supports lists. If, for example, there were multiple steps involved in setting up the test case, you could write the setup as such:

testPlan:
    - category:
        name: Unit being tested
        metaSetup: Any setup instructions that apply to the testSteps below.
        testSteps:
            - testStep:
                setup: 
                   1. Step 1
                   2. Step 2
                   3. Step 3
                action: The action being done
                expectedOutcome: The outcome expected after the action(s) execute.
As long as the list of steps is indented the same under the metaSetup, setup, action, or expected outcome sections, PRSR should be able to handle it.