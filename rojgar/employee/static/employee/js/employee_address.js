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

    var s_url = $("form").attr("data-s-url");
    console.log(s_url)
    var d_url = $("form").attr("data-d-url");
    var m_url = $("form").attr("data-m-url");

    $.get(s_url, function(data){
     console.log(data);
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
		var muni = Number(self.selectedDistrict());
        if(isNaN(district)){
            district = 0;
        }
		$.get(m_url, {district: district}, function(data){
			self.municipalityList(data);
//			self.selectedMunicipality(municipality)
		});

	});

	self.save = function(){


            $.ajax( post_url,{
 //	            console.log(self.selectedMunicipality, self.selectedDistrict,self.selectedState);

                data: { id: self.selectedId, state: self.selectedState, district: self.selectedDistrict, muni: self.selectedMunicipality},
                type: "post",
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
 }

ko.applyBindings(new ViewModel());