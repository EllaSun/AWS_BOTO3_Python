import datetime
import uuid
from fieldCol import *
import json
import boto3


def upload(my_stream_name, kinesis_region_name, DNB_file):
    kinesis_client = boto3.client('kinesis', region_name=kinesis_region_name)
    input_json_list = []
    count = 0
    data_list = []

    for line in DNB_file:
       """
	   #Delete the logic part as it is only handle special purpose.
	   """

        data_list.append(one_record)

    for data in data_list:
        kinesis_client.put_record(StreamName=my_stream_name, Data=json.dumps(data), PartitionKey='partitionKey-3')
