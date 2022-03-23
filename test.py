import re

phone_num_pattern = "\d{3}[-]??\d{3}[-]??\d{4}"
re_phone_num_pattern = re.compile(pattern=phone_num_pattern)
data = """
madhu 3242-5242-222222 and 546712121 and 324-542-2222"""
results = re_phone_num_pattern.findall(data)
print(results)
