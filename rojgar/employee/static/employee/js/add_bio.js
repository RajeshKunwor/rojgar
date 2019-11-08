function EmployeeBioModelView(){
    var self = this;
    self.service = ko.observable();
    var empID = Number($("#empID").val())
    self.empID1 = ko.observable(empID)
    self.education = ko.observable();
    self.experience = ko.observable();
    self.other = ko.observable();
    self.emp_bio_id = ko.observable();



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

     self.update = function(){
        var postData = ko.toJSON({ emp_bio_id:self.emp_bio_id, employee: self.empID1, education: self.education, experience: self.experience, others: self.other});
        console.log(postData)
        $.ajax("http://127.0.0.1:4000/api/employee/update_employee_bio",{
            data: postData,
            type: 'put',
            contentType: "application/json; charset=utf-8",
            dataType: 'json',
            success: function(response){ alert(response.response)
            window.open("http://127.0.0.1:4000/employee/employee_bio")
            }
       });

    }

    $.get("http://127.0.0.1:4000/api/employee/get_employee_bio",{emp_id: empID }, function(data){
        self.education(data.education);
        self.experience(data.experience);
        self.other(data.other);
        self.emp_bio_id(data.id)
    });

    self.userName = ko.observable();
    self.password = ko.observable();
    self.login = function(){}
}
ko.applyBindings(new EmployeeBioModelView());