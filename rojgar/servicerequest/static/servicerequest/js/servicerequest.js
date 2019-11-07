function ServiceRequest(){
    var self = this;
    var clientId = Number($("#client_id").val())
    self.client = ko.observable(clientId);
    self.status = ko.observable("pending")

    self.description = ko.observable();
    var urlParams = new URLSearchParams(window.location.search);
    var empId = Number(urlParams.get('emp_id'));
      self.employee = ko.observable(empId);

    self.send = function(){
        var postData = ko.toJSON({ client: self.client, employee: self.employee, description: self.description,status: self.status});
        console.log(postData)
        $.ajax("http://127.0.0.1:4000/api/servicerequest/create_service_request",{
            data: postData,
            type: 'post',
            contentType: "application/json; charset=utf-8",
            dataType: 'json',
            success: function(response){ alert(response.response)}
       });

    }

    self.userName = ko.observable();
    self.password = ko.observable();

    self.login = function(){

    }
}



ko.applyBindings(new ServiceRequest());


