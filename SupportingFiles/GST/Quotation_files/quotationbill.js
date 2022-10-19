var pre=($("#quotation_id").val());
var tapelement="first";
var count=0;
var call=0;

var rowdata = '<tr class="product-item-row">';
rowdata += '	<td>';
rowdata += '		<label class="product-item-row-number">1</label>';
rowdata += '	</td>';
rowdata += '	<td>';
rowdata += '		<label class="product-item-row-number product-item-row-number-tab">1</label><div class="inputlabel_wrapper"><input class="product-combobox"  placeholder="Enter Product name"  maxlength="500"  ><label>Product Name</label></div>';
rowdata += '		<input class="hidden-item-product-id" 			name="hidden-item-product-id[]" 		type="hidden" >';
rowdata += '		<input class="hidden-item-detail-product-id" 	name="hidden-item-detail-product-id[]" 		type="hidden" >';
rowdata += '		<input class="hidden-item-product-name" 		name="hidden-item-product-name[]" 		type="hidden" >';
rowdata += '		<input class="hidden-item-product-uom" 		name="hidden-item-product-uom[]" 		type="hidden" >';
rowdata += '		<input class="hidden-item-product-is_transport" 		name="hidden-item-product-is_transport[]" 		type="hidden" >';
rowdata += '		<input class="hidden-item-product-cgst" 		name="hidden-item-product-cgst[]" 		type="hidden" >';
rowdata += '		<input class="hidden-item-product-sgst" 		name="hidden-item-product-sgst[]" 		type="hidden" >';
rowdata += '		<input class="hidden-item-product-igst" 		name="hidden-item-product-igst[]" 		type="hidden" >';
rowdata += '		<input class="hidden-item-product-att1-name"	name="hidden-item-product-att1-name[]" 	type="hidden" >';
rowdata += '		<input class="hidden-item-product-att1-val"		name="hidden-item-product-att1-val[]" 	type="hidden" >';
rowdata += '		<input class="hidden-item-product-att2-name"	name="hidden-item-product-att2-name[]" 	type="hidden" >';
rowdata += '		<input class="hidden-item-product-att2-val"		name="hidden-item-product-att2-val[]" 	type="hidden" >';
rowdata += '		<input class="hidden-item-product-att3-name"	name="hidden-item-product-att3-name[]" 	type="hidden" >';
rowdata += '		<input class="hidden-item-product-att3-val"		name="hidden-item-product-att3-val[]" 	type="hidden" >';
rowdata += '		<input class="hidden-item-product-att4-name"	name="hidden-item-product-att4-name[]" 	type="hidden" >';
rowdata += '		<input class="hidden-item-product-att4-val"		name="hidden-item-product-att4-val[]" 	type="hidden" >';
rowdata += '		<div class="inputlabel_wrapper"><textarea  class="product_note"  placeholder="Item Note..."  name="product_note[]" maxlength="800" >'+default_product_note+'</textarea><label>Product Note</label></div>';
rowdata += '	</td>';
rowdata += '	<td>';
rowdata += '		<div class="inputlabel_wrapper"><input type="text" name="hsccode[]" class="hsccode"  placeholder="HSN/SAC" class="span2" style="width:60px;" maxlength="20"  ><label>HSN/SAC</label></div>';
rowdata += '	</td>';
rowdata += '	<td>';
rowdata += '		<div class="inputlabel_wrapper"><input type="text" name="quantity[]" class="quantity decimal_numeric_only"  placeholder="Qty." class="span2" style="width:50px;" maxlength="10" data-msg="Not enough stock!" ><label>Qty</label></div>';
rowdata += '		<label class="product-quantity-available"></label>';
rowdata += '	</td>';
rowdata += '<td>';
rowdata += '<div class="inputlabel_wrapper">';
rowdata += '<input type="text" name="uom" class="uom" placeholder="UOM"  maxlength="20">';
rowdata += '<label>UOM</label>';
rowdata += '</div>';
rowdata += '</td>';
rowdata += '	<td><center>';
rowdata += '		<div class="inputlabel_wrapper"><input type="text" name="rate[]" class="rate decimal_numeric_only"    placeholder="Price" style="width:100px;"  class="span2" maxlength="10" ><label>Price</label></div>';
rowdata += '		<div class="currency-fields" >';
rowdata += '		<div class="currency-factor-symbol">Rs</div>';
rowdata += '		<div class="inputlabel_wrapper"><input type="text" class="rate_usd decimal_numeric_only"    placeholder="Price" class="span2" maxlength="10"  ><label>Price</label></div>';
rowdata += '		</div>';
rowdata += '		<label class="customer_rate_label" ></label>';
rowdata += '		<span class="last-price-tip" ><i class="fa fa-info"></i></span>';
rowdata += '	</td></center>';
rowdata += '	<td class="discount_field">';
rowdata += '		<div class="inputlabel_wrapper"><input type="text" name="disc[]" class="disc decimal_numeric_only"   class="span2" style="width:50px;"  maxlength="10"  ><label>Disc.</label></div>';
rowdata += '		<input type="hidden" name="taxable_line_value[]" class="taxable_line_value"   class="span2"   >';
rowdata += '	</td>';
rowdata += '<td  class="product_row_cgst_col">';
rowdata += '	<div class="inputlabel_wrapper">';
rowdata += '	<select name="cgst_select" class="cgst_select"   >';
rowdata += '			<option value="">--</option>';
rowdata += '			'+gst_rates_options_cgst+'';
rowdata += '		</select>												';
rowdata += '		<label for="cgst[]">CGST + SGST</label>';
rowdata += '	</div>';
rowdata += '	<input type="text" class="cgst_sgst_rate text_rate decimal_numeric_only"    readonly="readonly"   style="width:50px;"   value="0" >											<input type="hidden" name="cgst_rate[]" class="cgst_rate text_rate decimal_numeric_only"    readonly="readonly"   style="width:50px;"   value="0" > <input type="hidden" name="sgst_rate[]" class="sgst_rate text_rate decimal_numeric_only"    readonly="readonly" style="width:50px;"  value="0" >';
rowdata += '	<input type="hidden" name="cgst[]" class="cgst decimal_numeric_only"    placeholder="%"  style="width:30px;" maxlength="5"  >												';
rowdata += '	<input type="hidden" name="sgst[]" class="sgst decimal_numeric_only"    placeholder="%"  style="width:30px;" maxlength="5"  >												';
rowdata += '</td>';
rowdata += '	<td class="product_row_igst_col">';
rowdata += '		<div class="inputlabel_wrapper"><select name="igst[]" class="igst">';
rowdata += '													<option value="">--</option>';
rowdata += '			'+gst_rates_options_igst+'';
rowdata += '												</select><label>IGST</label></div>';
rowdata += '		<input type="text" name="igst_rate[]" class="igst_rate text_rate decimal_numeric_only"    readonly="readonly" class="span2" style="width:50px;" value="0" >';
rowdata += '	</td>';
rowdata += '	<td>';
rowdata += '		<div class="inputlabel_wrapper inputlabel_wrapper_half"><input type="text" name="cess[]" class="cess decimal_numeric_only"    style="width:40px;" placeholder="%"   ><label>Cess %</label></div>';
rowdata += '		<input value="" type="hidden" name="cessrate[]" class="cessrate" >';
rowdata += '		<center class="hide_unser_tab">+</center>';
rowdata += '		<div class="inputlabel_wrapper inputlabel_wrapper_half"><input type="text" name="cess_amount[]" class="cess_amount decimal_numeric_only"   placeholder="Rs"  style="width:40px;"   ><label>Cess Rs</label></div>';
rowdata += '	</td>';
rowdata += '	<td style="width:90px;" ><center>';
rowdata += '			<div class="inputlabel_wrapper"><input type="text" name="line_total[]" class="line_total decimal_numeric_only"    placeholder="Total"  class="span2" style="width:80px;"  ><label>Total</label></div>';
rowdata += '		<div class="currency-fields" >';
rowdata += '		<div class="currency-factor-symbol">Rs</div>';
rowdata += '			<div class="inputlabel_wrapper"><input type="text" class="line_total_usd"    placeholder="Total"  class="span2" ><label>Total</label></div>';
rowdata += '		</div>';
rowdata += '	</center></td>';
rowdata += '	<td>';
rowdata += '		<center>';
rowdata += '			<button type="button"  value=""  class="btn btn-primary btnadd-product-line btnadd-row-item" ><i class="fa fa-plus" ></i></button>';
rowdata += '			<button type="button"  value=""  class="btn btn-danger btnremove-product-line btnremove-row-item"  style="display:none;"><i class="fa fa-minus" ></i></button>';
rowdata += '		</center>';
rowdata += '	</td>';
rowdata += '</tr>';
 




function InvoiceTypeSet(country,party_type = null){
	if ( $("#hidden-invoice-country").is( "select" ) ) {
		if(country == "India")			
		{												
			if(party_type == 'SEZ'){
				$("#hidden-invoice-country").html('<option value="SEZInvoice">Sez Invoice (With IGST)</option><option value="SEZInvoiceWithoutIGST">Sez Invoice (Without IGST)</option>');								
			}else{
				$("#hidden-invoice-country").html('<option value="Quotation">Regular</option><option value="BillofSupply">Bill of Supply</option>');								
			}
			$(".currency-fields").hide();
			$("body").removeClass("multicurrency-doc");
			$('#currency').val('INR - Indian Rupee');
			$('#currency').trigger("change");
		}		
		else	
		{		
			$("#hidden-invoice-country").html('<option value="ExportInvoice">Export Invoice (With IGST)</option><option value="ExportInvoiceWithoutIGST">Export Invoice (Without IGST)</option>');						
			$(".currency-fields").show();
			$("body").addClass("multicurrency-doc");
			$('#currency').trigger("change");
		}
		var defaulttype = $("#hidden-invoice-country").attr("data-value");
		if(defaulttype != "")
		{
			$('#hidden-invoice-country option[value="'+defaulttype+'"]').attr("selected","selected");
		}
		$("#hidden-invoice-country").trigger("change");
	}
	else{
		if(country == "India")			
		{		
			$(".currency-fields").hide();
			$("body").removeClass("multicurrency-doc");
			$('#currency').val('INR - Indian Rupee');
			$('#currency').trigger("change");
		}		
		else	
		{
			$(".currency-fields").show();
			$("body").addClass("multicurrency-doc");
			$('#currency').trigger("change");
		}
	}
}
function getCustomerOutstanding(){
	var data = {
        action: 'GetCustomerTotalOutstanding',
        id: $("#customers").val()
    }
	$.ajax({  
		type: "POST",  
		url: "ajaxcall.php",  
		ContentType : 'application/json',
		dataType: 'json',
		data: data,
		success: function(data){
			if(data.status=='OK')
			{
				$(".customer_outstanding_value").html(data.outstanding).removeClass("btn-link");;
			}
		},
		error: function(data){
		},
		complete: function(data){
		}
	});
}
function updateAddressData(updateShipping  = true){
	if($("#customers").val() != ""){
	var data = {
        action: 'GetCustomerAddress',
        id: $("#customers").val()
    }
	$.ajax({  
		type: "POST",  
		url: "ajaxcall.php",  
		ContentType : 'application/json',
		dataType: 'json',
		data: data,
		success: function(data){
			if(data.status=='OK')
			{
				$(".customer-information-invoice #address").html(data.address);
				$(".customer-information-invoice #phone").html(data.phone);
				$(".customer-information-invoice #gst").html(data.gst);
				$(".customer-information-invoice #cmp_gstno[data-value='']").val(data.gst);
				$(".customer-information-invoice #hidden-invoice-state[data-value='']").val(data.state);
				$(".customer-information-invoice .PlaceofSupply[data-value='']").val(data.state);		
				
				InvoiceTypeSet(data.country,data.party_type);
					
				if(data.gst == "")
				{
					$("#reverse_Charge").val("0");
					$("#reverse_Charge").attr("disabled", true).trigger("change");
				}
				else
				{
					$("#reverse_Charge").attr("disabled", false).trigger("change");
				}
				
				/*same shipping address enable & desabled code here*/
				if(updateShipping){
					var shipping_options = '';					
					var shipping_addresses_obj = jQuery.parseJSON(data.shipping_addresses);
					$.each(shipping_addresses_obj, function (i,ship_single) {
						shipping_options = shipping_options + '<option value="'+ship_single.ship_name+'" ship_address="'+ship_single.ship_address+'" ship_phone="'+ship_single.ship_phone+'" ship_pincode="'+ship_single.ship_pincode+'" ship_gstno="'+ship_single.ship_gstno+'" ship_country="'+ship_single.ship_country+'" ship_state="'+ship_single.ship_state+'" shipping_distance_eway="'+ship_single.shipping_distance_eway+'" >'+ship_single.ship_name+'</option>';
					});
					if(shipping_options != ""){
						$("#shipping_address").html(shipping_options);
					}else{
						$("#shipping_address").html('<option value="">--</option>');
					}
					if($('#shippingName').val() != "")
					{
						$("#shipping_address").val($('#shippingName').val());
					}
					$("#shipping_address").trigger('change');
				}
				
				SetIGTS();
				$(".customer_outstanding_value").html("Get Customer Oustanding").addClass("btn-link");
				$(".customer_outstanding_value").click(getCustomerOutstanding);
			}
			else
			{
				$(".customer_outstanding_value").html("").removeClass("btn-link");
			}
		},
		error: function(data){
		},
		complete: function(data){
		}
	});
	}
}

function SetIGTS(){
	
	if($("#hidden-invoice-country").val() == "SEZInvoiceWithoutIGST" ||  $("#hidden-invoice-country").val() == "ExportInvoiceWithoutIGST" || $("#hidden-invoice-country").val() == "BillofSupply")
	{
		DisableALL_IGST();
	}
	else if($("#hidden-invoice-country").val() == "SEZInvoice" || $("#hidden-invoice-country").val() == "ExportInvoice" )
	{
		EnableIGST();
	}
	else if($("#business_state").val() == $(".customer-information-invoice .PlaceofSupply").val())
	{
		DisableIGST();
	}
	else
	{
		EnableIGST();
	}
	$(window).trigger("resize");
}

function DisableALL_IGST(){
	$("#document-item-list .igst").val("").attr('readonly',true);
	$("#document-item-list .cgst").val("").attr('readonly',true);
	$("#document-item-list .sgst").val("").attr('readonly',true);
	$("#document-item-list .igst_rate").val("0");
	$("#document-item-list .cgst_rate").val("0");
	$("#document-item-list .cgst_sgst_rate").val("0");
	$("#document-item-list .sgst_rate").val("0");
	
	UpdateCalculations();
}
function DisableIGST(){
	$("#document-item-list").removeClass('tbl_igst');
	$("#document-item-list").addClass('tbl_cgst');
	$("#document-item-list .igst").val("").attr('readonly',true);
	$("#document-item-list .cgst").removeAttr('readonly');
	$("#document-item-list .cgst_select").removeAttr('disabled');
	$("#document-item-list .sgst").removeAttr('readonly');
	$("#document-item-list .igst_rate").val("0");
	$("#document-item-list .product-item-row").each(function(){
		var cgstPer = $(this).find(".hidden-item-product-cgst").val();
		var sgstPer = $(this).find(".hidden-item-product-sgst").val();
		if($(this).find(".cgst:not([readonly])").val() == "")
		{
			$(this).find(".cgst:not([readonly])").val(cgstPer);
			$(this).find(".cgst_select").val(cgstPer);
		}
		if($(this).find(".sgst:not([readonly])").val()== "")
		{
			$(this).find(".sgst:not([readonly])").val(sgstPer);
		}
		
	});
	UpdateCalculations();
}
function EnableIGST(){
	$("#document-item-list").addClass('tbl_igst');
	$("#document-item-list").removeClass('tbl_cgst');
	$("#document-item-list .igst").removeAttr('readonly');
	$("#document-item-list .cgst").val("").attr('readonly',true);
	$("#document-item-list .cgst_select").val("").attr('disabled',true);
	$("#document-item-list .sgst").val("").attr('readonly',true);
	$("#document-item-list .cgst_rate").val("0");
	$("#document-item-list .cgst_sgst_rate").val("0");
	$("#document-item-list .sgst_rate").val("0");
	$("#document-item-list .product-item-row").each(function(){
		var igstPer = $(this).find(".hidden-item-product-igst").val();
		if($(this).find(".igst:not([readonly])").val()=="")
		{
			$(this).find(".igst:not([readonly])").val(igstPer);
		}
		
	});
	UpdateCalculations();
}

function SetPaymentModeDueDate(){
	/* if($("#payment").val() == 'CASH' || $("#payment").val() == 'ONLINE')
	{
		$("#datepicker_lr").attr("data-old-due",$("#datepicker_lr").val());
		$("#datepicker_lr").val("");
		$("#datepicker_lr").prop('disabled',true);
	}
	else
	{
		$("#datepicker_lr").prop('disabled',false);
		if($("#datepicker_lr").attr("data-old-due") !="" && typeof $("#datepicker_lr").attr("data-old-due") !== typeof undefined && $("#datepicker_lr").attr("data-old-due") !== false){
			var ddd = $("#datepicker_lr").attr("data-old-due");
			$("#datepicker_lr").val(ddd);
		}
	} */
}

$(document).ready(function(){

	$(document).on("change", "#customers", function(){
		updateAddressData();
	});
	if($("#customers").val() != "")
	{
		updateAddressData();
	}
	
	$(document).on("change", "#hidden-invoice-country", function(){
		SetIGTS();
	});
	$(document).on("change", ".customer-information-invoice .PlaceofSupply", function(){
		SetIGTS();
	});
	SetIGTS();
	refreshSn();
	$( "#PlaceofSupply" ).autocomplete({
		source: availablePlaceofSupply,
		minLength:0
	}).focus(function(){
            $(this).autocomplete("search");
    });
});

function refreshSn()
{
    var time = 600000;
    setTimeout(
        function ()
        {
			var data = {
				action: 'refreshSn'
			}
			$.ajax({
				url: 'ajaxcall.php',
				type: "POST",
				cache: false,
				global: false,
				ContentType : 'application/json',
				dataType: 'json',
				data: data,
				complete: function () {refreshSn();}
			});
		},
		time
	);
}
/*on change quotation_id data get	*/
$(document).on("change", "#quotation_id", function(){
	
	
	if(isNaN($(this).val())){
		alert("Only Numeric Value.");
		return false;
	}
	var data = {
        action: 'ValidateQuotationID',
        id: parseInt($(this).val())
    }
	$.ajax({  
		type: "POST",  
		url: "ajaxcall.php",  
		ContentType : 'application/json',
		dataType: 'json',
		data: data,
		success: function(data){
			if(data.status=='USED')
			{	
				alert("Quotation No Is Already Exist!!");  
				$("#quotation_id").val("");
				$("#quotation_id").focus();
			}
		},
		error: function(data){
		},
		complete: function(data){
		}
	});
});
/*on change quotation_id data get	*/


function parseDate(s) {
  var months = {jan:0,feb:1,mar:2,apr:3,may:4,jun:5,
                jul:6,aug:7,sep:8,oct:9,nov:10,dec:11};
  var p = s.split('-');
  return new Date(p[2], months[p[1].toLowerCase()], p[0]);
}
function checkValidDate(){
	var IsValidDate = true;
	var datestr = $("#datepicker_bill").val();
	if(datestr != "")
	{
		var checkDate =  parseDate(datestr);
		var minDate = new Date(session_start, 3,1);
		var maxDate = new Date(session_end, 2,31);
		var validDate = (checkDate >= minDate && checkDate <= maxDate)?true:false;
		if(!validDate)
		{
			alert('Please select Valid Invoice Date.');
			IsValidDate = false;
			$("#datepicker_bill").focus();
		}
	}
	else
	{
		alert('Please select Valid Invoice Date.');
		IsValidDate = false;
		$("#datepicker_bill").focus();
	}
	return IsValidDate;
}

$(document).ready(function(){

	
	$( "#datepicker_bill" ).datepicker(
	{
		changeMonth: true,
		changeYear: true,
		dateFormat :'dd-M-yy',
		minDate : new Date(session_start, 3,1),
		maxDate : new Date(session_end, 2,31)
	});
	
	$( "#datepicker_shippingBillDate" ).datepicker(
	{
		changeMonth: true,
		changeYear: true,
		dateFormat :'dd-M-yy'
	});
	
	$( "#datepicker_challan" ).datepicker(
	{
		changeMonth: true,
		changeYear: true,
		dateFormat :'dd-M-yy'
	});
	$( "#datepicker_order" ).datepicker(
	{
		changeMonth: true,
		changeYear: true,
		dateFormat :'dd-M-yy'
	});
	
	
	UpdateTrigger();
	
	$( "#product_quotation_form" ).validate({
		rules: {
			field: {required: true},
			ignore: ':hidden, [readonly=readonly],[readonly],[readonly=true]',
		},
		messages: {
		},
		submitHandler: function(form) {
			if(validateCurrentRowsForSubmit() && checkValidDate() && qty_validate_items())
			{
				$("#SameShippingAdd").attr("disabled", false);
				$("#customers").attr("disabled", false);
				$.ajax({
					type: form.method,
					data: $(form).serialize(),
					dataType: 'json',
					beforeSend: function() {
						$("body").addClass("is-loading");
					},
					success: function(data) {
						if(data.status=='OK')
						{
							window.location.href = data.redirect;
						}
						else
						{
							$(".gogst_popup-content").html(data.data);
							if(data.errorTitle)
							{
								$(".gogst_popup-header").html(data.errorTitle);
							}
							else{
								$(".gogst_popup-header").html("Error in Saving Quotation");
							}
							$(".gogst_popup-header").html("Error in Saving Quotation");
							$('#gogst_popup').popup({
								scrolllock: true,
								transition: 'all 0.3s'
							});
							$('#gogst_popup').popup('show');
							$("body").removeClass("is-loading");
						}
					},
					error: function(xhr, status, error) { 
						var err = xhr.responseText;
						$(".gogst_popup-content").html(err.Message);
						if(data.errorTitle)
						{
							$(".gogst_popup-header").html(data.errorTitle);
						}
						else{
							$(".gogst_popup-header").html("Error in Saving Quotation");
						}
						$('#gogst_popup').popup({
							scrolllock: true,
							transition: 'all 0.3s'
						});
						$('#gogst_popup').popup('show');
						$("body").removeClass("is-loading");
					},
					complete: function() {
						
					}
				});
			}
		}
	});
	
});	

function UpdateCalculations(){
	SetPaymentModeDueDate();
	var reverse_Charge = $("#reverse_Charge").val();
	if(reverse_Charge=="1")
	{
		reverse_Charge = true;
		$(".reverse_charge_label_text").html("Tax Under Reverse Charge :");
	}
	else
	{
		reverse_Charge = false;
		$(".reverse_charge_label_text").html("Total Tax :");
	}
	
	var total_taxable_value = 0;
	var grand_total_value = 0;
	var total_tax_value = 0;
	
	
	var row_total_qty = 0;
	var row_total_price = 0;
	var row_total_disc = 0;
	var row_total_cgst_rate = 0;
	var row_total_sgst_rate = 0;
	var row_total_igst_rate = 0;
	var row_total_cess_rate = 0;
	var row_total_total=0;
	
	$("#document-item-list .product-item-row").each(function(){
		var quantity = $(this).find(".quantity").val();
		var is_transport = $(this).find(".hidden-item-product-is_transport").val();
		var rate = $(this).find(".rate").val();
		var disc = $(this).find(".disc").val();
		var taxable_line_value = $(this).find(".taxable_line_value").val();
		var cgst = "";
		var sgst = "";
		var igst = "";
		var cess = $(this).find(".cess").val();
		var cessrate = "";
		var cess_amount = $(this).find(".cess_amount").val();
		var cgstrate = "";
		var sgstrate = "";
		var igstrate = "";
		if($(this).find(".cgst:not([readonly])").length > 0 ) { cgst = $(this).find(".cgst:not([readonly])").val(); }
		if($(this).find(".sgst:not([readonly])").length > 0 ) { sgst = $(this).find(".sgst:not([readonly])").val(); }
		if($(this).find(".igst:not([readonly])").length > 0 ) { igst = $(this).find(".igst:not([readonly])").val(); }
		if(cgst != "" && (cgst.charAt(cgst.length - 1) != ".") ){
			cgst  = cgst.toString().substring(0, cgst.toString().indexOf('.') + 1 + gst_rate_decimal_rounding_by);
			$(this).find(".cgst:not([readonly])").val(cgst);
			cgst = parseFloat(cgst);
		}
		if(sgst != "" && (sgst.charAt(sgst.length - 1) != ".") ){
			sgst  = sgst.toString().substring(0, sgst.toString().indexOf('.') + 1 + gst_rate_decimal_rounding_by);
			$(this).find(".sgst:not([readonly])").val(sgst);
			sgst = parseFloat(sgst);
		}
		/* if(igst != "" && (igst.charAt(igst.length - 1) != ".") ){
			igst  = igst.toString().substring(0, igst.toString().indexOf('.') + 1 + gst_rate_decimal_rounding_by);
			$(this).find(".igst:not([readonly])").val(igst);
			igst = parseFloat(igst);
		} */
		var row_total = 0;
		
		if( quantity != "" && rate != "" )
		{
			if((quantity.charAt(quantity.length - 1) != "." && quantity_decimal_rounding_by > 0 && quantity.toString().indexOf('.') > -1  ))
			{
				quantity  = quantity.toString().substring(0, quantity.toString().indexOf('.') + 1 + quantity_decimal_rounding_by);
				$(this).find(".quantity").val(quantity);
				quantity = parseFloat(quantity);
			}
			else if( quantity_decimal_rounding_by == 0 && quantity.toString().indexOf('.') > -1  )
			{
				quantity  = quantity.toString().substring(0, quantity.toString().indexOf('.') + 1 + quantity_decimal_rounding_by);
				quantity = parseFloat(quantity);
				$(this).find(".quantity").val(quantity);
			}
			else{
				quantity = parseFloat(quantity);
			}
			if((rate.charAt(rate.length - 1) != "." && price_decimal_rounding_by > 0 && rate.toString().indexOf('.') > -1  ))
			{
				rate  = rate.toString().substring(0, rate.toString().indexOf('.') + 1 + price_decimal_rounding_by);
				$(this).find(".rate").val(rate);
				rate = parseFloat(rate);
			}
			else if( price_decimal_rounding_by == 0 && rate.toString().indexOf('.') > -1  )
			{
				rate  = rate.toString().substring(0, rate.toString().indexOf('.') + 1 + price_decimal_rounding_by);
				$(this).find(".rate").val(rate);
			}
			else{
				rate = parseFloat(rate);
			}
			if(disc !="")
			{
				disc = parseFloat(disc);
			}
			else
			{
				disc = 0;
			}
			if(!(is_transport == 1 || is_transport == "1")){
				row_total_qty += quantity;
			}
			row_total_price += rate;
			row_total =  quantity*rate;
			
			var DiskRs = 0;
			if(disc>0 && discount_in=='percentage')
			{
				DiskRs = (disc*row_total)/100;
			}						
			
			if(disc>0 && discount_in=='rupee' && discount_per_item == 1)
			{
				DiskRs = disc*quantity;
			}
			if(disc>0 && discount_in=='rupee' && discount_per_item == 0)
			{
				DiskRs = disc;
			}
			
			
			row_total_disc += DiskRs;
			row_total = row_total-DiskRs;
			row_total = Math.round(row_total * taxable_decimal_rounding) / taxable_decimal_rounding;
			
			
			$(this).find(".taxable_line_value").val(row_total);
			
			total_taxable_value += row_total;
			if(cgst != "" ){
				cgst = parseFloat(cgst);
				if(cgst>0){
					cgstrate = (row_total*cgst)/100;
					cgstrate = Math.round(cgstrate * gst_decimal_rounding) / gst_decimal_rounding;
				}
			}
			if(sgst != "" ){
				sgst = parseFloat(sgst);
				if(sgst>0){
					sgstrate = (row_total*sgst)/100;
					sgstrate = Math.round(sgstrate * gst_decimal_rounding) / gst_decimal_rounding;
				}
			}
			if(igst != "" ){
				igst = parseFloat(igst);
				if(igst>0){
					igstrate = (row_total*igst)/100;
					igstrate = Math.round(igstrate * gst_decimal_rounding) / gst_decimal_rounding;
				}
			}
			if(cess != "" ){
				cess = parseFloat(cess);
				if(cess>0){
					cessrate = (row_total*cess)/100;
					cessrate = Math.round(cessrate * gst_decimal_rounding) / gst_decimal_rounding;
				}
			}
			if(cgstrate !=""){
				$(this).find(".cgst_rate").val(cgstrate);
				$(this).find(".cgst_sgst_rate").val(cgstrate+sgstrate);
				if(!reverse_Charge){
					row_total = row_total+cgstrate;
				}
				total_tax_value+=cgstrate;
				row_total_cgst_rate += cgstrate;
			}
			else{
				$(this).find(".cgst_rate").val("0");
				$(this).find(".cgst_sgst_rate").val("0");
			}
			if(sgstrate !=""){
				$(this).find(".sgst_rate").val(sgstrate);				
				if(!reverse_Charge){
					row_total = row_total+sgstrate;
				}
				total_tax_value+=sgstrate;
				row_total_sgst_rate += sgstrate;
			}
			else{
				$(this).find(".sgst_rate").val("0");
			}
			if(igstrate !=""){
				$(this).find(".igst_rate").val(igstrate);
				if(!reverse_Charge){
					row_total = row_total+igstrate;
				}
				total_tax_value+=igstrate;
				row_total_igst_rate += igstrate;
			}
			else{
				$(this).find(".igst_rate").val("0");
			}
			
			if(cessrate !=""){
				$(this).find(".cessrate").val(cessrate);
				if(!reverse_Charge){
					row_total = row_total+cessrate;
				}
				total_tax_value+=cessrate;
				row_total_cess_rate += cessrate;
			}
			else{
				$(this).find(".cessrate").val("0");
			}
			
			
			if(cess_amount != "" ){
				cess_amount = parseFloat(cess_amount);
				if(cess_amount>0){
					cess_amount = Math.round(cess_amount * gst_decimal_rounding) / gst_decimal_rounding;
					
					$(this).find(".cess_amount").val(cess_amount);
					if(!reverse_Charge){
						row_total = row_total+cess_amount;
					}
					total_tax_value+=cess_amount;
					row_total_cess_rate += cess_amount;
				
				}
			}
			row_total = Math.round(row_total * taxable_decimal_rounding) / taxable_decimal_rounding;
			grand_total_value += row_total;
			row_total_total += row_total;
			$(this).find(".line_total").val(row_total);
			
			var currency_rate = $("#currency_rate").val();
			var currency = $("#currency").val();
			if(currency_rate == "")
			{
				currency_rate = 1;
			}
			else{
				currency_rate = parseFloat(currency_rate);
			}
			$(this).find(".rate_usd").val(conver_amount_with_factor(rate,currency_rate));
			$(this).find(".line_total_usd").val(conver_amount_with_factor(row_total,currency_rate));
		}
	});
	
	row_total_qty = Math.round(row_total_qty * quantity_decimal_rounding) / quantity_decimal_rounding;
	row_total_price = Math.round(row_total_price * price_decimal_rounding) / price_decimal_rounding;
	row_total_disc = Math.round(row_total_disc * 100) / 100;
	row_total_cgst_rate = Math.round(row_total_cgst_rate * gst_decimal_rounding) / gst_decimal_rounding;
	row_total_sgst_rate = Math.round(row_total_sgst_rate * gst_decimal_rounding) / gst_decimal_rounding;
	row_total_igst_rate = Math.round(row_total_igst_rate * gst_decimal_rounding) / gst_decimal_rounding;
	row_total_cess_rate = Math.round(row_total_cess_rate * gst_decimal_rounding) / gst_decimal_rounding;
	row_total_total=Math.round(row_total_total * 100) / 100;
	
	
	
	
	var other_tax_in_rupee =  $("#other_tax_in_rupee:checked").val();
	var other_tax_type_minus =  $("#other_tax_type_minus:checked").val();
	var other_tax_value =  $("#other_tax_value").val();
	var other_tax_amount =  $("#other_tax_amount").val();
	
	
	if(other_tax_in_rupee == "0")
	{
		other_tax_amount = ((other_tax_value * grand_total_value)/100);
		other_tax_amount=Math.round(other_tax_amount * 100) / 100;
		if(other_tax_type_minus == "1")
		{
			grand_total_value  = grand_total_value - other_tax_amount;
		}
		else
		{
			grand_total_value  = grand_total_value + other_tax_amount;
		}
		$("#other_tax_amount_label").html(other_tax_amount);
	}
	else 
	{
		other_tax_amount = other_tax_value;
		other_tax_amount=Math.round(other_tax_amount * 100) / 100;
		if(other_tax_type_minus == "1")
		{
			grand_total_value  = grand_total_value - other_tax_amount;
		}
		else
		{
			grand_total_value  = grand_total_value + other_tax_amount;
		}
		$("#other_tax_amount_label").html('');
	}
	$("#other_tax_amount").val(other_tax_amount);
	
	
	
	
	var total_discount_in_rupee =  $("#total_discount_in_rupee:checked").val();
	var total_discount_type_minus =  $("#total_discount_type_minus:checked").val();
	var total_discount_value =  $("#total_discount_value").val();
	var total_discount_amount =  $("#total_discount_amount").val();
	if(total_discount_in_rupee == "0")
	{
		total_discount_amount = ((total_discount_value * grand_total_value)/100);
		total_discount_amount=Math.round(total_discount_amount * 100) / 100;
		if(total_discount_type_minus == "1")
		{
			grand_total_value  = grand_total_value - total_discount_amount;
		}
		else
		{
			grand_total_value  = grand_total_value + total_discount_amount;
		}
		$("#total_discount_amount_label").html(total_discount_amount);
	}
	else 
	{
		total_discount_amount = total_discount_value;
		total_discount_amount=Math.round(total_discount_amount * 100) / 100;
		if(total_discount_type_minus == "1")
		{
			grand_total_value  = grand_total_value - total_discount_amount;
		}
		else
		{
			grand_total_value  = grand_total_value + total_discount_amount;
		}
		$("#total_discount_amount_label").html('');
	}
	$("#total_discount_amount").val(total_discount_amount);
	
	
	
	
		var old_grandTotal = grand_total_value;
		if(parseInt(enable_round_off,10) == 1){		grand_total_value = Math.round(grand_total_value);			}
		var round_off_value = grand_total_value - old_grandTotal;
	
	total_taxable_value = Math.round(total_taxable_value * taxable_decimal_rounding) / taxable_decimal_rounding;
	grand_total_value = Math.round(grand_total_value * 100) / 100;
	round_off_value = Math.round(round_off_value * 100) / 100;
	total_tax_value = Math.round(total_tax_value * gst_decimal_rounding) / gst_decimal_rounding;
	
	var currencycode = getCurrencyCodeFromName();
	var currencysymbol = cur_symbol[currencycode];
	var rupeesymbol = cur_symbol["INR"];
	$("#row_total_qty_lable").html(row_total_qty);
	$("#row_total_qty").val(row_total_qty);
	$("#row_total_price_lable").html(row_total_price);
	$("#row_total_price").val(row_total_price);
	$("#row_total_disc_lable").html(row_total_disc);
	$("#row_total_disc").val(row_total_disc);
	$("#row_total_cgst_rate_lable").html(row_total_cgst_rate+row_total_sgst_rate);
	$("#row_total_cgst_rate").val(row_total_cgst_rate);
	/* $("#row_total_sgst_rate_lable").html(row_total_sgst_rate); */
	$("#row_total_sgst_rate").val(row_total_sgst_rate);
	$("#row_total_igst_rate_lable").html(row_total_igst_rate);
	$("#row_total_igst_rate").val(row_total_igst_rate);
	$("#row_total_cess_rate_lable").html(row_total_cess_rate);
	$("#row_total_cess_rate").val(row_total_cess_rate);
	$("#row_total_total_lable").html(row_total_total);
	$("#row_total_total").val(row_total_total);
	
	$("#total_taxable_lable").html(total_taxable_value);
	$("#total_taxable").val(total_taxable_value);
	$("#total_tax_lable").html(total_tax_value);
	$("#total_tax").val(total_tax_value);
	$("#grand_total_lable").html(grand_total_value);
	$("#grand_total").val(grand_total_value);
	$("#hidden_round_off_value").val(round_off_value);
	$("#grandtotalwords").text(number2text(grand_total_value));	
	$("#hidden_grandtotalwords").val(number2text(grand_total_value));	
	
	if($("#currency").val()=="INR - Indian Rupee")
	{
		
		$("#currency_grandtotal_lable").html("");
		$("#currency_grandtotal").val("");
		
		$("#currency_total_in_words").html("");
		$("#hidden_currency_total_in_words").val("");
		
	}
	else
	{
		var currency_rate = $("#currency_rate").val();
		if(currency_rate == "")
		{
			currency_rate = 1;
		}
		else{
			currency_rate = parseFloat(currency_rate);
		
		}
		var currency_grandtotal = Math.round(conver_amount_with_factor(grand_total_value,currency_rate ) * 100) / 100;
		
		$("#grand_total_lable").html(rupeesymbol+" "+grand_total_value);
		
		
		$("#currency_grandtotal_lable").html(currencysymbol+ " " + currency_grandtotal);
		$("#currency_grandtotal").val(currency_grandtotal);
		
		
		$("#currency_total_in_words").html(number2text_with_currency(currency_grandtotal,currencycode));
		$("#hidden_currency_total_in_words").val(number2text_with_currency(currency_grandtotal,currencycode));
	}
	$('.inputlabel_wrapper input').each(function(){
		var inputlabel_wrapper = $(this).closest('.inputlabel_wrapper');
		if( !jQuery(this).val() ) {
			inputlabel_wrapper.removeClass('active_inputlabel');
		}else{
			inputlabel_wrapper.addClass('active_inputlabel');
		}
	});
	$('.inputlabel_wrapper textarea').each(function(){
		var inputlabel_wrapper = $(this).closest('.inputlabel_wrapper');
		if( !jQuery(this).val() ) {
			inputlabel_wrapper.removeClass('active_inputlabel');
		}else{
			inputlabel_wrapper.addClass('active_inputlabel');
		}
	});
}
function UpdateTrigger(){
	$("#document-item-list .quantity, #document-item-list .rate, #document-item-list .disc, #document-item-list .cgst, #document-item-list .sgst, #document-item-list .igst, #document-item-list .cess, #document-item-list .cess_amount,#total_discount_value,#total_discount_in_rupee,#total_discount_type_minus,#other_tax_value,#other_tax_in_rupee,#other_tax_type_minus,#currency_rate").off('keyup change blur').on('keyup change blur',function(){
		UpdateCalculations();
	});			
	$(".rate_usd,.line_total_usd").off('change').on('change',function(){
		UpdateCalculationsUSD($(this));
	});
	$("#document-item-list .line_total").off('blur').on('blur',function(){	
	var ParentRowOfCurTotal = $(this).parents(".product-item-row");	
	var quantity = $(ParentRowOfCurTotal).find(".quantity").val();	
	var line_total = $(ParentRowOfCurTotal).find(".line_total").val();	
	var rate = $(ParentRowOfCurTotal).find(".rate").val();	
	var disc = $(ParentRowOfCurTotal).find(".disc").val();	
	var taxable_line_value = $(ParentRowOfCurTotal).find(".taxable_line_value").val();	
	var cgst = "";	
	var sgst = "";	
	var igst = "";
	var cess = "";	
	var cess_amount = "";
	var cgstrate = "";	
	var sgstrate = "";	
	var igstrate = "";	
	if($(ParentRowOfCurTotal).find(".cgst:not([readonly])").length > 0 ) { 
		cgst = $(ParentRowOfCurTotal).find(".cgst:not([readonly])").val(); 
	}		
	if($(ParentRowOfCurTotal).find(".sgst:not([readonly])").length > 0 ) { 
		sgst = $(ParentRowOfCurTotal).find(".sgst:not([readonly])").val();
	}		
	if($(ParentRowOfCurTotal).find(".igst:not([readonly])").length > 0 ) {
		igst = $(ParentRowOfCurTotal).find(".igst:not([readonly])").val();
	}
	if(cgst != "" && (cgst.charAt(cgst.length - 1) != ".") ){
		cgst = parseFloat(cgst);
		cgst = Math.round(cgst * gst_rate_decimal_rounding) / gst_rate_decimal_rounding;
		$(ParentRowOfCurTotal).find(".cgst:not([readonly])").val(cgst);
	}
	if(sgst != "" && (sgst.charAt(sgst.length - 1) != ".") ){
		sgst = parseFloat(sgst);
		sgst = Math.round(sgst * gst_rate_decimal_rounding) / gst_rate_decimal_rounding;
		$(ParentRowOfCurTotal).find(".sgst:not([readonly])").val(sgst);
	}
	if(igst != "" && (igst.charAt(igst.length - 1) != ".") ){
		igst = parseFloat(igst);
		igst = Math.round(igst * gst_rate_decimal_rounding) / gst_rate_decimal_rounding;
		$(ParentRowOfCurTotal).find(".igst:not([readonly])").val(igst);
	}
	cess = $(ParentRowOfCurTotal).find(".cess").val();
	cess_amount = $(ParentRowOfCurTotal).find(".cess_amount").val();
	if( quantity != "" && line_total != "" )		{
		quantity = parseFloat(quantity);		
		if(quantity == 0)		
		{		
			quantity = 1;	
			$(ParentRowOfCurTotal).find(".quantity").val("1");	
		}		
		line_total = parseFloat(line_total);
		var totalTax = 0;	
		if(cgst != "" ){	
			cgst = parseFloat(cgst);	
			if(cgst>0){		
				totalTax += cgst;		
			}		
		}		
		if(sgst != "" ){
			sgst = parseFloat(sgst);
			if(sgst>0){			
				totalTax += sgst;		
			}		
		}		
		if(igst != "" ){	
			igst = parseFloat(igst);	
			if(igst>0){		
				totalTax += igst;	
			}		
		}		
		if(cess != "" ){	
			cess = parseFloat(cess);	
			if(cess>0){		
				totalTax += cess;	
			}		
		}
		
		if(cess_amount != "" ){	
			cess_amount = parseFloat(cess_amount);	
			if(cess_amount>0){		
				line_total -= cess_amount;
			}		
		}
		var taxablevalue = 0;	
		if(totalTax > 0)
		{		
			taxablevalue = (line_total*100)/(100+totalTax);	
		}		
		else	
		{		
			taxablevalue = line_total;	
		}				
		if(disc !="")		
		{			
			disc = parseFloat(disc);	
		}		
		else	
		{	
			disc = 0;	
		}		
		var DiskRs = 0;		

		if(disc>0 && discount_in=='percentage')		
		{		
			taxablevalue = (taxablevalue*100)/(100-disc);	
		}					

		if(disc>0 && discount_in=='rupee' && discount_per_item == 0)	
		{		
			taxablevalue = taxablevalue+disc;		
		}		
		if(disc>0 && discount_in=='rupee' && discount_per_item == 1)	
		{		
			taxablevalue = (taxablevalue+(disc*quantity));		
		}		
		taxablevalue += DiskRs;		
		rate = taxablevalue / quantity;		
		$(ParentRowOfCurTotal).find(".rate").val(Math.round(rate * price_decimal_rounding) / price_decimal_rounding);	
	}		
	UpdateCalculations();	
});
		
	$(".btnadd-row-item").off("click").on("click", function(){
		if(validateCurrentRows()){
			addNewRowItem($(this));
		}
	});
	$( ".btnremove-row-item").off("click").on("click", function(){
		RemoveRowItem($(this));
	});
	SetIGTS();
	$( ".product-combobox" ).autocomplete({
		source: function(request, response) {var results = $.ui.autocomplete.filter(availableProducts, request.term);response(results.slice(0, 500));},
		change: function(event, ui) {
			if (ui.item == null || ui.item == undefined) {
				var $targetparnt = $( event.target ).parents(".product-item-row");
				if(!productAllowed)
				{
					$( event.target ).val("");
					$(".gogst_popup-content").html("You do not have Access to add new Product.");
							$(".gogst_popup-header").html("Error in Adding Product");
							$('#gogst_popup').popup({
								scrolllock: true,
								transition: 'all 0.3s'
							});
							$('#gogst_popup').popup('show');
					
				}
				$( event.target ).attr("data-oldval", "");
				$($targetparnt).find(".quantity").attr('readonly',false);
				$($targetparnt).find(".hsccode").attr('readonly',false);
				$($targetparnt).find(".hidden-item-product-name").val($( event.target ).val());
				
				$($targetparnt).find(".hidden-item-product-uom").val("");
				$($targetparnt).find(".uom").attr('disabled',false);
				$($targetparnt).find(".uom").val("");
				$($targetparnt).find(".hidden-item-product-id").val("");
				$($targetparnt).find(".hidden-item-product-is_transport").val("");
				$($targetparnt).find(".hidden-item-product-cgst").val("");
				$($targetparnt).find(".hidden-item-product-sgst").val("");
				$($targetparnt).find(".hidden-item-product-igst").val("");
				$($targetparnt).find(".hidden-item-product-cess").val("");
				$($targetparnt).find(".hidden-item-product-cess_amount").val("");
				
				$($targetparnt).find(".product-quantity-available").html("");
				$($targetparnt).find(".quantity").removeAttr("qtymax");
				
				$($targetparnt).find(".hidden-item-product-att1-name").val("");
				$($targetparnt).find(".hidden-item-product-att1-val").val("");
				$($targetparnt).find(".hidden-item-product-att2-name").val("");
				$($targetparnt).find(".hidden-item-product-att2-val").val("");
				$($targetparnt).find(".hidden-item-product-att3-name").val("");
				$($targetparnt).find(".hidden-item-product-att3-val").val("");
				$($targetparnt).find(".hidden-item-product-att4-name").val("");
				$($targetparnt).find(".hidden-item-product-att4-val").val("");
				
			}
			else{
				if (ui.item) {
					$( event.target ).attr("data-oldval", ui.item.label );
					var $targetparnt = $( event.target ).parents(".product-item-row");
					$( event.target ).val( ui.item.label );
					$($targetparnt).find( ".hidden-item-product-id" ).val( ui.item.value);
					$($targetparnt).find( ".hidden-item-product-name" ).val( ui.item.name);
					if(ui.item.product_note != "" || default_product_note == "" ) { $($targetparnt).find( ".product_note" ).val( ui.item.product_note); }
					$($targetparnt).find( ".hidden-item-product-uom" ).val( ui.item.uom);
					$($targetparnt).find( ".uom" ).val( ui.item.uom);
					$($targetparnt).find(".uom").attr('disabled',true);
					$($targetparnt).find( ".hidden-item-product-is_transport" ).val( ui.item.is_transport);
					$($targetparnt).find(".quantity").attr('readonly',false);
					if(ui.item.is_transport == 1 || ui.item.is_transport == '1')
					{
						$($targetparnt).find(".quantity").val("1");
						$($targetparnt).find(".quantity").attr('readonly',true);
					}
					else if(ui.item.is_service_product == 1 || ui.item.is_service_product == '1')
					{
						
					}
					else
					{
						if(inventory_enable){
							if(ui.item.non_salable_product != 1 || ui.item.non_salable_product != '1'){
								$($targetparnt).find(".product-quantity-available").html(ui.item.items_available);
							}
							if(allow_oversell && (ui.item.non_salable_product != 1 || ui.item.non_salable_product != '1')){
								$($targetparnt).find(".quantity").attr("qtymax",ui.item.items_available);
							}
						}
					}
					$($targetparnt).find( ".hidden-item-product-cgst" ).val( ui.item.cgst);
					$($targetparnt).find( ".hidden-item-product-sgst" ).val( ui.item.sgst);
					$($targetparnt).find( ".hidden-item-product-igst" ).val( ui.item.igst).change();
					$($targetparnt).find( ".hidden-item-product-cess" ).val( ui.item.cess);
					$($targetparnt).find( ".hidden-item-product-cess-amount" ).val( ui.item.cess_amount);
					
					$($targetparnt).find(".hidden-item-product-att1-name").val(ui.item.attr1name);
					$($targetparnt).find(".hidden-item-product-att1-val").val(ui.item.attr1val);
					$($targetparnt).find(".hidden-item-product-att2-name").val(ui.item.attr2name);
					$($targetparnt).find(".hidden-item-product-att2-val").val(ui.item.attr2val);
					$($targetparnt).find(".hidden-item-product-att3-name").val(ui.item.attr3name);
					$($targetparnt).find(".hidden-item-product-att3-val").val(ui.item.attr3val);
					$($targetparnt).find(".hidden-item-product-att4-name").val(ui.item.attr4name);
					$($targetparnt).find(".hidden-item-product-att4-val").val(ui.item.attr4val);
				
					
					$($targetparnt).find(".hsccode").val(ui.item.hsn);
					if(ui.item.sellprice != ui.item.customerprice)
					{
						$($targetparnt).find(".rate").val(ui.item.customerprice);
						$($targetparnt).find(".customer_rate_label").html(ui.item.sellprice);
						
					}
					else
					{
						$($targetparnt).find(".rate").val(ui.item.sellprice);
						$($targetparnt).find(".customer_rate_label").html('');
					}
					if($($targetparnt).find(".quantity").val() == "")
						{
							$($targetparnt).find(".quantity").val("1");
						}
						
					$($targetparnt).find(".cgst:not([readonly])").val(parseFloat(ui.item.cgst));
					$($targetparnt).find(".cgst_select:not([disabled])").val(parseFloat(ui.item.cgst));
					$($targetparnt).find(".sgst:not([readonly])").val(parseFloat(ui.item.sgst));
					$($targetparnt).find(".igst:not([readonly])").val(parseFloat(ui.item.igst));
					$($targetparnt).find(".cess").val(ui.item.cess);
					$($targetparnt).find(".cess_amount").val(ui.item.cess_amount);
					UpdateCalculations();					
				}
			}
		},
		select: function( event, ui ) {
			var $targetparnt = $( event.target ).parents(".product-item-row");
			$( event.target ).attr("data-oldval", ui.item.label );
			$( event.target ).val( ui.item.label );
			$($targetparnt).find( ".hidden-item-product-id" ).val( ui.item.value);
			$($targetparnt).find( ".hidden-item-product-name" ).val( ui.item.name);
			if(ui.item.product_note != "" || default_product_note == "" ) { $($targetparnt).find( ".product_note" ).val( ui.item.product_note); }
			$($targetparnt).find( ".hidden-item-product-uom" ).val( ui.item.uom);
			$($targetparnt).find( ".uom" ).val( ui.item.uom);
					$($targetparnt).find(".uom").attr('disabled',true);
			$($targetparnt).find( ".hidden-item-product-is_transport" ).val( ui.item.is_transport);
			$($targetparnt).find(".quantity").attr('readonly',false);
			if(ui.item.is_transport == 1 || ui.item.is_transport == '1')
			{
				$($targetparnt).find(".quantity").val("1");
				$($targetparnt).find(".quantity").attr('readonly',true);
			}
			else if(ui.item.is_service_product == 1 || ui.item.is_service_product == '1')
			{
				
			}
			else
			{
				if(inventory_enable){
					if(ui.item.non_salable_product != 1 || ui.item.non_salable_product != '1'){
						$($targetparnt).find(".product-quantity-available").html(ui.item.items_available);
					}
					if(allow_oversell && (ui.item.non_salable_product != 1 || ui.item.non_salable_product != '1')){
						$($targetparnt).find(".quantity").attr("qtymax",ui.item.items_available);
					}
				}
			}
			
			$($targetparnt).find( ".hidden-item-product-cgst" ).val( ui.item.cgst);
			$($targetparnt).find( ".hidden-item-product-sgst" ).val( ui.item.sgst);
			$($targetparnt).find( ".hidden-item-product-igst" ).val( ui.item.igst).change();
			$($targetparnt).find( ".hidden-item-product-cess" ).val( ui.item.cess);
			$($targetparnt).find( ".hidden-item-product-cess-amount" ).val( ui.item.cess_amount);
			
			$($targetparnt).find(".hidden-item-product-att1-name").val(ui.item.attr1name);
			$($targetparnt).find(".hidden-item-product-att1-val").val(ui.item.attr1val);
			$($targetparnt).find(".hidden-item-product-att2-name").val(ui.item.attr2name);
			$($targetparnt).find(".hidden-item-product-att2-val").val(ui.item.attr2val);
			$($targetparnt).find(".hidden-item-product-att3-name").val(ui.item.attr3name);
			$($targetparnt).find(".hidden-item-product-att3-val").val(ui.item.attr3val);
			$($targetparnt).find(".hidden-item-product-att4-name").val(ui.item.attr4name);
			$($targetparnt).find(".hidden-item-product-att4-val").val(ui.item.attr4val);
			
			
			
			
			$($targetparnt).find(".hsccode").val(ui.item.hsn);
			if(ui.item.sellprice != ui.item.customerprice)
			{
				$($targetparnt).find(".rate").val(ui.item.customerprice);
				$($targetparnt).find(".customer_rate_label").html(ui.item.sellprice);
				
			}
			else
			{
				$($targetparnt).find(".rate").val(ui.item.sellprice);
				$($targetparnt).find(".customer_rate_label").html('');
			}
			if($($targetparnt).find(".quantity").val() == "")	
			{		
				$($targetparnt).find(".quantity").val("1");	
			}
			$($targetparnt).find(".cgst_select:not([disabled])").val(parseFloat(ui.item.cgst));
			$($targetparnt).find(".cgst:not([readonly])").val(parseFloat(ui.item.cgst));
			$($targetparnt).find(".sgst:not([readonly])").val(parseFloat(ui.item.sgst));
			$($targetparnt).find(".igst:not([readonly])").val(parseFloat(ui.item.igst));	
			$($targetparnt).find(".cess").val(ui.item.cess);
			$($targetparnt).find(".cess_amount").val(ui.item.cess_amount);
			UpdateCalculations();						
			return false;
		}, minLength:0
	}).focus(function(){            
            $(this).autocomplete("search");
    });
	var rowcounter = 1;
	var rowlength = $("#document-item-list .product-item-row").length;
	$("#document-item-list .product-item-row").each(function(){
		$(this).find(".product-item-row-number").html(rowcounter);
		if(rowlength == rowcounter)
		{
			$(this).find(".btnadd-row-item").show();
			$(this).find(".btnremove-row-item").hide();
		}
		else
		{
			$(this).find(".btnremove-row-item").show();
		}
		rowcounter += 1;
	});
	
	$( ".uom" ).autocomplete({
		source: autoUOMList,
		change: function(event, ui) {
			if (ui.item == null || ui.item == undefined) {
				var $targetparnt = $(this).parents(".product-item-row");
				$($targetparnt).find( ".hidden-item-product-uom" ).val("");			
				$($targetparnt).find( ".uom" ).val("");
			}
			else{
				if (ui.item) {
					var $targetparnt = $(this).parents(".product-item-row");
					$($targetparnt).find( ".uom" ).val( ui.item.value);			
					$($targetparnt).find( ".hidden-item-product-uom" ).val( ui.item.value);			
				}
			}
		},
		select: function( event, ui ) {
			var $targetparnt = $(this).parents(".product-item-row");
			$($targetparnt).find( ".uom" ).val( ui.item.value);			
			$($targetparnt).find( ".hidden-item-product-uom" ).val( ui.item.value);			
			return false;
		}, minLength:0
	}).focus(function(){            
            $(this).autocomplete("search");
    });
}

function addNewRowItem(ele){
	$(ele).parents('tr.product-item-row').after(rowdata);
	$(".currency-factor-symbol").html(cur_symbol[getCurrencyCodeFromName()]);
	UpdateTrigger();
}
function validateCurrentRows(){
	var isValid = true;
	if($("#document-item-list .product-item-row").length >= document_item_allowed)
	{
		alert('Maximum '+document_item_allowed+' Items can be added in invoice.');
		isValid = false;
	}
	$("#document-item-list .product-item-row").each(function(){
		var quantity = $(this).find(".quantity").val();
		var rate = $(this).find(".rate").val();
		var product = $(this).find(".hidden-item-product-name").val();
		var row_total = 0;
		if( product == "")
		{
			alert('Please Select Product.');
			$(this).find(".product-combobox").focus();
			isValid = false;
			return false;
		}
		if( quantity == "")
		{
			alert('Please enter Quantity.');
			$(this).find(".quantity").focus();
			isValid = false;
			return false;
		}
		if(  rate == "" )
		{
			alert('Please enter Price.');
			$(this).find(".rate").focus();
			isValid = false;
			return false;
		}
	});
	return isValid;
}
function validateCurrentRowsForSubmit(){
	var isValid = true;
	if($("#document-item-list .product-item-row").length >= 26 &&  false)
	{
		alert('Maximum '+document_item_allowed+' Items can be added in invoice.');
		isValid = false;
	}
	if($("#document-item-list .product-item-row").length>1)
	{
		var RowCounter = 1;
		var totalRowsData = $("#document-item-list .product-item-row").length;
		$("#document-item-list .product-item-row").each(function(){
			var quantity = $(this).find(".quantity").val();
			var rate = $(this).find(".rate").val();
			var product = $(this).find(".hidden-item-product-name").val();
			var row_total = 0;
			
			if(totalRowsData == RowCounter &&  product == "" &&  rate == "" &&  quantity == "")
			{
			
			}
			else
			{
				if( product == "")
				{
					alert('Please Select Product.');
					$(this).find(".product-combobox").focus();
					isValid = false;
					return false;
				}
				if( quantity == "")
				{
					alert('Please enter Quantity.');
					$(this).find(".quantity").focus();
					isValid = false;
					return false;
				}
				if(  rate == "" )
				{
					alert('Please enter Price.');
					$(this).find(".rate").focus();
					isValid = false;
					return false;
				}
			}
			
			RowCounter++;
		});
	}
	else
	{
		$("#document-item-list .product-item-row").each(function(){
			var quantity = $(this).find(".quantity").val();
			var rate = $(this).find(".rate").val();
			var product = $(this).find(".hidden-item-product-name").val();
			var row_total = 0;
			if( product == "")
			{
				alert('Please Select Product.');
				$(this).find(".product-combobox").focus();
				isValid = false;
				return false;
			}
			if( quantity == "")
			{
				alert('Please enter Quantity.');
				$(this).find(".quantity").focus();
				isValid = false;
				return false;
			}
			if(  rate == "" )
			{
				alert('Please enter Price.');
				$(this).find(".rate").focus();
				isValid = false;
				return false;
			}
		});
	}
	
	return isValid;
}
$(document).on("change", "#reverse_Charge", function(){
	UpdateCalculations();
});
$(document).on("change", "#payment", function(){
	SetPaymentModeDueDate();
});

function RemoveRowItem(row){
	$(row).parents(".product-item-row").remove();
	UpdateTrigger();
	UpdateCalculations();
}

$('#SameShippingAdd').change(function() {
    if($(this).is(":checked")) {
        $("#shipping_detail_drawer").removeClass("open_drwawer");
    }
	else
	{
		$("#shipping_detail_drawer").addClass("open_drwawer");
	}
	$(window).trigger("resize");
});


$('#hidden-invoice-country').change(function() {
	var sezcurrent = $(this).val();
    if(sezcurrent == "SEZInvoice" || sezcurrent == "SEZInvoiceWithoutIGST" || sezcurrent == "ExportInvoice" || sezcurrent == "ExportInvoiceWithoutIGST") {
        $(".sez-box").show();
    }
	else
	{
		$(".sez-box").hide();
	}
});
	
	var sezcurrent = $('#hidden-invoice-country').val();
    if(sezcurrent == "SEZInvoice" || sezcurrent == "SEZInvoiceWithoutIGST" || sezcurrent == "ExportInvoice" || sezcurrent == "ExportInvoiceWithoutIGST") {
        $(".sez-box").show();
    }
	else
	{
		$(".sez-box").hide();
	}

	
	
$('#currency').change(function() {
    $(".currency-factor-name").html(getCurrencyCodeFromName());
	$(".currency-factor-symbol").html(cur_symbol[getCurrencyCodeFromName()]);
	UpdateCalculations();
});
function UpdateCalculationsUSD(ele){
	
	if(ele.val().charAt(ele.val().length - 1) == ".")
	{
		return;
	}
	
	var currency_rate = $("#currency_rate").val();
	if(currency_rate == "")
	{
		currency_rate = 1;
	}
	else{
		currency_rate = parseFloat(currency_rate);
	}
	
	if($(ele).hasClass("rate_usd"))
	{
		var rate = Math.round(conver_amount_reverse_with_factor($(ele).val(),currency_rate ) * 100) / 100;	
		$(ele).parents("td").find(".rate").val(rate).trigger("change");
	}
	else{
		var line_total = Math.round(conver_amount_reverse_with_factor($(ele).val(),currency_rate ) * 100) / 100;	
		$(ele).parents("td").find(".line_total").val(line_total).trigger("blur");
	}
}
/* Validate single quantity field */
function qty_validate_item(item){
	var isValid = true;
	if(! allow_oversell){
		return true;
	}
	if (typeof item.attr('qtymax') !== 'undefined' && item.attr('qtymax') !== false) {
		if(parseInt(item.val()) != 0  && parseInt(item.val()) > parseInt(item.attr('qtymax'))){
			item.next().remove(".qerror");
			item.after("<span class='qerror'>Not enough stock!</span>");
			isValid = false;		
		}else{
			item.next().remove(".qerror");		
			isValid = true;
		}
	}	
	
	return isValid;
}

/* Validate all quantity fields on submit */
function qty_validate_items(){
	var isValid = true;
	if(! allow_oversell){
		return true;
	}
	$("input[name='quantity[]']").each(function() {
		qty_validate_item($(this));
		if(qty_validate_item($(this)) == false){
			isValid = false;			
		}
	});
	return isValid;
}

/* Quantity validation on quantity change */
$(document).on('keyup change', "input[name='quantity[]']",function () {
	qty_validate_item($(this));	
});

/* Switchers */
$('input[type=radio][name=disc-type]').change(function() {
    if (this.value == '1') {
		discount_in = 'rupee';		
	}
    else if (this.value == '0') {
		discount_in = 'percentage';
    }
	$('#discount_in').val(discount_in);
	UpdateCalculations();
});
$('input[type=radio][name=roundoff]').change(function() {
    if (this.value == '1') {
		enable_round_off = '1';		
	}
    else if (this.value == '0') {
		enable_round_off = '0';		
    }
	UpdateCalculations();
});
$(document).on('change', ".cgst_select",function () {		
	var $targetparnt = $(this).parents(".product-item-row");
	$($targetparnt).find(".cgst").val($(this).val());
	$($targetparnt).find(".sgst").val($(this).val());
	UpdateCalculations();
});