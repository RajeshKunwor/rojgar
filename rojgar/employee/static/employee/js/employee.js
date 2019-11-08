function Employee(){
    var self = this;
    self.photo = ko.observable();
    var userId = Number($("#userId").val());
    $.get("http://127.0.0.1:4000/api/user/get_profile", { user_id: userId}, function(data){
        self.photo(data.image)
    });

    self.userName = ko.observable();
    self.password = ko.observable();
    self.login = function(){}
}
ko.applyBindings(new Employee());