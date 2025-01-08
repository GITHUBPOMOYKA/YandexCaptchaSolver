import httpx

client = httpx.Client()

sitekey = 'ysc1_MgppNDUgxmXDi4sjId2mqm1sOSX8Ro3KVo3dvxUY8f599520'

print(client.post(f'https://captcha-api.yandex.ru/check?&sitekey={sitekey}', data={'rdata': 'eyJnMyI6IlNHOHFLQ1kzc0NnPTswIiwicGdyZHQiOiIxSUJZQXlyREFBZVBwc0xmcEtzbUJwZGNpTzQ9OzEiLCJwZ3JkIjoiaGpmc0VEWVVGQ2hNdjR3bHVWczZYdHJ3ODdFMmdEa09QbXk5OE8xOTFpT1RnSUJBMlNtTHkvSm1YMUdKU2NBczRMalpWaFRLdGREUjR4a1BFYWptN3VrdkJDckxGSk8wV0JvaFVwcGFscVpMWVE4aEZLQ1FSd2ZtL2djc2N2aHB6dzVNNVcyYTlYcmNURWlmUC9jTW8rWWlHQTN2aXpsZzFiRFBFVG1PT2dwY3RPRCtXSC8vVy84M3AvSkc0aXc0MkVkbWVxOWttNzgzL3B5Q1RuVEVoTGtFazA0PSJ9','key': client.post(f'https://captcha-api.yandex.ru/check?&sitekey={sitekey}', data={'sitekey': sitekey}).json()['captcha']['key']}).json()['spravka'])