function Example() {
  var self = this;

  self.uploadFile = ko.observable(null);
  self.uploadName = ko.computed(function() {
    console.log(self.uploadFile())
    return !!self.uploadFile() ? self.uploadFile().name : '-';
  });

  self.clear = function() {
    self.uploadFile(null);
  };
};

ko.bindingHandlers.fileUpload = {
  init: function(element, valueAccessor) {
    $(element).change(function() {
      valueAccessor()(element.files[0]);
    });
  },
  update: function(element, valueAccessor) {
    if (ko.unwrap(valueAccessor()) === null) {
      $(element).wrap('<form>').closest('form').get(0).reset();
      $(element).unwrap();
    }
  }
};

ko.applyBindings(new Example());