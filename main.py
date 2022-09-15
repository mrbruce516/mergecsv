import glob


def write_index():
    file = 'every_day_log.csv'
    with open(file, 'r+', encoding='gbk') as f:
        content = f.read()
        f.seek(0, 0)
        text = '性能采集时间' + ',' + '业务系统' + ',' + 'pc_id'
        f.write(text + '\n' + content)


def merge():
    csv_list = glob.glob('everyday/*.csv')
    print(u'共发现%s个CSV文件' % len(csv_list))
    print(u'正在处理............')
    for i in csv_list:
        fr = open(i, 'rb').read()
        with open('every_day_log.csv', 'ab') as f:
            f.write(fr)
    print(u'合并完毕！')


if __name__ == '__main__':
    # merge()
    write_index()
