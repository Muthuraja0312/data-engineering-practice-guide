
SQL:
select account_number,concat('****',substr(account_number, 5,8),'****') as,concat(substr(mobile_number, 1, 3),'*******') as mask_mbl_number from customer_details;

select email,concat(left(email,2),'****',substring(email,position('@' in email)))as email_mask,account_number,concat('xxxx-xxxx-xxxx-',right(account_number,4)) as masked_acc_number,mobile_number,concat('xxxxxx',right(mobile_number,4)) as masked_mbl_number from customer_details


pyspark:

def mask_email(email):
    return email[0]+ "**"+email[9:]

def mask_mobile(mobile):
    return mobile[0:2]+ "**"+mobile[0]


fdf=df.withColumn("email",udf(mask_email)(df.email))
fdf.show(truncate=False)
