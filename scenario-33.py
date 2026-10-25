
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
====================================================
Encryption and decryption:

using sha2 we cant do decrypt:

1. from pyspark.sql.functions import sha2, col

df = df.withColumn(
    "email_hash",
    sha2(col("email"), 256)
)
aes function help to both encrypt and derypt:

2.from pyspark.sql.functions import expr

df_encrypted = df.withColumn(
    "encrypted_email",
    expr("base64(aes_encrypt(email, '1234567890123456'))")
)

df_encrypted.show(truncate=False)
3.df_encrypted.withColumn(
    "decrypted_email",
    expr("""
        CAST(
            aes_decrypt(
                unbase64(encrypted_email),
                '1234567890123456'
            ) AS STRING
        )
    """)
).show(truncate=False)
