
function validateForm() {
	
	
	 var x = document.getElementById("companyname").value;
	var y = document.getElementById("address1").value;
	
    if (x == null || x == "") {
        alert("Company Name must be filled out");
        return false;
    }
	 if (y == null || y == "") {
        alert("address1  must be filled out");
        return false;
    }
		return true; 
}


function validateEmail(email) {
  var emailReg = /^([\w-\.]+@([\w-]+\.)+[\w-]{2,7})?$/;
  var result = email.replace(/\s/g, "").split(",");        
  for(var i = 0;i < result.length;i++) {
      if(!emailReg.test(result[i])) {
          return false;
      }
  }       
  return true;
}//validateEmail
	
$(document).ready(function() 
{
	//$("input").attr("required",true);	var company = $("#listBoxCompany").val();		if(company == "Vendor"){		$("#Vender-detail1").show();		$("#Vender-detail2").show();		$("#Vender-detail3").show();	}	else if(company == "Customer-Vendor"){		$("#Vender-detail1").show();		$("#Vender-detail2").show();		$("#Vender-detail3").show();	}	else{		$("#Vender-detail1").hide();		$("#Vender-detail2").hide();		$("#Vender-detail3").hide();	}	
$(document).on("change", "#listBoxCompany", function(){		var company = $("#listBoxCompany").val();
		if(company == "Vendor"){		$("#Vender-detail1").show();		$("#Vender-detail2").show();		$("#Vender-detail3").show();	}	else if(company == "Customer-Vendor"){		$("#Vender-detail1").show();		$("#Vender-detail2").show();		$("#Vender-detail3").show();	}	else{		$("#Vender-detail1").hide();		$("#Vender-detail2").hide();		$("#Vender-detail3").hide();	}});
function validateNumaric(event){
	
		 if(event.which != 8 && isNaN(String.fromCharCode(event.which))){
		   alert("Only Numeric Is Allowed");
			   return true;
		}else{
		   return false;
	   }
	}//validateNumaric
	
	
	
$(document).on("focusout", "#email", function(){
		 var isEmail=$(this).val();
		 if(validateEmail(isEmail)){
		 }else{
			  $(this).focus();
			 alert("Enter Valid email");
			 $(this).val(""); 
			
		 $(this).focus();
		 }
	});//email

	
 	
(function($,W,D){
    var JQUERY4U = {};

    JQUERY4U.UTIL ={
        setupFormValidation: function(){
            //form validation rules

			/* $("#edit-profile").validate({

                rules: {
                    contactperson:{
						required: false,
						contactperson: true
						},
                    companyname:{
						required: false
					},
					
                    email: {
                        required: false,
                        email: false
                    },
					landmark: {
                        required: false
                       
                    },
                    pincode: {
                        required: false,
                        
                    },
					contactno1: {
                        required: false,
                        
                    },
					contactno2: {
                        required: false,
                        
                    },
					faxno: {
                        required: false
                        
                    },
                    cstno: "required"
                },
	messages: {
             
				
                    pincode:{
								required: "This Field Is Required",
								minlength: "pincode must be 6 characters long"
							},
				 contactno1:{
								required: "This Field Is Required",
								minlength: "contactno must be 10 characters long"
							},
				 contactno2:{
								required: "This Field Is Required",
								minlength: "contactno must be 10 characters long"
							},
					  faxno:{
								required: "This Field Is Required"
							},
					
					  email: "This Field Is Required",
                      cstno: "This Field Is Required",
					website: "This Field Is Required",
					landmark:"*landmark Field Is Required",
				contactperson:"This Field Is Required", 
                companyname: "This Field Is Required",
				 
                      tinno: "This Field Is Required"
					  
                },
                submitHandler: function(form) {
                    form.submit();
                }
            }); */
        }
    }

    //when the dom has loaded setup form validation rules
    $(D).ready(function($) {
        JQUERY4U.UTIL.setupFormValidation();
    });

})(jQuery, window, document);//function($,W,D) 

function validAlpha(e){
		
		var keypressed = e.which || e.keyCode;

if ((keypressed >=65 && keypressed <= 90) // letters
    || (keypressed >=48 && keypressed <= 57) // digits
    || keypressed === 8 // backspace
    || keypressed === 27 // escape
    || keypressed === 46 // delete
    || (keypressed >= 35 && keypressed <= 40) // end, home, arrows
    // TODO: shift, ctrl, alt, caps-lock, etc
    ) {
		return true;
  // do something
}else{
	return false;
}
	}
function allowOnlyAlpha(evt){
	 var charCode = (evt.which) ? evt.which : event.keyCode
		if ((charCode != 46 || $(this).val().indexOf('.') != -1) && (charCode < 65 || charCode > 90)&& (charCode < 97 || charCode > 122)&&charCode!=8&&charCode!=32) {
			return false;
		} 
  else{
	  return true;
  }
}


			
$(document).on("keypress","#contactperson",function(evt){
	
		if(allowOnlyAlpha(evt)){
			return true;
			}
	else{
		alert("Number and Special char. are not allowed"); 
		var str=$(this).val();
		str = str.replace(/[^\a-z\t\s\+]/g,"");
		$(this).val(str);
				return false;
	}
});


   
$('#tinno').keyup(function(event){

      $(this).attr('');
		var str=$(this).val();
		str = str.replace(/[^0-9\.]+/g, "");
		$(this).val(str);
		
	});//#tinno
   


});


$(document).on('focus','.inputlabel_wrapper input', function () {
	var inputlabel_wrapper = $(this).closest('.inputlabel_wrapper');
	inputlabel_wrapper.addClass('active_inputlabel');
});
$(document).on('focusout','.inputlabel_wrapper input', function () {
	var inputlabel_wrapper = $(this).closest('.inputlabel_wrapper');
	if( !jQuery(this).val() ) {
		inputlabel_wrapper.removeClass('active_inputlabel');		
	}else{
		inputlabel_wrapper.addClass('active_inputlabel');		
	}
});
$(document).on('focus','.inputlabel_wrapper textarea', function () {
	var inputlabel_wrapper = $(this).closest('.inputlabel_wrapper');
	inputlabel_wrapper.addClass('active_inputlabel');
});
$(document).on('focusout','.inputlabel_wrapper textarea', function () {
	var inputlabel_wrapper = $(this).closest('.inputlabel_wrapper');
	if( !jQuery(this).val() ) {
		inputlabel_wrapper.removeClass('active_inputlabel');		
	}else{
		inputlabel_wrapper.addClass('active_inputlabel');		
	}
});


$(document).ready(function() {
    $('#customers').select2('open').select2('close');
});