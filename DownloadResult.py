import boto3
import json


def download(logGroupName, logStreamName):
    client = boto3.client('logs')
    debug_info = open("./log/debug_info", 'a')
    care_info = ""
    past = None
    cur = None
    count = 1
    log_params_dic = {
        "logGroupName": logGroupName,
        "logStreamName": logStreamName,
        "limit": 1,
        "startFromHead": True
    }

    this_line = ""
    full_line = ""
    incomplete_line = False
    while cur != past or cur == None:
        if cur != None:
            log_params_dic["nextToken"] = cur
        past = cur
        response = client.get_log_events(**log_params_dic)
        cur = response["nextForwardToken"]

        if ('uuid' in str(response['events'])) or incomplete_line:
            if 'uuid' in str(response['events']):
                count = count + 1

            this_line = response['events'][0]['message']
            if incomplete_line:
                full_line = "".join((full_line, this_line))

            else:
                full_line = this_line
            try:
                dic = json.loads(full_line)
            except:
                incomplete_line = True
                continue
            incomplete_line = False
            result = dic['message']
            duns = result["customer"]["duns"]
            content_item_id = result['contentItemId']
            match = result["match"]
            create = 'No' if match else 'Yes'
            items = (content_item_id, duns, create)
            result = "\t".join(items)
            care_info = "\n".join((care_info, result))






    log_file = open('./result/log_latest.txt', 'w')
    log_file.write(str(care_info))
    log_file.close()
    debug_info.close()
    print count
