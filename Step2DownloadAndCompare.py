from DownloadResult import *
from Compare import *

logGroupName="/aws/lambda/colaTestMonitor"
logStreamName = "2017/09/26/[$LATEST]490181aab2df44e4ad6e795d7a0ee605"

manual_result_file = "./input/manualResult.txt"
download(logGroupName, logStreamName)
compare(manual_result_file)
