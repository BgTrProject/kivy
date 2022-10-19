# import csv
# import json
#
# csv_path2="/home/bilgi/Desktop/zzzzbing.csv"
# csv_path="/home/bilgi/Desktop/bing_aramalar.csv"
# txt_path="/home/bilgi/Desktop/zzdd.txt"
# csv_file = csv_path
# txt_file =txt_path
#
# with open(txt_file, "w") as my_output_file:
#     with open(csv_file, "r") as my_input_file:
#         [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
#     my_output_file.close()
#
#
# def deser(self,contentz):
#     try:
#         contentz=contentz.decore("utf-8")
#     except AttributeError:
#         pass
#     try:
#         body=json.loads(contentz)
#     except json.decoder.JSONDecodeError:
#         body=contentz
#     if self._data_wrapper and isinstance(body,dict) and "content" in body:
#         body=body["content"]
#     return body
#
