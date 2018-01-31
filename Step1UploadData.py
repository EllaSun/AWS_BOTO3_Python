from TransAndUpload import *

my_stream_name = 'test-cola-data-services-content-item-stream'
DNB_file = open('./input/DnB_Data_2017-07-17 Truncated.txt', 'r')
kinesis_region_name = "ap-southeast-2"

upload(my_stream_name, kinesis_region_name, DNB_file)