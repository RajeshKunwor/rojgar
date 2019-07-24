function Job(category, title, image, desc){
    var self = this;
    self.categorys = ko.observable(category)
    self.title = title;
    self.image = image;
    self.desc = desc;
    self.category = self.categorys.id

}

function JobViewModel(){
    var self = this;
    self.title = ko.observable();
    self.image = ko.observable();
    self.desc = ko.observable();
    self.jobList = ko.observableArray();
    self.oldCategoryList = ko.observableArray();
    self.loadCategory = function(){
        $.get("http://127.0.0.1:4000/api/job/list_category", function(data){
        self.oldCategoryList(data);
        });
    }
    self.loadCategory();

    self.addJob = function(){
        self.jobList.push(new Job(self.oldCategoryList[0], self.title(), self.image(),self.desc()));
    }

    self.removeJob = function(job){
        self.jobList.remove(job)
    }
    self.saveJob = function(){
    }

    self.updateJob = function(){}

  }

ko.applyBindings(new JobViewModel());