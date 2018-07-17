from behave import given, step

from core.modules.request_manager import RequestManager


@given(u'I have room manager server running')
def step_impl(context):
    print("Server Running")


@step(u"I send the request")
def step_impl(context):
    context.response = RequestManager.execute_request(context.method,
                                                      context.base_url,
                                                      context.end_point)
    context.status_code = context.response.status_code
