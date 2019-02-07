from behave import when

UPDATE_ACCOUNT_URL = f'/accounts/%s'


@when('I close the account')
def get_account_by_context(context):
    response = context.web_client.patch(UPDATE_ACCOUNT_URL % context.account_number,
                                        json={"account_status": "closed"})
    context.response = response
