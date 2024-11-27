# 定义变量
year = 2024
month = 11
day = 9
name = '小明'

#打印%字符串
print('我在%d年%d月%02d日开始python的学习，我-%s，一定能学好'%(year,month,day,name))

#打印format字符串
print('我在{:d}年{:d}月{:02d}日开始python的学习，我-{:s}，一定能学好'.format(year,month,day,name))