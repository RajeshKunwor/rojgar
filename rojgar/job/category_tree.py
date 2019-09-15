from .models import Category, Job

class JobClass(object):

    def __init__(self, id, category, name):
        self.id = id
        self.category = category
        self.name = name
    def __repr__(self):
        return self.name

class CategoryClass(object):

    def __init__(self,id=None, parent=None, name=None):
        self.id = id
        self.parent = parent
        self.name = name
        self.category_list = []
        self.job_list = []

    def __repr__(self):
        return self.name

def recurse(cate):
    category = CategoryClass(cate.id, cate.parent_id, cate.name)
    child_cate = Category.objects.filter(parent=cate.id)
    job = Job.objects.filter(category_id=cate.id)

    for j in job:
        jb = JobClass(j.id, j.category_id, j.name)
        category.job_list.append(jb)

    for child in child_cate:
        ch = recurse(child)
        category.category_list.append(ch)

    return category



def root_category():
    final_list = []
    root_cate = Category.objects.filter(parent=None)
    for cate in root_cate:
        temp = recurse(cate)
        final_list.append(temp)
    return final_list

