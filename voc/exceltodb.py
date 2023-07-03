import pandas as pd

from .models import CustomerTB, CenterTB


core_cols = ["접수시각", "국사", "신고자의견", "연락처1", "회선명", "상세주소"]


## table_content: VOCTB
def exceltodb(table_content):
    path = table_content.voc_file.path
    _data = pd.read_excel(path, sheet_name=0, header=1, usecols="B:BF", na_values="NaN")
    _data = _data[core_cols]

    ## add related center name to VOCTB
    cent_name = _data["국사"].str[:2][1]
    center_instance = CenterTB.objects.get(cent_name=cent_name)

    df = pd.DataFrame()
    # df['voc'] = table_content                               ## related VOCTB
    # df['cent_id'] = center_instance                         ## related CenterTB
    df["receipt"] = pd.to_datetime(_data["접수시각"])
    df["cust_name"] = _data["회선명"]
    df["declaration"] = _data["신고자의견"]
    df["cust_num"] = _data["연락처1"].str.replace("-", "")  ## delete dash
    df["cust_ads"] = _data["상세주소"]

    customer_objects = [
        CustomerTB(
            voc=table_content,
            cent=center_instance,
            receipt=row["receipt"],
            cust_name=row["cust_name"],
            declaration=row["declaration"],
            cust_num=row["cust_num"],
            cust_ads=row["cust_ads"],
            tm_judge="",
        )
        for _, row in df.iterrows()
    ]

    CustomerTB.objects.bulk_create(customer_objects)  ## save all data
