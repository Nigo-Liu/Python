import requests
import json
import logging

logger = logging.getLogger(__name__)


def get_status_code_and_json(self, response):
    try:
        return response.status_code, response.json()
    except Exception:
        return response.status_code, None


def get_users(self, endpoint, headers):
    url = '{0}/api/v2/users'.format(endpoint)
    return self.requests.get(url=url, headers=headers, auth=('admin','admin'))

def get_job_list(self):
    project_id = configs.tenant_id
    url = '{0}/jobs/?project={1}'.format(self._url, project_id)
    return self.get_status_code_and_json(requests.get(
        url=url, headers=self._headers, verify=False))

def create_jobs(self, job_name, job_type, job_image, job_flavor,
                job_command, schedule=None, a_zone=None,
                server=None, location=None, mountPath=None, runs=None):
    try:
        url = '{0}/jobs/'.format(self._url)
        job = str(job_type)
        image = str(job_image)
        # logger.debug(job_flavor)
        flavor = int(job_flavor)
        name = str(job_name)
        sched = str(schedule)
        availability_zone = str(a_zone)
        command = str(job_command)
        # logger.debug(runs)
        job_run = int(runs)
        # logger.debug(server)
        nfs = str(server)
        # logger.debug(location)
        locate = str(location)
        # logger.debug(mountPath)
        mnt = str(mountPath)
        data = {'name': name,
                'type': job,
                'project': configs.tenant_id,
                'image': image,
                'flavor': flavor,
                'command': command,
                }
        if schedule:
            data['schedule'] = sched
        if a_zone:
            data['availability_zone'] = availability_zone
        if runs:
            data['runs'] = job_run
        if server and location and mountPath:
            data['volumes'] = [{"server": nfs,
                                "location": locate, "mountPath": mnt}]
        # logger.debug(data)
        return self.get_status_code_and_json(requests.post(
            url=url, data=json.dumps(data),
            headers=self._headers, verify=False))
    except Exception as e:
        logger.error('create jobs error from backend: {}'.format(str(e)))
        return None

def delete_jobs(self, job_id):
    url = '{0}/jobs/{1}/'.format(self._url, job_id)
    return self.get_status_code_and_json(requests.delete(
        url=url, headers=self._headers, verify=False))

def get_job_details(self, job_id):
    url = '{0}/jobs/{1}/'.format(self._url, job_id)
    return self.get_status_code_and_json(requests.get(
        url=url, headers=self._headers, verify=False))

# To be modify
def update_job(self, job_id, job_name=None, job_image=None,
               command=None, schedule=None,
               server=None, location=None, mountPath=None):
    try:
        url = '{0}/jobs/{1}/'.format(self._url, job_id)
        data = {

        }
        if job_name:
            data['name'] = job_name
        if job_image:
            data['image'] = job_image
        if command:
            data['command'] = command
        if schedule:
            data['schedule'] = schedule

        if server and location and mountPath:
            data['volumes'] = [{'server': server,
                                'location': location,
                                'mountPath': mountPath}]
        logger.debug(url)
        logger.debug(data)
        return self.get_status_code_and_json(requests.patch(
            url=url, data=json.dumps(data),
            headers=self._headers, verify=False))
    except Exception as e:
        logger.error('job update goc api error: {}'.format(str(e)))
        return None

def get_job_run_list(self, job_id):
    url = '{0}/jobs/{1}/runs/'.format(self._url, job_id)
    return self.get_status_code_and_json(requests.get(
        url=url, headers=self._headers, verify=False))

def get_job_run_detail(self, job_id, run_id):
    url = '{0}/jobs/{1}/runs/{2}/'.format(self._url, job_id, run_id)
    return self.get_status_code_and_json(requests.get(
        url=url, headers=self._headers, verify=False))


def stop_job_run_type(self, job_id, run_id, run_type_stop):
    try:
        url = '{0}/jobs/{1}/runs/{2}/{3}/'.format(
            self._url, job_id, run_id, run_type_stop)
        return self.get_status_code_and_json(requests.post(
            url=url, headers=self._headers, verify=False))
    except Exception as e:
        logger.error(
            'stop job runner type error from backend : {}'.format(str(e)))
        return None

def job_action(self, job_id, action):
    try:
        url = '{0}/jobs/{1}/{2}/'.format(self._url, job_id, action)
        return self.get_status_code_and_json(requests.post(
            url=url, headers=self._headers, verify=False))
    except Exception as e:
        logger.error('job action error from backend : {}'.format(str(e)))
        return None