function Category(parentCategory, newCategory){
    var self = this;
    self.parentCategory = ko.observable(parentCategory);
    self.newCategory = newCategory;
}

function CategoryViewModel(){
    var self = this;
    self.newCategory = ko.observable();
    self.categoryList = ko.observableArray();

    self.addCategory = function(){
        self.categoryList.push(new Category("",self.newCategory()));
    }

    self.removeCategory = function(cate){
        self.categoryList.remove(cate)
    }
    self.saveCategory = function(){

    }

    self.updateCategory = function(){}

}
ko.applyBindings(new CategoryViewModel());