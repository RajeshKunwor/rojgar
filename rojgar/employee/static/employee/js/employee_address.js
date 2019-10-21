function ViewModel(){
    var self = this;
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

    var s_url = $("#employee_signup_form").attr("data-s-url");
    var d_url = $("#employee_signup_form").attr("data-d-url");
    var m_url = $("#employee_signup_form").attr("data-m-url");
    var data_post_url = $("#employee_signup_form").attr("data-post-url");
    console.log(data_post_url)

    $.get(s_url, function(data){
//     console.log(data);
        self.stateList(data);
//        self.selectedState(state);


    });


 ko.computed(function(){
		var state = Number(self.selectedState());
        if(isNaN(state)){
            state = 0;
        }
		$.get(d_url, {state: state}, function(data){
			self.districtList(data);
//			self.selectedDistrict(district);
		});
	});


 ko.computed(function(){
		var district = Number(self.selectedDistrict());
        if(isNaN(district)){
            district = 0;
        }
		$.get(m_url, {district: district}, function(data){
			self.municipalityList(data);
//			self.selectedMunicipality(municipality)
		});

	});

	self.save = function(){
        employee_data = ko.toJSON({fullName: self.fullName,
                 userName: self.userName,
                 mobileNumber: self.mobileNumber,
                 email: self.email,
                 password: self.password,
                 state: self.selectedState,
                 district: self.selectedDistrict,
                 municipality: self.selectedMunicipality,
                 wardNumber: self.wardNumber,
                 street: self.street

               })

               console.log(employee_data)
            $.ajax( data_post_url,{
                data: employee_data,
                type: "post",
                contentType: "application/json; charset=utf-8",
                dataType: 'json',
                success: function(response){alert(response.response);}

            });

//            location.reload();

	    };

    self.update = function(id){

        $.get(pu_url,{id: id.id}, function(data){
            console.log(data)
            state = data[0].province_id;
            self.selectedId(id.id)
            district = data[0].district_id;
            municipality = data[0].municipality_id;
            self.selectedState(state);
            self.selectedDistrict(district)
            self.selectedMunicipality(municipality)

        });
    };


    self.userName = ko.observable();
    self.password = ko.observable();

    self.login = function(){

    }
 }

ko.applyBindings(new ViewModel());