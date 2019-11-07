function ListServiceViewModel(){
    var self = this;
    self.serviceRequestList = ko.observableArray();
    self.id = ko.observable();
    var empId = Number($("#empId").val());
    $.get("http://127.0.0.1:4000/api/servicerequest/list_service_request",{ emp_id: empId}, function(data){
        console.log(data)
        self.serviceRequestList(data);
    });

    self.confirm = function(obj){
        var id = obj.id;
        self.id(id);
        console.log(self.id)
        var postData = ko.toJSON({ service_request_id:self.id })
        $.ajax("http://127.0.0.1:4000/api/servicerequest/update_status",{
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

ko.applyBindings(new ListServiceViewModel())