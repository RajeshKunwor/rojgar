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
};

ko.applyBindings(new ServiceViewModel());