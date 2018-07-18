from behave import step, then
from compare import expect
from core.modules.build_expected_response import BuildResponse
from core.modules.data_settings_manager import DataSettingsManager
from core.modules.request_manager import RequestManager
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
    context.response = RequestManager.execute_request(context.method,
                                                      context.base_url,
                                                      context.end_point)
    context.status_code = context.response.status_code


@step(u'I {method} to {end_point}')
def step_impl(context, method, end_point):
    context.method = method
    context.end_point = end_point


@step(u"I prepare following body")
def step_impl(context):
    context.body = DataSettingsManager.fill_json_with_data_on_settings(context.text)


@step(u"I should get response with status code {status_code}")
def step_impl(context, status_code):
    expect(int(status_code)).to_equal(context.response.status_code)


@step(u"I should validate the {schema} schema received")
def step_impl(context, schema):
    """
    :param schema:
    :type context: behave.runner.Context
    """

    expect(ResponseSchemaManager.is_valid_schema(context.response.json(), schema)).to_equal(True)


@step(u"I should validate the response contains the body json sent")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    json_response = context.response.json()
    json_expected = BuildResponse.build_expected_response(context.body, context.response.json())
    expect(ResponseJsonManager.is_json_equal_to(json_response, json_expected)).to_equal(True)


@step(u"I send create request")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.response = RequestManager.execute_request(context.method,
                                                      context.base_url,
                                                      context.end_point,
                                                      headers=context.headers,
                                                      body=context.body,
                                                      )
    context.status_code = context.response.status_code
    context.item_id = context.response.json()["_id"]


@step("I send update request")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.response = RequestManager.execute_request(context.method,
                                                      context.base_url,
                                                      context.end_point,
                                                      item_id=context.item_id,
                                                      headers=context.headers)


@step("I send delete request")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.response = RequestManager.execute_request(context.method,
                                                      context.base_url,
                                                      context.end_point,
                                                      item_id=context.item_id,
                                                      headers=context.headers)


@step("I prepare following header")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    for row in context.table:
        for heading in row.headings:
            context.headers[heading] = context.accounts[row[heading]]


@step("I prepare following table")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    for row in context.table:
        for heading in row.headings:
            context.body[heading] = row[heading] + CommonActions.get_random_key()


@step(u'I keep the "id" as "$id_meeting" from the previous step')
def step_impl(context):
    resp_json = context.response.json()
    context.item_id = resp_json["_id"]
    context.after_item_id = resp_json["_id"]
    context.id_meeting = resp_json["_id"]


@step(u'I construct a expected response')
def step_impl(context):
    context.actual_json = context.resp.json()
    context.expect_json = context.data
    context.expect_json['_id'] = context.id_meeting
    context.expect_json['body'] = context.actual_json['body']


@then(u'the built expected response should be equal to the obtained response')
def step_impl(context):
    result = ResponseJsonManager.is_json_equal_to(context.actual_json, context.expect_json, )
    expect(result).to_be_truthy()
