from openqa_client.client import OpenQA_Client

client = OpenQA_Client(server='openqa.opensuse.org')

print(client.openqa_request('GET', 'workers'))


# a bit of an api doc can be found if you request an invalid request

# https://openqa.opensuse.org/api/v1

# The above client seems to always address requests against the api/v1
# REST structures.

# Creating a job is documented as:
#
# +/jobs
# POST	"apiv1_create_job"	Creates a job given a list of settings passed as parameters. TEST setting/parameter is mandatory and should be the name of the test.
#
# but the README says something different
#

