$.validator.addMethod('mobile', function(value, element,params){
	return this.optional(element)||(/^(98|97|96)\d{8}$/).test(element.value)
},"Mobile number must be in format.Eg: 9865012746");

$.validator.addMethod('string', function(value, element){
	return this.optional(element)||(/^([^0-9]|\s)\D+$/).test(value)
}, "This field must be valid.");
$(document).ready(function(){
    $("#employee_signup_form").validate({
        rules: {
            full_name: {
                required: true,
                minlength: 4,
                string: true
            },

            mobile_number: {
                required: true,
                mobile: true

            },
            username: {
                required: true,
                minlength: 3
            },
            state: {
                required: true
            },
            municipality: {
                required: true
            },
            district: {
                required: true,
            },
            street: {
                required: true,
                minlength: 4
            },
            wardno: {
                required: true,
                number: true,
            },
            email: {
               required: true,
               email: true
            },
            password: {
               required: true,
               minlength: 8
            },
            cpassword: {
                required: true,
                equalTo: "#password"
            },

        },
        messages: {
            fullname: {
                required: "Full Name must be required.",
                minlength: "Full Name must be 4 length characters.",

            },
            username: {
                required: "User must be required.",
                minlength: "User has at least 3 characters."
            },
            email: {
                required: "Email must be required.",
                email: "Email must in format."
            },
            password: {
                required: 'Password must be required.',
                minlength: 'Password must have at least 8 character length.'
            },
            cpassword: {
                required: 'Confirm password must be required.',
                equalTo: 'Password must be matched with previous password.'
            },
            state: {
                required: "State must be required."
            },
            municipality: {
                required: "Municipality must be required."
            },
            district: {
                required: "District must be required."
            },
            street: {
                required: 'Street must be required.',
                minlength: 'Street has at least 4 characters.'
            },
            wardno: {
                required: 'Ward number must be required.',
                number: 'Ward number must be numberd.'
            },

            mobile: {
                required: "Mobile number must be required.",

            }
        }
    });
 });