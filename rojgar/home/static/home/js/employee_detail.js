function EmployeeServiceViewModel(){
    var self = this;
    self.employee = ko.observableArray();
    self.loadEmployee = function(){
         var urlParams = new URLSearchParams(window.location.search);
         var job_id = (urlParams.get('emp_id'));
        $.get("http://127.0.0.1:4000/api/home/employee_detail", {'emp_id': emp_id}, function(data){
            console.log(data)
            self.employeeService(data);
        });
    }
    self.loadEmployee();


    self.userName = ko.observable();
    self.password = ko.observable();

    self.login = function(){

    }
};
ko.applyBindings(new EmployeeServiceViewModel());