function EmployeeServiceModelView(){
    var self = this;
    var empId = Number($("#empId").val());
    self.empService = ko.observableArray();
    $.get("http://127.0.0.1:4000/api/employee/get_employee_service",{emp_id: empId }, function(data){
        self.empService(data);
    });

    self.userName = ko.observable();
    self.password = ko.observable();

    self.login = function(){

    }

}
ko.applyBindings(new EmployeeServiceModelView());