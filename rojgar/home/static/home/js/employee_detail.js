function EmployeeServiceViewModel(){
    var self = this;
    self.name = ko.observable();
    self.address = ko.observable();
    self.mobile_no =  ko.observable();
    self.email = ko.observable();
    self.bio = ko.observable();
    self.loadEmployee = function(){
         var urlParams = new URLSearchParams(window.location.search);
         var emp_id = (urlParams.get('emp_id'));
        $.get("http://127.0.0.1:4000/api/home/employee_detail", {'emp_id': emp_id}, function(data){
            console.log(data)
            self.name(data.name)
            self.address(data.address)
            self.email(data.email)
            self.mobile_no(data.mobile_number)

        });
    }
    self.loadEmployee();


    self.userName = ko.observable();
    self.password = ko.observable();

    self.login = function(){

    }
};
ko.applyBindings(new EmployeeServiceViewModel());