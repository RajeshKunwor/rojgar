function ServiceRequest(){
    var self = this;
    self.client = ko.observable();
    self.employee = ko.observable();
    self.description = ko.observable();
}



ko.applyBindings(new ServiceRequest());