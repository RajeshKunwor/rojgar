function ServiceViewModel(){
    var self = this;

    self.service = ko.observableArray();
    self.loadService = function(){
        $.get("http://127.0.0.1:4000/api/home/list_service", function(data){
            console.log(data)
            self.service(data);
        });
    }
    self.loadService();

    self.loadEmployee = function(obj){
        var job_id = obj.id
        window.open("http://127.0.0.1:4000/employee?job_id="+job_id,'_self')
    }

    self.userName = ko.observable();
    self.password = ko.observable();

    self.login = function(){

    }

};

ko.applyBindings(new ServiceViewModel());