from behave import step

from core.utils.common_actions import CommonActions


@when(u'I set the following parameters for a meeting')
def step_impl(context):
    context.params = {}
    for row in context.table:
        context.params["owner"] = CommonActions.parameter_validator(context, row["owner"])
        context.params["start"] = CommonActions.parameter_validator(context, row["start"])
