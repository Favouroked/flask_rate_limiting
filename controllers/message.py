from flask import Blueprint, request

from common.config import MAX_REQUEST_COUNT, TIMEOUT, redis_client
from jobs.sms import message_queue
from utils.request import validate_body
from utils.response import error_response, response

message = Blueprint('message', __name__)


@message.before_request
def rate_limiting():
    ip = request.remote_addr
    count = redis_client.get(ip)
    count = int(count) if count else None
    if count is not None:
        if count > MAX_REQUEST_COUNT:
            return error_response("You can't send another request at this time.")
        redis_client.incr(ip)
    else:
        redis_client.set(ip, 1, TIMEOUT)


@message.route('/send', methods=['POST'])
def send():
    body = request.get_json()
    status, missing_field = validate_body(body, ['to', 'message'])
    if not status:
        return error_response(f'{missing_field} is required')
    message_queue.put(body)
    return response(True, 'Queued', None)
