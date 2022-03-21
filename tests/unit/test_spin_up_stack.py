import aws_cdk as core
import aws_cdk.assertions as assertions

from spin_up.spin_up_stack import SpinUpStack

# example tests. To run these tests, uncomment this file along with the example
# resource in spin_up/spin_up_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = SpinUpStack(app, "spin-up")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
