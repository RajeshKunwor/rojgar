function EmployeeBioModelView(){
    var self = this;
    var empId = Number($("#empId").val());
    self.education = ko.observable();
    self.experience = ko.observable();
    self.other = ko.observable();
    $.get("http://127.0.0.1:4000/api/employee/get_employee_bio",{emp_id: empId }, function(data){
        self.education(data.education);
        self.experience(data.experience);
        self.other(data.other);
    });

    self.userName = ko.observable();
    self.password = ko.observable();

    self.login = function(){

    }

}
ko.applyBindings(new EmployeeBioModelView());