function Category(){
    var self = this;
    self.category = ko.observable();

    self.saveCategory = function(){

    }

    self.updateCategory = function(){}

}

function Job(){
    var self = this;
    self.jobTitle = ko.observable();
    self.jobList = ko.observableArray();

    self.addJob = function(){
        self.jobList.append(self.jobTitle)
    }
    self.saveJob = function(){
    }

    self.updateJob = function(){}
}

ko.applyBindings(new Category());
ko.applyBindings(new Job());