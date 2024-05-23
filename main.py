import pandas as pd


df = pd.read_csv('data.csv')
df['transaction_date'] = pd.to_datetime(df['transaction_date'])

def hasChargeback():
    # filters the data to only show transactions that have a chargeback claim
    return df.loc[(df['has_cbk'] == True)]

def meanChargebackTime():
    # get the average time of transactions with chargeback
    result_cbk = hasChargeback()
    mean_cbk = result_cbk['transaction_date'].mean()
    print(mean_cbk)

def meanTransactionTime():
    # get the average time of all transactions
    mean_transaction = df['transaction_date'].mean()
    print(mean_transaction)

def uniqueMerchant():
    #shows the number of unique merchants in the data
    print(df['merchant_id'].nunique())

def uniqueChargebackMerchant():
    #shows the number of unique merchants with chargebacks
    result_cbk = hasChargeback()
    count_result = result_cbk['merchant_id'].nunique()
    print(count_result)

def merchantChargebackCount():
    #shows the top 10 merchants with most chargeback claims
    result_cbk = hasChargeback()
    count_result = result_cbk.groupby(['merchant_id']).size().sort_values(ascending=False)
    print(count_result.head(10).to_string())

def merchantTransactionCount():
    #shows the top 30 merchants with most transactions with or without chargeback claims
    result_cbk = df.groupby(['merchant_id']).size().sort_values(ascending=False)
    print(result_cbk.head(30).to_string())

def specificMerchantTransactions():
    #filters the data by specific merchants showing their transactions, average value of transactions and number of card numbers used
    result_cbk = df.loc[df['merchant_id'] == 1308]
    mean_cbk = result_cbk['transaction_amount'].mean()
    card_cbk = result_cbk.groupby(['card_number']).size()
    print(result_cbk.to_string())
    print(card_cbk.to_string())
    print(mean_cbk)

def chargebackCount():
    #shows the total number of chargeback claims in the data
    result_cbk = hasChargeback()
    count_cbk = result_cbk.groupby(['has_cbk']).size()
    print(count_cbk)

def transactionCount():
    #shows how many transactions have chargeback and how many does not have chargeback
    count_cbk = df.groupby(['has_cbk']).size()
    print(count_cbk)

def meanTransactionValue():
    #shows the average value of all the transactions in the data
    mean_value = df['transaction_amount'].mean()
    print(mean_value)

def meanChargebackValue():
    #shows the average value of all chargeback transactions
    result_cbk = hasChargeback()
    mean_value = result_cbk['transaction_amount'].mean()
    print(mean_value)

def uniqueUser():
    #shows the number of unique users in the data
    print(df['user_id'].nunique())

def uniqueChargebackUser():
    #shows the number of unique users with chargeback claims
    result_cbk = hasChargeback()
    count_result = result_cbk['user_id'].nunique()
    print(count_result)

def userChargebackCount():
    #shows the top 10 users with most chargeback claims in the data
    result_cbk = hasChargeback()
    count_result = result_cbk.groupby(['user_id']).size().sort_values(ascending=False)
    print(count_result.head(10).to_string())

def userCount():
    #shows the top 30 users with most transactions in the data
    count_result = df.groupby(['user_id']).size().sort_values(ascending=False)
    print(count_result.head(30).to_string())

def specificUserTransactions():
    #filters transaction by users, offering the option to also filter by merchant, the average transaction value and cards used
    result_cbk = df.loc[df['user_id'] == 11750]
    merchant_cbk = result_cbk.loc[result_cbk['merchant_id'] == 11750]
    mean_cbk = result_cbk['transaction_amount'].mean()
    card_cbk = result_cbk.groupby(['card_number']).size()
    print(result_cbk.to_string())
    print(mean_cbk)
    print(card_cbk)

def uniqueDevice():
    #shows the number of unique devices in the data
    print(df['device_id'].nunique())

def uniqueChargebackDevice():
    #shows the number of unique devices with chargeback claims
    result_cbk = hasChargeback()
    count_result = result_cbk['device_id'].nunique()
    print(count_result)

def deviceChargebackCount():
    #shows the top 10 devices with most chargeback claims
    result_cbk = hasChargeback()
    count_result = result_cbk.groupby(['device_id']).size().sort_values(ascending=False)
    print(count_result.head(10).to_string())

def deviceCount():
    #shows the top 30 devices with most transactions in the data
    count_result = df.groupby(['device_id']).size().sort_values(ascending=False)
    print(count_result.head(30).to_string())

def specificDeviceTransactions():
    #filters the data to show transaction by specific devices, their average value, and card numbers used
    result_cbk = df.loc[df['device_id'] == 342890]
    mean_cbk = result_cbk['transaction_amount'].mean()
    card_cbk = result_cbk.groupby(['card_number']).size()
    print(result_cbk.to_string())
    print(mean_cbk)
    print(card_cbk)