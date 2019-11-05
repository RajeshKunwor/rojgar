function ServiceViewModel(){
    var self = this;
    self.service = ko.observableArray();
    self.serviceList = ko.observableArray();
    self.districtList = ko.observableArray();
    self.selectedService = ko.observable();
    self.selectedDistrict = ko.observable();

    var d_url = $("#search_employee").attr("data-d-url");

    $.get("http://127.0.0.1:4000/api/job/list_job", function(data){
        self.serviceList(data)
    });


    $.get(d_url, function(data){
        self.districtList(data);
    });

    self.loadService = function(){
        $.get("http://127.0.0.1:4000/api/home/list_service", function(data){
            console.log(data)
            self.service(data);
        });
    }
    self.loadService();

    self.search = function(){
        var service_id = self.selectedService();
        var district_id = self.selectedDistrict();
        $.get("", function(data){

        });

    }
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