function Job(category, title, image, desc){
    var self = this;
    self.category = ko.observable(category)
    self.title = title;
    self.image = image;
    self.desc = desc;

}

function JobViewModel(){
    var self = this;
    self.title = ko.observable();
    self.image = ko.observable();
    self.desc = ko.observable();
    self.jobList = ko.observableArray();

    self.addJob = function(){
        self.jobList.push(new Job("", self.title(), self.image(),self.desc()));
    }

    self.removeJob = function(job){
        self.jobList.remove(job)
    }
    self.saveJob = function(){
    }

    self.updateJob = function(){}

  }

ko.applyBindings(new JobViewModel());