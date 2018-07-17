from behave import step, when, then

from core.modules.data_settings_manager import DataSettingsManager


@step(u'I {method} to {endpoint}')
def step_impl(context, method, endpoint):
    context.method = method
    context.end_point = endpoint


@step("I set the following body")
def step_impl(context):
    DataSettingsManager.fill_json_with_data_on_settings(context.text)
    pass


@step("All Ok")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass