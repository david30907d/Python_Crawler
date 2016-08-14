# coding = utf-8
import json,re,sys,pyprind,requests,urllib,traceback
from pyquery import PyQuery as pq
title_key = ["url", "property","genres", "title", "teacher"]   
comment_key = ["push-content"]


url = 'https://www.ptt.cc/bbs/NCHU-Courses/M.1310189510.A.D97.html'

def get_ppt_content(url):
    re = requests.get(url)
    re = re.text.replace(':','')
    course_unit = []#course_unit 在結束時就會回傳json格式
    title_arr = []
    d = pq(re)#now d means $ in JQuery
    title = d('.article-meta-value:eq(2)').text()
    t = title.split(' ')
    title_arr.append(url)
    title_arr.append(t[0])    
    genre = t[1].split('/')[0]
    title_arr.append(genre)
    course_name = t[1].split('/')[2]
    title_arr.append(course_name)
    teacher = t[1].split('/')[3]
    title_arr.append(teacher)      
    row = dict(zip(title_key,title_arr))   
    push_arr=[]    
    for i in d('.push-content'):
        '''with open ('ptt_comment.json','a',encoding = 'UTF-8') as f:
          f.write(d(i).text()+'\n')'''
        push_arr.append(d(i).text())
    for i in comment_key:
        row[i] = push_arr
    course_unit.append(row)
    return course_unit
    
    


def start_json(json_path):
    with open(json_path, 'w' ,encoding = 'UTF-8') as json_file:
        json_file.truncate()#如果沒有傳入參數的話，就會本全文清空
        #若傳入整數n的話，是指把n位置以後的文字都刪掉
        json_file.write('[')#單純只是寫入而已

def to_json(json_path,arr,notFirst = False):
    # print(arr)
    with open(json_path, 'a', encoding='UTF-8') as json_file:
        #with 述句執行完畢後會自動關檔，後面的as 則是把開檔完的reference指派給as 後的變數
        #as裡面的名稱在外部是看不到的，是區域變數
        for d in arr:
            json_str = json.dumps(d, ensure_ascii=False, sort_keys=True)
            #在這裡使用到json的module,dump是轉存，將python的物件型態轉成json的物件型態
            #因為json是js的型態；ensure_ascii若為true(預設)
            #就會確保所有輸入的字元都是ascii，若非則跳過那個字元
            #設為false就會照原樣輸出
            #sort_keys預設為false，功用為把key做排序
            json_file.write('{}{}'.format((',' if notFirst else ''), json_str))
            #str.format()這個函式，會在{}裡面填入字串，{}裡面可以放index或key名稱
            notFirst = True

def end_json(json_path):
    with open(json_path, 'a' ,encoding = 'UTF-8') as json_file:
        json_file.write(']')

if __name__  ==  "__main__":
    start_json('ptt_comment.json')
    course_unit=get_ppt_content(url)
    #print(course_unit)
    to_json('ptt_comment.json',course_unit,False)
    end_json('ptt_comment.json')