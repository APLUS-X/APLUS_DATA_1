# !/usr/bin/env python


pg = __import__('psycopg2')
pd = __import__('pandas')
csv= __import__('csv')
import re


def pg_conn():
    db = pg.connect(host="", port="", database="bi", user="", password="")
    return db


#周一导入时修改默认行数，
row_index = 0
file_name = input('请输入抖音运营数据的文件编号:')
operate_file = 'exported.csv'
robot_file = 'exported (' + file_name + ').csv'


def open_file(file,index):
    with open(file, encoding='utf-8')as operate_file:
        operate_data = csv.reader(operate_file)
        next(operate_data)
        row = []
        for i in operate_data:
            row.append(i)
        csv_data = (row[index])
        return csv_data


def operate_sql(index):
    db = pg_conn()
    parenting_data = open_file(operate_file,index)
    cursor = db.cursor()
    sql = '''INSERT INTO ods.o_om_tiktok_summary(logdate,
                            main_page_cnt,
                            new_fans_cnt,
                            total_fans_cnt,
                            video_play_cnt,
                            likes_cnt,
                            coment_cnt,
                            share_cnt,
                            etl_datetime,
                            account_type)
               values(%s,%s,%s,%s,%s,%s,%s,%s,now(),'智伴育儿说');'''
    cursor.execute(sql, parenting_data)
    Sql = "select etl.start_one_unit(1277)"
    cursor.execute(Sql)
    db.commit()
    print(f'智伴育儿说运营数据{list(parenting_data)}导入成功')
operate_sql(row_index)


def robot_sql(index):
    db = pg_conn()
    robot_data = open_file(robot_file,index)
    cursor = db.cursor()
    sql = '''INSERT INTO ods.o_om_tiktok_summary(logdate,
                            main_page_cnt,
                            new_fans_cnt,
                            total_fans_cnt,
                            video_play_cnt,
                            likes_cnt,
                            coment_cnt,
                            share_cnt,
                            etl_datetime,
                            account_type)
               values(%s,%s,%s,%s,%s,%s,%s,%s,now(),'智伴儿童机器人');'''
    cursor.execute(sql, robot_data)
    Sql = "select etl.start_one_unit(1277)"
    cursor.execute(Sql)
    db.commit()
    print(f'智伴儿童机器人运营数据{list(robot_data)}导入成功')
robot_sql(row_index)


user_file = 'user_analysis.xls'
menu_file = 'menu_analysis.xls'


def git_html(file,num):
    read_html = pd.read_html(file, encoding='utf-8', header=0,skiprows=num, index_col=False)[0]
    values_1 = list(read_html.T.to_dict().values())
    df = pd.DataFrame(values_1)
    return df


def user_to_csv():
    df = git_html(user_file,2)
    a = df.dropna(axis=1, how='any')
    a.to_csv('user_test.csv', index=False)
user_to_csv()


def user_sql(index):
    db = pg_conn()
    user_name = 'user_test.csv'
    user_data = open_file(user_name,-(index+1))
    cursor = db.cursor()
    sql = '''INSERT INTO ods.o_wx_user_analysis(logdate,
                                                new_Attention,
                                                unfriend,
                                                net_increase,
                                                cumulative_number,
                                                etl_datetime)
           values(%s,%s,%s,%s,%s,now());'''
    cursor.execute(sql, user_data)
    Sql = "select etl.start_one_unit(1279)"
    cursor.execute(Sql)
    db.commit()
    print(f'微信用户数据{list(user_data)}导入成功')
user_sql(row_index)


def date_time():
    df = git_html(menu_file,0)
    index = str(df.head(0))
    del_index = re.search('[0-9]{4}-[0-9]{2}-[0-9]{2}', index).group()
    df.insert(0, del_index,del_index)
    df.to_csv('menu_test.csv', index=False)
date_time()


def menu_sql():
    db = pg_conn()
    with open('menu_test.csv', encoding='utf-8')as menu_file:
        menu = csv.reader(menu_file)
        next(menu)
        next(menu)
        next(menu)
        for menu_data in menu:
            cursor = db.cursor()
            sql ='''INSERT INTO ods.o_wx_menu_analysis(logdate,
                                        Version_ID,
                                        Level_1_menu,
                                        Level_2_menu,
                                        Number_of_clicks,
                                        Number_of_hits,
                                        Average_number,
                                        etl_datetime)
                values(%s,%s,%s,%s,%s,%s,%s,now());'''
            cursor.execute(sql, menu_data)
            Sql = "select etl.start_one_unit(1279)"
            cursor.execute(Sql)
            db.commit()
            cursor.close()
            print(f'菜单数据{list(menu_data)}导入成功')
menu_sql()

