#-*-coding:utf-8-*-

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class Page():
    def get_page(request,page,data):
        # 生成paginator对象, 定义每页显示10条记录
        paginator = Paginator(data, 5)
        currentPage = int(page)
        try:
            data = paginator.page(page)  # 获取当前页码的记录
        except PageNotAnInteger:
            data = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
        except EmptyPage:
            data = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容

        dir = {
            'paginator':paginator,
            'currentPage':currentPage,
            'data':data
        }

        return dir

