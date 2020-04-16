def get_access_token():
 url = 'https://oapi.dingtalk.com/gettoken?corpid=%s&corpsecret=%s' % (corp_id, corp_secret)
 request = urllib2.Request(url)
 response = urllib2.urlopen(request)
 response_str = response.read()
 response_dict = json.loads(response_str)
 error_code_key = "errcode"
 access_token_key = "access_token"
 if response_dict.has_key(error_code_key) and response_dict[error_code_key] == 0 and response_dict.has_key(access_token_key):
  return response_dict[access_token_key]
 else:
  return ''