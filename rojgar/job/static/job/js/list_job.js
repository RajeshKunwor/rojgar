function JobViewModel(){
    var self = this;
    self.category = ko.observable();
    self.title = ko.observable();
    self.description = ko.observable();
    self.jobList = ko.observableArray();
    self.oldCategoryList = ko.observableArray();
    self.loadCategory = function(){
        $.get("http://127.0.0.1:4000/api/job/list_category", function(data){
        self.oldCategoryList(data);
        });
    }
    self.loadCategory();
    $.get("http://127.0.0.1:4000/api/job/list_job", function(data){
        console.log(data)
        self.jobList(data);
        $('#job-table').DataTable();
    });

    self.updateJob = function(job){
        var jobId = job.id;
        console.log(jobId)
        window.open("http://127.0.0.1:4000/dashboard/job/update-job?job="+jobId,'_self');
    }
}
ko.applyBindings(new JobViewModel());