from behave import step
from compare import expect
from core.modules.build_expected_response import BuildResponse
from core.modules.data_settings_manager import DataSettingsManager
from core.modules.response_json_manager import ResponseJsonManager
from core.modules.response_schema_manager import ResponseSchemaManager
from core.utils.common_actions import CommonActions
from core.utils.singleton_logger import SingletonLogger

logger_agent = SingletonLogger().get_logger()


@step(u'I have {server} Server running')
def step_impl(context, server):
    logger_agent.info("SERVER: {} Server".format(server))


@step(u"I send the request")
def step_impl(context):
    print(context.request.get_item_id(), context.request.get_base_url())
    context.response = context.request.execute_request(context.method,
                                                       context.end_point)
    print(context.response)


@step(u'I {method} to {end_point}')
def step_impl(context, method, end_point):
    context.method = method
    context.end_point = end_point


@step(u"I prepare following body")
def step_impl(context):
    context.request.set_body(DataSettingsManager.fill_json_with_data_on_settings(context.text))


@step(u"I should get response with status code {status_code}")
def step_impl(context, status_code):
    expect(int(status_code)).to_equal(context.response.status_code)


@step(u"I should validate schema received with  {schema_name} schema on {schema_folder} folder")
def step_impl(context, schema_name, schema_folder):
    """
    :param schema_folder:
    :param schema_name:
    :type context: behave.runner.Context
    """

    expect(ResponseSchemaManager.is_valid_schema(context.response.json(),
                                                 schema_folder,
                                                 schema_name)).to_equal(True)


@step(u"I should validate the response contains the body json sent")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    json_response = context.response.json()
    json_expected = BuildResponse.build_expected_response(context.request.body, context.response.json())
    expect(ResponseJsonManager.is_json_equal_to(json_response, json_expected)).to_equal(True)


@step("I prepare following header")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    headers = {}
    for row in context.table:
        for heading in row.headings:
            if row[heading] in context.accounts:
                headers[heading] = context.accounts[row[heading]]
            else:
                headers[heading] = row[heading]
    context.request.set_headers(headers)


@step("I prepare following table")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    body = {}
    for row in context.table:
        for heading in row.headings:
            body[heading] = row[heading] + CommonActions.get_random_key()
    context.request.set_body(body)


@step('I keep the "id" as "$item_id" from JSON response')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print("in step",context.response.json()["_id"])
    context.item_id = context.response.json()["_id"]

@step("I saved the {item_id} of {feature} created before")
def step_impl(context,item_id,feature):
    """
    :param item_id:
    :type context: behave.runner.Context
    """
    context.request.set_item_id(context.item_id)