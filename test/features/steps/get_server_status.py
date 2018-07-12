import requests
from behave import given, when, step, then
from compare import expect


@given(u'I have room manager server running')
def step_impl(context):
    print("Server Running")


@when(u'I {method} to {endpoint}')
def step_impl(context, method, endpoint):
    context.method = method
    context.endpoint = endpoint


@step(u"I send the request")
def step_impl(context):
    context.response = requests.get(url=context.base_url + context.endpoint)
    context.status_code = context.response.status_code


@then(u"I should get response with status code {status_code}")
def step_impl(context, status_code):
    expect(int(status_code)).to_equal(context.response.status_code)
