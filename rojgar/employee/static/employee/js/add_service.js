function EmployeeServiceModelView(){
    var self = this;
    self.service = ko.observable();
    var empID = Number($("#empID").val())
    self.empID1 = ko.observable(empID)

    self.userName = ko.observable();
    self.password = ko.observable();
    self.login = function(){}
    self.serviceList = ko.observableArray();
    $.get("http://127.0.0.1:4000/api/job/list_job", function(data){
        console.log(data)
        self.serviceList(data)
    });

    self.save = function(){
        var postData = ko.toJSON({ employee: self.empID1, job: self.service});
        console.log(postData)
        $.ajax("http://127.0.0.1:4000/api/employee/create_employee_job",{
            data: postData,
            type: 'post',
            contentType: "application/json; charset=utf-8",
            dataType: 'json',
            success: function(response){ alert(response.response)}
       });

    }
}
ko.applyBindings(new EmployeeServiceModelView());