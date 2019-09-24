function EmployeeServiceViewModel(){
    var self = this;
    self.employeeId = ko.observable();
    self.employeeService = ko.observableArray();
    self.loadEmployeeService = function(){
        var empId = self.employeeId();
        $.get("",{emp_id: empId}, function(data){
            console.log(data)
            self.service(data);
        });
    }
    self.loadEmployeeService();
};
ko.applyBindings(new EmployeeServiceViewModel());