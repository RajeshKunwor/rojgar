function LoginViewModel(){
    var self = this;
    self.userName = ko.observable();
    self.password = ko.observable();
    var url = $("#login_form").attr("data-url");

    self.login = function(){
        userData = ko.toJSON({userName: self.userName, password: self.password});
        console.log(userData)
        $.ajax(url,
        {
            data: userData,
            type: "post",
            contentType: "application/json; charset=utf-8",
            dataType: 'json',
            success: function(response){window.open(response.response,'_self');}
            error: function(response){alert(response.response);}
        }
        );
    }

}
ko.applyBindings(new LoginViewModel());