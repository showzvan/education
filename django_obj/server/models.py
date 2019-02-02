from django.db import models
from school.models import Schools
from major.models import MajorCates,Majors


# 服务大厅 文章分类
class ServerCategorys(models.Model):
    catename = models.CharField("分类名", max_length=255, null=False)
    is_status = models.BooleanField("状态", default=True)  # true 可用  false 不可用
    # created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    # last_mod_time = models.DateTimeField(verbose_name='修改时间', auto_now=True)

    class Meta:
        verbose_name = "服务大厅文章分类"
        verbose_name_plural = verbose_name
        db_table = "zhouju_server_categorys"


# 服务大厅 文章
class ServerPosts(models.Model):
    post_title = models.CharField("文章标题", max_length=255, null=False)
    source = models.CharField("文章来源", max_length=255, default="舟炬教育")
    source_link = models.URLField("来源链接", null=False, default="http://www.zhoujuedu.com")
    post_content = models.TextField("文章内容")
    edit_time = models.DateTimeField("编辑时间", null=False, auto_now=True)
    views = models.IntegerField("阅读人数", default=0)
    cateid = models.ForeignKey("ServerCategorys", on_delete=models.CASCADE, verbose_name="分类id")
    keywords = models.CharField("关键字", max_length=255)
    is_status = models.BooleanField("状态", default=True)  # true 可用  false 不可用

    class Meta:
        verbose_name = "服务大厅文章"
        verbose_name_plural = verbose_name
        db_table = "zhouju_server_posts"


# 学习中心
class Centers(models.Model):
    name = models.CharField("中心名称", max_length=255, null=False)
    num = models.PositiveIntegerField("编号", null=False)
    address = models.CharField("地址", max_length=255, null=False)
    phone = models.CharField("电话", max_length=255)
    is_direct = models.BooleanField("是否直属", default=False)  # False 否 true 是
    is_status = models.BooleanField("状态", default=True)  # true 可用  false 不可用

    class Meta:
        verbose_name = "学习中心"
        verbose_name_plural = verbose_name
        db_table = "zhouju_centers"


# 附件表
class Attachments(models.Model):
    name = models.CharField("附件名", max_length=255, null=False)
    addtime = models.DateTimeField("添加时间", auto_now=True)
    filename = models.FileField("存储地址",upload_to="enclosure")
    # filename = models.CharField("存储地址", max_length=255)
    is_status = models.BooleanField("状态", default=True)  # true 可用  false 不可用

    class Meta:
        verbose_name = "附件表"
        verbose_name_plural = verbose_name
        db_table = "zhouju_attachments"


# 模拟题
class AQuestions(models.Model):
    LEVAL_LIST = (
        ('gqz', "高起专"),
        ('gqb', "高起本"),
        ('zsb', "专升本")
    )
    name = models.CharField("模拟题附件名", max_length=255, null=False)
    # filename = models.CharField("存储地址", max_length=255, null=False)
    filename = models.FileField("存储地址", upload_to="file")
    school_id = models.ForeignKey("school.Schools", verbose_name="所属学校", on_delete=models.DO_NOTHING)
    major_cate_id = models.ForeignKey("major.MajorCates", verbose_name="所属专业", on_delete=models.DO_NOTHING)
    leval = models.CharField("所属层次", choices=LEVAL_LIST, default='gqb',max_length=3)
    addtime = models.DateTimeField("添加时间", auto_now=True)
    is_status = models.BooleanField("状态", default=True)  # true 可用  false 不可用

    class Meta:
        verbose_name = "模拟题"
        verbose_name_plural = verbose_name
        db_table = "zhouju_aquestions"