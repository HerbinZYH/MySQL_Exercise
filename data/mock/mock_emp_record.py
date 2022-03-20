import random
from config import Config
import datetime

emp = ['Girotti', 'Aranda Hynes', 'Maharaj', 'Prien', 'Farnleitner',
       'Page', 'Moeyens', 'Chambers', 'Boese', 'Antonik', 'Zhang']
dept = ['Business Office', 'Personnel Department',
        'General Affairs Department', 'Research and Development Department(R&D)']


def mock_emp():
    connect = Config.connect
    cur = connect.cursor()
    now = datetime.datetime.now()

    for index, dept_name in enumerate(dept):
        cur.execute(
            'insert into dept(dept_num, dept_name) values({}, "{}");'.format(index+1, dept_name))

    for ename in emp:
        dept_num = random.randint(1, len(emp))
        salary = 10000 + random.randint(500, 2000)
        hiredate = now - \
            datetime.timedelta(weeks=random.randint(
                0, 10), days=random.randint(50, 100))
        hiredate = hiredate.strftime('%Y-%m-%d')

        cur.execute('insert into emp(ename, hiredate, salary, dept) values("{}","{}",{},{});'.format(
            ename, hiredate, salary, dept_num))
    connect.commit()
    connect.close()


if __name__ == '__main__':
    mock_emp()
