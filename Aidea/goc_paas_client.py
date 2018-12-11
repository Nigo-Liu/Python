import requests
import json
import logging


logger = logging.getLogger(__name__)


class APIJob():
    def __init__(self, request=None):
        super(APIJob, self).__init__(request)

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
            # logger.debug(job_id)
            url = '{0}/jobs/{1}/'.format(self._url, job_id)
            data = {

            }
            # logger.debug(job_name)
            if job_name:
                data['name'] = job_name
            # logger.debug(job_type)
            # if job_type:
            #     data['type'] = job_type
            # logger.debug(job_image)
            if job_image:
                data['image'] = job_image
            # logger.debug(type(job_flavor))
            # if job_flavor:
            #     data['flavor'] = job_flavor
            # logger.debug(command)
            if command:
                data['command'] = command
            # logger.debug(schedule)
            if schedule:
                data['schedule'] = schedule
            # logger.debug(a_zone)
            # if a_zone:
            #     data['availability_zone'] = a_zone
            # logger.debug(runs)
            # if runs:
            #     data['runs'] = runs
            # logger.debug(server)
            # logger.debug(location)
            # logger.debug(mountPath)
            if server and location and mountPath:
                data['volumes'] = [{'server': server,
                                    'location': location,
                                    'mountPath': mountPath}]
            # if server and location and mountPath:
            #     data['volumes'][0]['server'] = server,
            #     data['volumes'][0]['location'] = location,
            #     data['volumes'][0]['mountPath'] = mountPath
            # if location:
            #     data['volumes'][0]['location'] = location
            # if mountPath:
                        #     data['volumes'][0]['mountPath'] = mountPath
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

    # To be modify
    # def get_job_run_type(self, job_id, run_id, run_type):
    #     url = '{0}/jobs/{1}/runs/{2}/{3}/'.format(
    #         self._url, job_id, run_id, run_type)
    #     return self.get_status_code_and_json(requests.get(
    #         url=url, headers=self._headers, verify=False))

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
        # *** job action submit / stop  ***
        try:
            url = '{0}/jobs/{1}/{2}/'.format(self._url, job_id, action)
            return self.get_status_code_and_json(requests.post(
                url=url, headers=self._headers, verify=False))
        except Exception as e:
            logger.error('job action error from backend : {}'.format(str(e)))
            return None