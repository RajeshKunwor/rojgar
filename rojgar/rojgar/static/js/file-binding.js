ko.bindingHandlers.fileUpload = {
  init: function(element, valueAccessor) {
    $(element).change(function() {
      valueAccessor()(element.files[0]);
    });
  },
  update: function(element, valueAccessor) {
    if (ko.unwrap(valueAccessor()) === null) {
      $(element).wrap('<form>').closest('form').get(2).reset();
      $(element).unwrap();
    }
  }
};
