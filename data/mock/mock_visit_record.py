from config import Config
import random
import datetime


def generate_visit_record_data(num=1000):
    appid_range = [10023+i for i in range(20)]
    user_name_range = ['user_' + str(i) for i in range(10)]
    visit_time_range = [i for i in range(10)]
    now = datetime.datetime.now()

    connect = Config.connect

    cur = connect.cursor()

    for _ in range(num):
        appid = random.choice(appid_range)
        user_name = random.choice(user_name_range)
        vist_time = now - datetime.timedelta(days=random.choice(
            visit_time_range), hours=random.choice(visit_time_range))
        vist_time = vist_time.strftime('%Y-%m-%d %H:%M:%S')

        cur.execute('insert into visit_record(appid, user_name, visit_time) values ({}, "{}", "{}");'.format(
            appid, user_name, vist_time))

    connect.commit()

    connect.close()


if __name__ == '__main__':
    generate_visit_record_data()
