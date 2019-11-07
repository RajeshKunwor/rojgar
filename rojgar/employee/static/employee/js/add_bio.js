function EmployeeBioModelView(){
    var self = this;
    self.service = ko.observable();
    var empID = Number($("#empID").val())
    self.empID1 = ko.observable(empID)
    self.education = ko.observable();
    self.experience = ko.observable();
    self.other = ko.observable();



    self.save = function(){
        var postData = ko.toJSON({ employee: self.empID1, education: self.education, experience: self.experience, others: self.other});
        console.log(postData)
        $.ajax("http://127.0.0.1:4000/api/employee/create_employee_bio",{
            data: postData,
            type: 'post',
            contentType: "application/json; charset=utf-8",
            dataType: 'json',
            success: function(response){ alert(response.response)
            window.open("http://127.0.0.1:4000/employee/employee_bio")
            }
       });

    }


    self.userName = ko.observable();
    self.password = ko.observable();
    self.login = function(){}
}
ko.applyBindings(new EmployeeBioModelView());