import traceback
import os

from slackweb import Slack
from entsoe.exceptions import NoMatchingDataError


def handle_errors(func):
    try:
        return func()
    except NoMatchingDataError as e:
        print("NoMatchingDataError")
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        push_msg_slack(traceback.format_exc())
    return None


def push_msg_slack(message):
    if 'SLACK_WEBHOOK' not in os.environ or len(os.environ['SLACK_WEBHOOK']) == 0:
        return

    SLACK_WEBHOOK = os.environ['SLACK_WEBHOOK']
    slack = Slack(url=SLACK_WEBHOOK)

    try:
        res = slack.notify(
            text="<!channel> Error on PowEUs:\n```\n{}\n```".format(message),
        )
        print(res)
    except Exception as e:
        print("Slack exception: {}".format(e))
        # if slack is down or if we reach rate limits (\o/) don't fail !!
        pass
