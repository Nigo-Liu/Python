# coding=UTF-8
import logging
import requests
import json
from gocloud.client import utils

logger = logging.getLogger(__name__)


def _set_session(session, ip, request):
    try:
        session.headers.update({'X-CSRFToken':
                                request.COOKIES.get('csrftoken'),
                                'Referer': 'https://%s' % ip})
        session.cookies.update(request.COOKIES)
        session.verify = False
    except Exception as e:
        raise e


class Request():
    def __init__(self, request, ip=None):
        self.ip = ip
        self._request = request

    def _get_req(self):
        s = requests.Session()
        _set_session(s, self.ip, self._request)
        return s

    def req_get(self, url, params=None):
        url = utils.get_service_url(self.ip, url=url)
        req = self._get_req()
        ret = req.get(url, params=params)
        logger.debug('GET status code: %d' % ret.status_code)
        try:
            ret_message = json.loads(ret.text)
        except Exception:
            ret_message = ret.text
        if ret.status_code != requests.codes.ok:
            ret.reason = ret_message
            ret.raise_for_status()
        return json.loads(ret.text)

    def req_post(self, url, data=None, files=None, headers={}):
        url = utils.get_service_url(self.ip, url=url)
        req = self._get_req()
        if len(headers) > 0:
            req.headers.update(headers)
        if files is not None:
            ret = req.post(url, data=data, files=files)
        else:
            ret = req.post(url, json=data)
        logger.debug('POST status code: %d' % ret.status_code)
        logger.debug("content: %s" % ret.content)
        try:
            ret_message = json.loads(ret.text)
        except Exception:
            ret_message = ret.text
        if ret.status_code != requests.codes.ok:
            ret.reason = ret_message
            ret.raise_for_status()
        return ret

    def req_delete(self, url, data=None, params=None):
        url = utils.get_service_url(self.ip, url=url)
        req = self._get_req()
        ret = req.delete(url, json=data, params=params)
        logger.debug('DELETE status code: %d' % ret.status_code)
        logger.debug("content: %s" % ret.content)
        try:
            ret_message = json.loads(ret.text)
        except Exception:
            ret_message = ret.text
        if ret.status_code != requests.codes.ok:
            ret.reason = ret_message
            ret.raise_for_status()
        return ret

    def req_patch(self, url, data=None):
        url = utils.get_service_url(self.ip, url=url)
        req = self._get_req()
        ret = req.patch(url, json=data)
        logger.debug('PATCH status code: %d' % ret.status_code)
        logger.debug("content: %s" % ret.content)
        try:
            ret_message = json.loads(ret.text)
        except Exception:
            ret_message = ret.text
        if ret.status_code != requests.codes.ok:
            ret.reason = ret_message
            ret.raise_for_status()
        return ret_message

    def req_put(self, url, data=None, files=None):
        url = utils.get_service_url(self.ip, url=url)
        req = self._get_req()
        ret = req.put(url, json=data, files=files)
        logger.debug('PUT status code: %d' % ret.status_code)
        logger.debug("content: %s" % ret.content)
        try:
            ret_message = json.loads(ret.text)
        except Exception:
            ret_message = ret.text
        if ret.status_code != requests.codes.ok:
            ret.reason = ret_message
            ret.raise_for_status()
        return ret_message
