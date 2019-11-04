function EmployeeServiceViewModel(){
    var self = this;
    self.employeeService = ko.observableArray();
    self.loadEmployeeService = function(){
         var urlParams = new URLSearchParams(window.location.search);
         var job_id = (urlParams.get('job_id'));
        $.get("http://127.0.0.1:4000/api/home/list_employee", {'job_id': job_id}, function(data){
            console.log(data)
            self.employeeService(data);
        });
    }
    self.loadEmployeeService();

    self.loadEmployeeDetail = function(obj){
        var emp_id = obj.emp_id
        console.log(emp_id)
        window.open("http://127.0.0.1:4000/employee_detail?emp_id="+emp_id,'_self')
    }

    self.userName = ko.observable();
    self.password = ko.observable();

    self.login = function(){

    }
};
ko.applyBindings(new EmployeeServiceViewModel());