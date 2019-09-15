function ViewModel(){
    var self = this;
    self.category = ko.observableArray()
    self.loadData = function(){
        $.get("http://127.0.0.1:4000/api/job/list_categorys", function(data){
            console.log(data)
            self.category(data);
//            $("#mytable").treetable({ expandable: true });
//            $(".advance").treetable({ expandable: true });
        });
    }
    self.loadData();

    self.updateCategory = function(cate){
        console.log(cate)
    }
}
ko.applyBindings(new ViewModel());