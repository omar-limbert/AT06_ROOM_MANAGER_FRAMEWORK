from behave import step


@step(u'I {method} to {endpoint}')
def step_impl(context, method, endpoint):
    context.method = method
    context.endpoint = endpoint
