function Category(parentCategory, newCategory){
    var self = this;
    self.parentCategory = ko.observable(parentCategory);
    self.parent = self.parentCategory.id;
    self.name = newCategory;
}

function CategoryViewModel(){
    var self = this;
    self.newCategory = ko.observable();
    self.oldCategoryList = ko.observableArray();
    self.categoryList = ko.observableArray();
    self.loadCategory = function(){
        $.get("http://127.0.0.1:4000/api/job/list_category", function(data){
        self.oldCategoryList(data);
        });
    }

    self.addCategory = function(){
        self.categoryList.push(new Category(self.oldCategoryList[0],self.newCategory()));
    }

    self.removeCategory = function(cate){
        self.categoryList.remove(cate)
    }
    self.saveCategory = function(){
       var data = JSON.stringify(self.categoryList());
         console.log(data)
        var url = "http://127.0.0.1:4000/api/job/create_category"
        $.ajax({
          type: "post",
          url: url,
          data: data,
          contentType : 'application/json; charset=utf-8',
          success: function(response){ self.loadCategory();},
          error : function(){}

        });

    }

    self.loadCategory();
    self.updateCategory = function(){}

}
ko.applyBindings(new CategoryViewModel());