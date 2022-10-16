from time import sleep
from apscheduler.schedulers.background import BlockingScheduler
from Blog import Blog
from BlogPost import BlogPost

def post():
    print('Chuẩn bị post bài')
    blog = BlogPost()
    blog.title = 'Bài post tự động từ BlogPot'
    blog.content = 'Được xử lý theo kiểu nó tự tạo và post lên luôn'
    blog.tags=['Tự động','Đối tượng']
    blog.update_to_blog()

sched = BlockingScheduler()

# def prompt():
# 	notify_ending(message="Tự động đây")
 
post()
sched.add_job(post,'interval', seconds=60) 
sched.start()