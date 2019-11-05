function EmployeeModelView(){
    var self = this;
    var empID = Number($("#empId").val())
    self.empID1 = ko.observable(empID)
    var state = 0;
    var district = 0;
    var municipality = 0;
    self.stateList = ko.observableArray();
    self.districtList = ko.observableArray();
    self.municipalityList = ko.observableArray();
    self.selectedState = ko.observable();
    self.selectedDistrict = ko.observable();
    self.selectedMunicipality = ko.observable();

    self.fullName = ko.observable();
    self.userName = ko.observable();
    self.email = ko.observable();
    self.password = ko.observable();
    self.mobileNumber = ko.observable();
    self.wardNumber = ko.observable();
    self.street = ko.observable();

    $.get("http://127.0.0.1:4000/api/employee/get_employee", { 'emp_id': 1}, function(data){
        console.log(data)
        self.fullName(data.full_name)
        self.email(data.email)
       state = data.state;
        district = data.district;
        municipality = data.municipality;
        self.wardNumber(data.ward_number)
        self.street(data.street)


    });

    var s_url = $("#employee_update_form").attr("data-s-url");
    var d_url = $("#employee_update_form").attr("data-d-url");
    var m_url = $("#employee_update_form").attr("data-m-url");

     $.get(s_url, function(data){
//     console.log(data);
        self.stateList(data);
        self.selectedState(state);


    });

 ko.computed(function(){
		var state = Number(self.selectedState());
        if(isNaN(state)){
            state = 0;
        }
		$.get(d_url, {state: state}, function(data){
			self.districtList(data);
			self.selectedDistrict(district);
		});
	});


 ko.computed(function(){
		var district = Number(self.selectedDistrict());
        if(isNaN(district)){
            district = 0;
        }
		$.get(m_url, {district: district}, function(data){
			self.municipalityList(data);
			self.selectedMunicipality(municipality)
		});

	});

    self.userName = ko.observable();
    self.password = ko.observable();

    self.login = function(){

    }
}
ko.applyBindings(new EmployeeModelView());