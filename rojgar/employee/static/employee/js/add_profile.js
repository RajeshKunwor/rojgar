function AddProfileViewModel(){
    var self = this;
    self.save = function(){
        var form = document.getElementById('update-profile-form');
        formData = new FormData(form)
        formData.append('user', Number($('#user').val()));
        formData.append('photo', $('#image')[0].files[0]);

        $.ajax({
            url: "http://127.0.0.1:4000/api/user/create_profile",
            type: "post",
            data: formData,
            contentType: false,
            processData: false,
            success: function(response) { alert(response.response);
             },
            error: function(){},
        });
    }

    self.userName = ko.observable();
    self.password = ko.observable();

    self.login = function(){

    }
}
ko.applyBindings(new AddProfileViewModel());