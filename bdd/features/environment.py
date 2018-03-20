from yaml import load
from steps import data as json_responses


def before_all(context):
    context.settings = load(open('features/test.yaml').read())
    context.base_url = ""
    context.staging_url = context.settings['staging_url']
    context.headers = {}
    context.json_responses = json_responses
    context.twitter_auth = context.settings['twitter_auth']
    context.verify_ssl = True


def after_feature(context, feature):
    context.headers.clear()