function JobViewModel(){
    var self = this;
    self.jobId = ko.observable();
    self.name = ko.observable();
    self.description = ko.observable();
    self.jobList = ko.observableArray();
    self.oldCategoryList = ko.observableArray();
    self.selectedCategory = ko.observable();
    self.update = ko.observable(false);
    self.loadCategory = function(){
        $.get("http://127.0.0.1:4000/api/job/list_category", function(data){
        self.oldCategoryList(data);

        });
    }
    self.loadCategory();

    self.addJob = function(){

        self.jobList.push(new Job(self.oldCategoryList[0], self.name(),self.description()));
    }

    self.removeJob = function(job){
        self.jobList.remove(job)
    }
//    self.saveJob = function(){
//        var data = JSON.stringify(self.jobList());
//         console.log(data)
//        var url = "http://127.0.0.1:4000/api/job/create_job"
//        $.ajax({
//          type: "post",
//          url: url,
//          data: data,
//          contentType : 'application/json; charset=utf-8',
//          success: function(response){ self.loadCategory();},
//          error : function(){}
//
//        });
//
//    }

    self.saveJob = function(){
        var form = document.getElementById('job-form');
        formData = new FormData(form)
        formData.append('id', self.jobId());
        formData.append('name', $('#jobTitle').val());
        formData.append('category', $('#category').val());
        formData.append('description', $('#description').val());
        formData.append('image', $('#image')[0].files[0]);
        for (var value of formData.values()) {
           console.log(value);
        }
        console.log(self.update())
        if(self.update()===true){
            $.ajax({
            url: "http://127.0.0.1:4000/api/job/update_job",
            type: "put",
            data: formData,
            contentType: false,
            processData: false,
            success: function(response) { alert(response.response) },
            error: function(){},
        });

        }
        else{
            $.ajax({
            url: "http://127.0.0.1:4000/api/job/create_job",
            type: "post",
            data: formData,
            contentType: false,
            processData: false,
            success: function(response) { alert(response.response) },
            error: function(){},
        });
        }

    }

    self.saveAndContinue = function(){
        var form = document.getElementById('job-form');
        formData = new FormData(form)
        formData.append('name', $('#jobTitle').val());
        formData.append('category', $('#category').val());
        formData.append('description', $('#description').val());
        formData.append('image', $('#image')[0].files[0]);
        for (var value of formData.values()) {
           console.log(value);
        }
        $.ajax({
            url: "http://127.0.0.1:4000/api/job/create_job",
            type: "post",
            data: formData,
            contentType: false,
            processData: false,
            success: function(response) { alert(response.response);
            window.open("http://127.0.0.1:4000/dashboard/job/create-job/",'_self');
             },
            error: function(){},
        });
    }
    url_string = window.location.href;
    var url = new URL(url_string);
    var job = url.searchParams.get("job");
    console.log(job);
    console.log(url)
    $.get("http://127.0.0.1:4000/api/job/get_job",{job: job}, function(data){
        console.log(data);
        self.selectedCategory(data.category);
        self.jobId(data.id);
        self.name(data.name);
        self.description(data.description);
        if(self.jobId()!=null){
            self.update(true);
        }
    });


    self.updateJob = function(){


    }

  }

ko.applyBindings(new JobViewModel());