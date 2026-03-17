from behave import when, then
from api.login_api import login

@when('I call login API with email "{email}" and password "{password}"')
def step_impl(context, email, password):

    context.response = login(email.password)

@then('response status should be 200')
def step_impl(context):

    assert context.response.status_code == 200

@then("token should be present")
def step_impl(context)
    data = context.response.json()

    assert "token" in data