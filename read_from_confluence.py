import re
from atlassian import Confluence
import xmltojson

# Obtain an API token from: https://id.atlassian.com/manage-profile/security/api-tokens
# You cannot log-in with your regular password to these services.

confluence = Confluence(
    url='https://srijan2023.atlassian.net',
    username='hmnsh25@gmail.com',
    password='ATATT3xFfGF0b-c75wTWgZoya6pkSJvSj3g_5PCfFXsRx887IpoVnRgrxUaEuU1wSjPGZXbcGKRJqg3m_wv853bXy9oFyMO1N5GxCTnHFQYW5Pb-acClUZ6s-WXuxW1NT3CX-idhtB3irgnhU_fzS7x1X_QELK8ebsc-zLtuvbnkuPmzqaJRCps=164ECC25',
    cloud=True)

# clean = re.compile('<.*?>')
# print(confluence.get_all_spaces())
# print(confluence.get_all_pages_from_space('~712020a40603ee628a48279fd6ba87a13155bd'))
d = confluence.get_page_by_id(458757,'body.storage.value')
print(d['body']['storage']['value'])
# print(re.sub(clean, '', d['body']['storage']['value']))
