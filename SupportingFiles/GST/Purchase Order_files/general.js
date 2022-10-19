var availablePlaceofSupply = ['Andaman and Nicobar','Andhra Pradesh','Andhra Pradesh (New)','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadra & Nagar Haveli and Daman & Diu','Dadra and Nagar Haveli','Daman and Diu','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep Islands','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Orissa','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal'];
var cur_symbol= {};
cur_symbol['AED'] = 'AED';
cur_symbol['AFN'] = 'AFN';
cur_symbol['ALL'] = 'ALL';
cur_symbol['AMD'] = 'AMD';
cur_symbol['ANG'] = 'ANG';
cur_symbol['AOA'] = 'AOA';
cur_symbol['ARS'] = '$';
cur_symbol['AUD'] = '$';
cur_symbol['AWG'] = 'AWG';
cur_symbol['AZN'] = 'AZN';
cur_symbol['BAM'] = 'BAM';
cur_symbol['BBD'] = '$';
cur_symbol['BDT'] = 'BDT';
cur_symbol['BGN'] = 'BGN';
cur_symbol['BHD'] = 'BHD';
cur_symbol['BIF'] = 'BIF';
cur_symbol['BMD'] = '$';
cur_symbol['BND'] = '$';
cur_symbol['BOB'] = 'BOB';
cur_symbol['BRL'] = 'R$';
cur_symbol['BSD'] = '$';
cur_symbol['BTN'] = 'BTN';
cur_symbol['BWP'] = 'BWP';
cur_symbol['BYR'] = 'BYR';
cur_symbol['BZD'] = '$';
cur_symbol['CAD'] = '$';
cur_symbol['CDF'] = 'CDF';
cur_symbol['CHF'] = 'CHF';
cur_symbol['CLP'] = '$';
cur_symbol['CNY'] = '¥';
cur_symbol['COP'] = '$';
cur_symbol['CRC'] = 'CRC';
cur_symbol['CUP'] = '$';
cur_symbol['CVE'] = '$';
cur_symbol['CZK'] = 'CZK';
cur_symbol['DJF'] = 'DJF';
cur_symbol['DKK'] = 'DKK';
cur_symbol['DOP'] = '$';
cur_symbol['DZD'] = 'DZD';
cur_symbol['EGP'] = '£';
cur_symbol['ERN'] = 'ERN';
cur_symbol['ETB'] = 'ETB';
cur_symbol['EUR'] = '€';
cur_symbol['FJD'] = '$';
cur_symbol['FKP'] = '£';
cur_symbol['GBP'] = '£';
cur_symbol['GEL'] = 'GEL';
cur_symbol['GHS'] = 'GHS';
cur_symbol['GIP'] = '£';
cur_symbol['GMD'] = 'GMD';
cur_symbol['GNF'] = 'GNF';
cur_symbol['GTQ'] = 'GTQ';
cur_symbol['GYD'] = '$';
cur_symbol['HKD'] = '$';
cur_symbol['HNL'] = 'HNL';
cur_symbol['HRK'] = 'HRK';
cur_symbol['HTG'] = 'HTG';
cur_symbol['HUF'] = 'HUF';
cur_symbol['IDR'] = 'IDR';
cur_symbol['ILS'] = 'ILS';
cur_symbol['INR'] = '₹';
cur_symbol['IQD'] = 'IQD';
cur_symbol['IRR'] = 'IRR';
cur_symbol['ISK'] = 'ISK';
cur_symbol['JMD'] = 'JMD';
cur_symbol['JOD'] = 'JOD';
cur_symbol['JPY'] = 'JPY';
cur_symbol['KES'] = 'KES';
cur_symbol['KGS'] = 'KGS';
cur_symbol['KHR'] = 'KHR';
cur_symbol['KMF'] = 'KMF';
cur_symbol['KPW'] = 'KPW';
cur_symbol['KRW'] = 'KRW';
cur_symbol['KWD'] = 'KWD';
cur_symbol['KYD'] = '$';
cur_symbol['KZT'] = 'KZT';
cur_symbol['LAK'] = 'LAK';
cur_symbol['LBP'] = 'LBP';
cur_symbol['LKR'] = 'LKR';
cur_symbol['LRD'] = '$';
cur_symbol['LSL'] = 'LSL';
cur_symbol['LYD'] = 'LYD';
cur_symbol['MAD'] = 'MAD';
cur_symbol['MDL'] = 'MDL';
cur_symbol['MGA'] = 'MGA';
cur_symbol['MKD'] = 'MKD';
cur_symbol['MMK'] = 'MMK';
cur_symbol['MNT'] = 'MNT';
cur_symbol['MOP'] = 'MOP';
cur_symbol['MRO'] = 'MRO';
cur_symbol['MUR'] = 'MUR';
cur_symbol['MVR'] = 'MVR';
cur_symbol['MWK'] = 'MWK';
cur_symbol['MXN'] = '$';
cur_symbol['MYR'] = 'MYR';
cur_symbol['MZN'] = 'MZN';
cur_symbol['NAD'] = '$';
cur_symbol['NGN'] = 'NGN';
cur_symbol['NIO'] = 'NIO';
cur_symbol['NOK'] = 'NOK';
cur_symbol['NPR'] = 'NPR';
cur_symbol['NZD'] = '$';
cur_symbol['OMR'] = 'OMR';
cur_symbol['PAB'] = 'PAB';
cur_symbol['PEN'] = 'PEN';
cur_symbol['PGK'] = 'PGK';
cur_symbol['PHP'] = 'PHP';
cur_symbol['PKR'] = 'PKR';
cur_symbol['PLN'] = 'PLN';
cur_symbol['PYG'] = 'PYG';
cur_symbol['QAR'] = 'QAR';
cur_symbol['RUB'] = 'RUB';
cur_symbol['RWF'] = 'RWF';
cur_symbol['SAR'] = 'SAR';
cur_symbol['SBD'] = '$';
cur_symbol['SCR'] = 'SCR';
cur_symbol['SEK'] = 'SEK';
cur_symbol['SGD'] = '$';
cur_symbol['SHP'] = '£';
cur_symbol['SLL'] = 'SLL';
cur_symbol['SOS'] = 'SOS';
cur_symbol['SRD'] = '$';
cur_symbol['STD'] = 'STD';
cur_symbol['SVC'] = 'SVC';
cur_symbol['SYP'] = 'SYP';
cur_symbol['SZL'] = 'SZL';
cur_symbol['THB'] = 'THB';
cur_symbol['TJS'] = 'TJS';
cur_symbol['TND'] = 'TND';
cur_symbol['TOP'] = 'TOP';
cur_symbol['TRY'] = 'TRY';
cur_symbol['TTD'] = '$';
cur_symbol['TWD'] = '$';
cur_symbol['TZS'] = 'TZS';
cur_symbol['UAH'] = 'UAH';
cur_symbol['UGX'] = 'UGX';
cur_symbol['USD'] = '$';
cur_symbol['USN'] = '$';
cur_symbol['UYU'] = 'UYU';
cur_symbol['UZS'] = 'UZS';
cur_symbol['VEF'] = 'VEF';
cur_symbol['VND'] = 'VND';
cur_symbol['VUV'] = 'VUV';
cur_symbol['WST'] = 'WST';
cur_symbol['XAF'] = 'XAF';
cur_symbol['XCD'] = '$';
cur_symbol['XOF'] = 'XOF';
cur_symbol['XPF'] = 'XPF';
cur_symbol['YER'] = 'YER';
cur_symbol['ZAR'] = 'ZAR';
cur_symbol['ZMW'] = 'ZMW';
cur_symbol['ZWL'] = '$';

var cur_main= {};
cur_main['AED'] = "UAE DIRHAM";
cur_main['AFN'] = "AFGHANI";
cur_main['ALL'] = "LEK";
cur_main['AMD'] = "ARMENIAN DRAM";
cur_main['ANG'] = "NETHERLANDS ANTILLEAN GUILDER";
cur_main['AOA'] = "KWANZA";
cur_main['ARS'] = "ARGENTINE PESO";
cur_main['AUD'] = "AUSTRALIAN DOLLAR";
cur_main['AWG'] = "ARUBAN FLORIN";
cur_main['AZN'] = "AZERBAIJANIAN MANAT";
cur_main['BAM'] = "CONVERTIBLE MARK";
cur_main['BBD'] = "BARBADOS DOLLAR";
cur_main['BDT'] = "TAKA";
cur_main['BGN'] = "BULGARIAN LEV";
cur_main['BHD'] = "BAHRAINI DINAR";
cur_main['BIF'] = "BURUNDI FRANC";
cur_main['BMD'] = "BERMUDIAN DOLLAR";
cur_main['BND'] = "BRUNEI DOLLAR";
cur_main['BOB'] = "BOLIVIANO";
cur_main['BRL'] = "BRAZILIAN REAL";
cur_main['BSD'] = "BAHAMIAN DOLLAR";
cur_main['BTN'] = "NGULTRUM";
cur_main['BWP'] = "PULA";
cur_main['BYR'] = "BELARUSSIAN RUBLE";
cur_main['BZD'] = "BELIZE DOLLAR";
cur_main['CAD'] = "CANADIAN DOLLAR";
cur_main['CDF'] = "CONGOLESE FRANC";
cur_main['CHF'] = "SWISS FRANC";
cur_main['CLP'] = "CHILEAN PESO";
cur_main['CNY'] = "YUAN RENMINBI";
cur_main['COP'] = "COLOMBIAN PESO";
cur_main['CRC'] = "COSTA RICAN COLON";
cur_main['CUP'] = "CUBAN PESO";
cur_main['CVE'] = "CABO VERDE ESCUDO";
cur_main['CZK'] = "CZECH KORUNA";
cur_main['DJF'] = "DJIBOUTI FRANC";
cur_main['DKK'] = "DANISH KRONE";
cur_main['DOP'] = "DOMINICAN PESO";
cur_main['DZD'] = "ALGERIAN DINAR";
cur_main['EGP'] = "EGYPTIAN POUND";
cur_main['ERN'] = "NAKFA";
cur_main['ETB'] = "ETHIOPIAN BIRR";
cur_main['EUR'] = "EURO";
cur_main['FJD'] = "FIJI DOLLAR";
cur_main['FKP'] = "FALKLAND ISLANDS POUND";
cur_main['GBP'] = "POUND STERLING";
cur_main['GEL'] = "LARI";
cur_main['GHS'] = "GHANA CEDI";
cur_main['GIP'] = "GIBRALTAR POUND";
cur_main['GMD'] = "DALASI";
cur_main['GNF'] = "GUINEA FRANC";
cur_main['GTQ'] = "QUETZAL";
cur_main['GYD'] = "GUYANA DOLLAR";
cur_main['HKD'] = "HONG KONG DOLLAR";
cur_main['HNL'] = "LEMPIRA";
cur_main['HRK'] = "KUNA";
cur_main['HTG'] = "GOURDE";
cur_main['HUF'] = "FORINT";
cur_main['IDR'] = "RUPIAH";
cur_main['ILS'] = "NEW ISRAELI SHEQEL";
cur_main['INR'] = "INDIAN RUPEE";
cur_main['IQD'] = "IRAQI DINAR";
cur_main['IRR'] = "IRANIAN RIAL";
cur_main['ISK'] = "ICELAND KRONA";
cur_main['JMD'] = "JAMAICAN DOLLAR";
cur_main['JOD'] = "JORDANIAN DINAR";
cur_main['JPY'] = "YEN";
cur_main['KES'] = "KENYAN SHILLING";
cur_main['KGS'] = "SOM";
cur_main['KHR'] = "RIEL";
cur_main['KMF'] = "COMORO FRANC";
cur_main['KPW'] = "NORTH KOREAN WON";
cur_main['KRW'] = "WON";
cur_main['KWD'] = "KUWAITI DINAR";
cur_main['KYD'] = "CAYMAN ISLANDS DOLLAR";
cur_main['KZT'] = "TENGE";
cur_main['LAK'] = "KIP";
cur_main['LBP'] = "LEBANESE POUND";
cur_main['LKR'] = "SRI LANKA RUPEE";
cur_main['LRD'] = "LIBERIAN DOLLAR";
cur_main['LSL'] = "LOTI";
cur_main['LYD'] = "LIBYAN DINAR";
cur_main['MAD'] = "MOROCCAN DIRHAM";
cur_main['MDL'] = "MOLDOVAN LEU";
cur_main['MGA'] = "MALAGASY ARIARY";
cur_main['MKD'] = "DENAR";
cur_main['MMK'] = "KYAT";
cur_main['MNT'] = "TUGRIK";
cur_main['MOP'] = "PATACA";
cur_main['MRO'] = "OUGUIYA";
cur_main['MUR'] = "MAURITIUS RUPEE";
cur_main['MVR'] = "RUFIYAA";
cur_main['MWK'] = "KWACHA";
cur_main['MXN'] = "MEXICAN PESO";
cur_main['MYR'] = "MALAYSIAN RINGGIT";
cur_main['MZN'] = "MOZAMBIQUE METICAL";
cur_main['NAD'] = "NAMIBIA DOLLAR";
cur_main['NGN'] = "NAIRA";
cur_main['NIO'] = "CORDOBA ORO";
cur_main['NOK'] = "NORWEGIAN KRONE";
cur_main['NPR'] = "NEPALESE RUPEE";
cur_main['NZD'] = "NEW ZEALAND DOLLAR";
cur_main['OMR'] = "RIAL OMANI";
cur_main['PAB'] = "BALBOA";
cur_main['PEN'] = "NUEVO SOL";
cur_main['PGK'] = "KINA";
cur_main['PHP'] = "PHILIPPINE PESO";
cur_main['PKR'] = "PAKISTAN RUPEE";
cur_main['PLN'] = "ZLOTY";
cur_main['PYG'] = "GUARANI";
cur_main['QAR'] = "QATARI RIAL";
cur_main['RUB'] = "RUSSIAN RUBLE";
cur_main['RWF'] = "RWANDA FRANC";
cur_main['SAR'] = "SAUDI RIYAL";
cur_main['SBD'] = "SOLOMON ISLANDS DOLLAR";
cur_main['SCR'] = "SEYCHELLES RUPEE";
cur_main['SEK'] = "SWEDISH KRONA";
cur_main['SGD'] = "SINGAPORE DOLLAR";
cur_main['SHP'] = "SAINT HELENA POUND";
cur_main['SLL'] = "LEONE";
cur_main['SOS'] = "SOMALI SHILLING";
cur_main['SRD'] = "SURINAM DOLLAR";
cur_main['STD'] = "DOBRA";
cur_main['SVC'] = "EL SALVADOR COLON";
cur_main['SYP'] = "SYRIAN POUND";
cur_main['SZL'] = "LILANGENI";
cur_main['THB'] = "BAHT";
cur_main['TJS'] = "SOMONI";
cur_main['TND'] = "TUNISIAN DINAR";
cur_main['TOP'] = "PA’ANGA";
cur_main['TRY'] = "TURKISH LIRA";
cur_main['TTD'] = "TRINIDAD AND TOBAGO DOLLAR";
cur_main['TWD'] = "NEW TAIWAN DOLLAR";
cur_main['TZS'] = "TANZANIAN SHILLING";
cur_main['UAH'] = "HRYVNIA";
cur_main['UGX'] = "UGANDA SHILLING";
cur_main['USD'] = "US DOLLAR";
cur_main['USN'] = "US DOLLAR (NEXT DAY)";
cur_main['UYU'] = "PESO URUGUAYO";
cur_main['UZS'] = "UZBEKISTAN SUM";
cur_main['VEF'] = "BOLIVAR";
cur_main['VND'] = "DONG";
cur_main['VUV'] = "VATU";
cur_main['WST'] = "TALA";
cur_main['XAF'] = "CFA FRANC BEAC";
cur_main['XCD'] = "EAST CARIBBEAN DOLLAR";
cur_main['XOF'] = "CFA FRANC BCEAO";
cur_main['XPF'] = "CFP FRANC";
cur_main['YER'] = "YEMENI RIAL";
cur_main['ZAR'] = "RAND";
cur_main['ZMW'] = "ZAMBIAN KWACHA";
cur_main['ZWL'] = "ZIMBABWE DOLLAR";

var cur_decimal= {};
cur_decimal['AED'] = "FILS";
cur_decimal['AFN'] = "PUL";
cur_decimal['ALL'] = "QINDARKA";
cur_decimal['AMD'] = "LUMA";
cur_decimal['ANG'] = "CENT";
cur_decimal['AOA'] = "CENT";
cur_decimal['ARS'] = "CENTAVO";
cur_decimal['AUD'] = "CENT";
cur_decimal['AWG'] = "CENT";
cur_decimal['AZN'] = "GOPIKS";
cur_decimal['BAM'] = "FENING";
cur_decimal['BBD'] = "CENT";
cur_decimal['BDT'] = "PAISA";
cur_decimal['BGN'] = "STOTINKA";
cur_decimal['BHD'] = "FILS";
cur_decimal['BIF'] = "CENTIME";
cur_decimal['BMD'] = "CENT";
cur_decimal['BND'] = "CENT";
cur_decimal['BOB'] = "CENTAVO";
cur_decimal['BRL'] = "CENTAVO";
cur_decimal['BSD'] = "CENT";
cur_decimal['BTN'] = "CHETRUM";
cur_decimal['BWP'] = "CHETRUM";
cur_decimal['BYR'] = "KAPYEYKA";
cur_decimal['BZD'] = "CENT";
cur_decimal['CAD'] = "CENT";
cur_decimal['CDF'] = "CENTIME";
cur_decimal['CHF'] = "RAPPEN";
cur_decimal['CLP'] = "CENTAVO";
cur_decimal['CNY'] = "FEN";
cur_decimal['COP'] = "CENTAVO";
cur_decimal['CRC'] = "CENTIMO";
cur_decimal['CUP'] = "CENTAVO";
cur_decimal['CVE'] = "CENTAVO";
cur_decimal['CZK'] = "HALER";
cur_decimal['DJF'] = "CENTIME";
cur_decimal['DKK'] = "ORE";
cur_decimal['DOP'] = "CENTAVO";
cur_decimal['DZD'] = "SANTEEM";
cur_decimal['EGP'] = "PIASTRE";
cur_decimal['ERN'] = "CENT";
cur_decimal['ETB'] = "SANTIM";
cur_decimal['EUR'] = "CENT";
cur_decimal['FJD'] = "CENT";
cur_decimal['FKP'] = "PENNY";
cur_decimal['GBP'] = "PENNY";
cur_decimal['GEL'] = "TETRI";
cur_decimal['GHS'] = "PESEWA";
cur_decimal['GIP'] = "PENNY";
cur_decimal['GMD'] = "BUTUT";
cur_decimal['GNF'] = "CENTIME";
cur_decimal['GTQ'] = "CENTAVO";
cur_decimal['GYD'] = "CENT";
cur_decimal['HKD'] = "CENT";
cur_decimal['HNL'] = "CENTAVO";
cur_decimal['HRK'] = "LIPA";
cur_decimal['HTG'] = "CENTIME";
cur_decimal['HUF'] = "FILLER";
cur_decimal['IDR'] = "SEN";
cur_decimal['ILS'] = "AGORA";
cur_decimal['INR'] = "PAISA";
cur_decimal['IQD'] = "FILS";
cur_decimal['IRR'] = "DINAR";
cur_decimal['ISK'] = "EYRIR";
cur_decimal['JMD'] = "CENT";
cur_decimal['JOD'] = "PIASTRE";
cur_decimal['JPY'] = "SEN";
cur_decimal['KES'] = "CENT";
cur_decimal['KGS'] = "TYIYN";
cur_decimal['KHR'] = "SEN";
cur_decimal['KMF'] = "CENTIME";
cur_decimal['KPW'] = "CHON";
cur_decimal['KRW'] = "JEON";
cur_decimal['KWD'] = "FILS";
cur_decimal['KYD'] = "CENT";
cur_decimal['KZT'] = "TIIN";
cur_decimal['LAK'] = "ATT";
cur_decimal['LBP'] = "PIASTRE";
cur_decimal['LKR'] = "CENT";
cur_decimal['LRD'] = "CENT";
cur_decimal['LSL'] = "SENTE";
cur_decimal['LYD'] = "DIRHAM";
cur_decimal['MAD'] = "CENTIME";
cur_decimal['MDL'] = "BAN";
cur_decimal['MGA'] = "CENTIMES";
cur_decimal['MKD'] = "DENI";
cur_decimal['MMK'] = "PYA";
cur_decimal['MNT'] = "MONGO";
cur_decimal['MOP'] = "AVO";
cur_decimal['MRO'] = "KHOUMS";
cur_decimal['MUR'] = "CENT";
cur_decimal['MVR'] = "LAARI";
cur_decimal['MWK'] = "TAMBALA";
cur_decimal['MXN'] = "CENTAVO";
cur_decimal['MYR'] = "SEN";
cur_decimal['MZN'] = "CENTAVO";
cur_decimal['NAD'] = "CENT";
cur_decimal['NGN'] = "KOBO";
cur_decimal['NIO'] = "CENTAVO";
cur_decimal['NOK'] = "ORE";
cur_decimal['NPR'] = "PAISE";
cur_decimal['NZD'] = "CENT";
cur_decimal['OMR'] = "BAISA";
cur_decimal['PAB'] = "CENTESIMO";
cur_decimal['PEN'] = "CENTIMO";
cur_decimal['PGK'] = "TOEA";
cur_decimal['PHP'] = "CENTAVO";
cur_decimal['PKR'] = "PAISE";
cur_decimal['PLN'] = "GROSZ";
cur_decimal['PYG'] = "CENTIMO";
cur_decimal['QAR'] = "DIRHAM";
cur_decimal['RUB'] = "KOPEK";
cur_decimal['RWF'] = "CENTIME";
cur_decimal['SAR'] = "HALALA";
cur_decimal['SBD'] = "CENT";
cur_decimal['SCR'] = "CENT";
cur_decimal['SEK'] = "ORE";
cur_decimal['SGD'] = "CENT";
cur_decimal['SHP'] = "PENNY";
cur_decimal['SLL'] = "CENT";
cur_decimal['SOS'] = "CENT";
cur_decimal['SRD'] = "CENT";
cur_decimal['STD'] = "CENTIMO";
cur_decimal['SVC'] = "CENTAVO";
cur_decimal['SYP'] = "PIASTRE";
cur_decimal['SZL'] = "CENT";
cur_decimal['THB'] = "SATANG";
cur_decimal['TJS'] = "DIRAM";
cur_decimal['TND'] = "MILLIME";
cur_decimal['TOP'] = "SENITI";
cur_decimal['TRY'] = "KURUS";
cur_decimal['TTD'] = "CENT";
cur_decimal['TWD'] = "CENT";
cur_decimal['TZS'] = "CENT";
cur_decimal['UAH'] = "KOPIYKA";
cur_decimal['UGX'] = "CENT";
cur_decimal['USD'] = "CENT";
cur_decimal['USN'] = "CENT";
cur_decimal['UYU'] = "CENTESIMO";
cur_decimal['UZS'] = "TIYIN";
cur_decimal['VEF'] = "CENTIMO";
cur_decimal['VND'] = "HAO";
cur_decimal['VUV'] = "";
cur_decimal['WST'] = "SENE";
cur_decimal['XAF'] = "CENTIME";
cur_decimal['XCD'] = "CENT";
cur_decimal['XOF'] = "CENTIME";
cur_decimal['XPF'] = "CENTIME";
cur_decimal['YER'] = "FILS";
cur_decimal['ZAR'] = "CENT";
cur_decimal['ZMW'] = "NGWEE";
cur_decimal['ZWL'] = "CENT";


function number2text_with_currency(value,currency="INR") {
    var fraction = Math.round(frac(value) * 100);
    var f_text = "";
    if (fraction > 0) {
        f_text = "AND " + convert_number(fraction) + " "+ cur_decimal[currency];
    }
    return convert_number(value) + " "+cur_main[currency]+" " + f_text + " ONLY";
}


function number2text(value) {
    var fraction = Math.round(frac(value) * 100);
    var f_text = "";
    if (fraction > 0) {
        f_text = "AND " + convert_number(fraction) + " PAISA";
    }
    return convert_number(value) + " RUPEES " + f_text + " ONLY";
}

function frac(f) {
    return (f % Math.floor(f));
}

function convert_number(number) {
    if ((number < 0) || (number > 999999999)) {
        return "NUMBER OUT OF RANGE!";
    }
    var Gn = Math.floor(number / 10000000); /* Crore */
    number -= Gn * 10000000;
    var kn = Math.floor(number / 100000); /* lakhs */
    number -= kn * 100000;
    var Hn = Math.floor(number / 1000); /* thousand */
    number -= Hn * 1000;
    var Dn = Math.floor(number / 100); /* Tens (deca) */
    number = number % 100; /* Ones */
    var tn = Math.floor(number / 10);
    var one = Math.floor(number % 10);
    var res = "";
    if (Gn > 0) {
        res += (convert_number(Gn) + " CRORE");
    }
    if (kn > 0) {
        res += (((res == "") ? "" : " ") + convert_number(kn) + " LAKH");
    }
    if (Hn > 0) {
        res += (((res == "") ? "" : " ") + convert_number(Hn) + " THOUSAND");
    }
    if (Dn) {
        res += (((res == "") ? "" : " ") + convert_number(Dn) + " HUNDRED");
    }
    var ones = Array("", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "ELEVEN", "TWELVE", "THIRTEEN", "FOURTEEN", "FIFTEEN", "SIXTEEN", "SEVENTEEN", "EIGHTEEN", "NINETEEN");
    var tens = Array("", "", "TWENTY", "THIRTY", "FORTY", "FIFTY", "SIXTY", "SEVENTY", "EIGHTY", "NINETY");
    if (tn > 0 || one > 0) {
        if (!(res == "")) {
            res += " AND ";
        }
        if (tn < 2) {
            res += ones[tn * 10 + one];
        } else {
            res += tens[tn];
            if (one > 0) {
                res += ("-" + ones[one]);
            }
        }
    }
    if (res == "") {
        res = "ZERO";
    }
    return res;
}

function conver_amount_with_factor(amount,factor)
{
	return Math.round((amount/factor)*100)/100;
}
function conver_amount_reverse_with_factor(amount,factor)
{
	return amount*factor;
}

function getCurrencyCodeFromName()
{
	var currencyname = $(".currency").val().substring(0,($(".currency").val().indexOf('-'))).trim();
	if(currencyname == "")
	{
		currencyname = "INR";
	}
	return currencyname;
}
function allowOnlyNumber(evt){

	try {

		var charCode = (evt.which) ? evt.which : event.keyCode

		if ((charCode != 46 || $(this).val().indexOf('.') != -1) && (charCode < 48 || charCode > 57)&&charCode!=8&&charCode!=45) {

			alert("Only Numeric Input Is Allowed");

			return false;

		} 

		else{

			return true;

		}

	}

	catch(err){

	}
}

function selectall()
{
	
	if(document.tabledata.del.checked==true)
	{
		var chks = document.getElementsByName('delall[]');
		
		for(i=0;i<chks.length;i++)
		{
			chks[i].checked=true;
		}
	}
	else if(document.tabledata.del.checked==false)
	{
		var chks = document.getElementsByName('delall[]');
		
		for(i=0;i<chks.length;i++)
		{
			chks[i].checked=false;
		}
	}
}


function IsNumber(a)
{
	var reg = /^\d+$/;
	if(reg.test(a))
	{
	return true;
	}
	else{return false;}
}


var handles = ["Select State","Andaman and Nicobar","Andhra Pradesh","Andhra Pradesh (New)","Arunachal Pradesh","Assam","Bihar","Chandigarh","Chhattisgarh","Dadra & Nagar Haveli and Daman & Diu", "Dadra and Nagar Haveli","Daman and Diu","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Ladakh","Lakshadweep Islands","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Orissa","Puducherry","Punjab", "Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal"];
var handlesCodes = [""," ( 35 )"," ( 28 )"," ( 37 )"," ( 12 )"," ( 18 )"," ( 10 )"," ( 04 )"," ( 22 )"," ( 26 )"," ( 26 )"," ( 25 )"," ( 07 )"," ( 30 )"," ( 24 )"," ( 06 )"," ( 02 )"," ( 01 )"," ( 20 )"," ( 29 )"," ( 32 )"," ( 38 )"," ( 31 )"," ( 23 )"," ( 27 )"," ( 14 )"," ( 17 )"," ( 15 )"," ( 13 )"," ( 21 )"," ( 34 )"," ( 03 )"," ( 08 )"," ( 11 )"," ( 33 )"," ( 36 )"," ( 16 )"," ( 09 )"," ( 05 )"," ( 19 )"];

$(function() {
  var options = '';
  for (var i = 0; i < handles.length; i++) {  
	if(handles[i] == "Select State")  {	
		options += '<option value="">' + handles[i] + '</option>';  
	}  
	else  
	{	
		if(handles[i] == "Dadra and Nagar Haveli" || handles[i] == "Daman and Diu" )
		{
			options += '<option value="' + handles[i] + '">' + handles[i] +handlesCodes[i]+ '**</option>';  
		}
		else
		{
			options += '<option value="' + handles[i] + '">' + handles[i] +handlesCodes[i]+ '</option>';  
		}
		
	}
  }
  $('#listBox').html(options);
try {
	$('#listBox1').html(options);
	/* Edit Time Set State Selected Code */
	if($('#listBox1[data-value]').length>0)
	{
		if($('#listBox1').attr("data-value") != "")
		{
			$('#listBox1').val($('#listBox1').attr("data-value"));
		}
		
	}
	
	$('.all_state_list').html(options);	
	$(".all_state_list").each(function() {		
		if($(this).attr('data-value').length>0)
		{
			if($(this).attr("data-value") != "")
			{				
				$(this).val($(this).attr("data-value"));
			}
			
		}
		
	});
	
}
catch(err) {

}

try {
	var optionsNew = options.replace("Select State","Select Place of Supply");
	$('#PlaceofSupply').html(optionsNew);
	if($('#PlaceofSupply[data-value]').length>0)
	{
		if($('#PlaceofSupply').attr("data-value") != "")
		{
			$('#PlaceofSupply').val($('#PlaceofSupply').attr("data-value"));
			
		}
		
	}
}
catch(err) {

}

try {
	$('#listBox2').html(options);
	/* Edit Time Set State Selected Code */
	if($('#listBox2[data-value]').length>0)
	{
		if($('#listBox2').attr("data-value") != "")
		{
			$('#listBox2').val($('#listBox2').attr("data-value"));
			
		}
		
	}
}
catch(err) {

}

  
  
  
	/* Edit Time Set State Selected Code */
	if($('#listBox[data-value]').length>0)
	{
		if($('#listBox').attr("data-value") != "")
		{
			$('#listBox').val($('#listBox').attr("data-value"));
			
		}
		
	}
	
	
	/* Edit Time Set City Selected Code */
	if($('#secondlist[data-value]').length>0)
	{
		if($('#secondlist').attr("data-value") != "")
		{
			setTimeout(function(){
				$('#secondlist').val($('#secondlist').attr("data-value"));
			},100);
		}
	}
  
});


var handlescon = ["Select Country","Afghanistan","Albania","Algeria","Andorra","Angola","Antigua and Barbuda","Argentina","Armenia","Australia","Austria","Azerbaijan","Bahamas","Bahrain","Bangladesh","Barbados","Belarus","Belgium","Belize","Benin","Bhtan","Bolivia","Bosnia and Herzegovina","Botswana","Brazil","Brunei","Bulgaria","Burkina Faso","Burundi","Cabo Verde","Cambodia","Cameroon","Canada","Central African Republic (CAR)","Chad","Chile","China","Colombia","Comoros","Democratic Republic of the Congo","Republic of the Congo","Costa Rica","Cote d'Ivoire","Croatia","Cuba","Cyprus","Czech Republic","Denmark","Djibouti","Dominica","DominicanRepublic","Ecuador","Egypt","El Salvador","Equatorial Guinea","Eritrea","Estonia","Ethiopia","Fiji","Finland","France","Gabon","Gambia","Georgia","Germany","Ghana","Greece","Grenada","Guatemala","Guinea","uinea-Bissau","Guyana","Haiti","Honduras","Hong Kong","Hungary","Iceland","India","Indonesia","Iran","Iraq","Ireland","Isle of Man","Israel","Italy","Jamaica","Japan","Jordan","Kazakhstan","Kenya","Kiribati","Kosovo","Kuwait","Kyrgyzstan","Laos","Latvia","Lebanon","Lesotho","Liberia","Libya","Liechtenstein","Lithuania","Luxemborg","Macedonia (FYROM)","Madagascar","Malawi","Malaysia","Maldives","Mali","Malta","Marshall Islands","Mauritania","Mauritius","Mexico","Micronesia","Moldova","Monaco","Mongolia","Montenegro","Morocco","Mozambique","Myanmar (Burma)","Namibia","Nauru","Nepal","Netherlands","New Zealand","Nicaragua","Niger","Nigeria","North Korea","Norway","Oman","Pakistan","Palau","Palestine","Panama","Papua New Guinea","Paraguay","Peru","Philippines","Poland","Portugal","Qatar","Reunion","Romania","Russia","Rwanda","Saint Kitts and Nevis","Saint Lucia","Saint Vincentand the Grenadines","Samoa","San Marino","Sao Tome and Principe","Saudi Arabia","Senegal","Serbia","Seychelles","Sierra Leone","Singapore","Slovakia","Slovenia","Solomon Islands","Somalia","South Africa","South Korea","South Sudan","Spain","Sri Lanka","Sudan","Suriname","Swaziland","Sweden","Switzerland","Syria","Taiwan","Tajikistan","Tanzania","Thailand","Timor-Leste","Togo","Tonga","Trinidadad Tobago","Tunisia","Turkey","Turkmenistan","Tuvalu","Uganda","Ukraine","United Arab Emirates (UAE)","United Kingdom (UK)","United States of America (USA)","Uruguay","Uzbekistan","Vanuatu","Vatican City (Holy See)","Venezuela","Vietnam","Yemen","Zambia","Zimbabwe"];

$(function() {
	var options = '';	
	for (var i = 0; i < handlescon.length; i++) {  
		if(handlescon[i] == "Select State" || handlescon[i] == "Select Country")  {	options += '<option value="">' + handlescon[i] + '</option>';  }  else  {	options += '<option value="' + handlescon[i] + '">' + handlescon[i] + '</option>';  }
	}
	$('#listBoxCountry').html(options);
	
  
	/* Edit Time Set State Selected Code */
	if($('#listBoxCountry[data-value]').length>0)
	{
		if($('#listBoxCountry').attr("data-value") != "")
		{
			$('#listBoxCountry').val($('#listBoxCountry').attr("data-value"));
			
		}
		
	}
	
	
	
	try {
		$('#country_of_origin').html(options);
		/* Edit Time Set State Selected Code */
		if($('#country_of_origin[data-value]').length>0)
		{
			if($('#country_of_origin').attr("data-value") != "")
			{
				$('#country_of_origin').val($('#country_of_origin').attr("data-value"));
			}
			
		}
	}
	catch(err) {
	
	}
	try {
		$('#country_of_final').html(options);
		/* Edit Time Set State Selected Code */
		if($('#country_of_final[data-value]').length>0)
		{
			if($('#country_of_final').attr("data-value") != "")
			{
				$('#country_of_final').val($('#country_of_final').attr("data-value"));
			}
			
		}
	}
	catch(err) {
	
	}
	try {
		$('#listBoxCountry1').html(options);
		/* Edit Time Set State Selected Code */
		if($('#listBoxCountry1[data-value]').length>0)
		{
			if($('#listBoxCountry1').attr("data-value") != "")
			{
				$('#listBoxCountry1').val($('#listBoxCountry1').attr("data-value"));
			}
			
		}			
		$('.listBoxCountry1').html(options);		
		$(".listBoxCountry1").each(function() {
			if($(this).attr('data-value').length>0)
			{
				if($(this).attr("data-value") != "")
				{
					$(this).val($(this).attr("data-value"));
				}
				
			}
		});
	}
	catch(err) {
	
	}
	try {
		$('#listBoxCountry2').html(options);
		/* Edit Time Set State Selected Code */
		if($('#listBoxCountry2[data-value]').length>0)
		{
			if($('#listBoxCountry2').attr("data-value") != "")
			{
				$('#listBoxCountry2').val($('#listBoxCountry2').attr("data-value"));
			}
			
		}
	}
	catch(err) {
	
	}
	
});

function selct_country($val)
{
	if($val == 'India') {
		$('#listBox').show(); 
		$('#newState').hide();
		$('#listBox').attr("name","state"); 
		$('#newState').attr("name","statex"); 
	}
	else{
		$('#listBox').hide(); 
		$('#newState').show();
		$('#listBox').attr("name","statex"); 
		$('#newState').attr("name","state"); 
	}
}

function selct_state_option($val,dropdown,input,name)
{
	if($val == 'India') {
		$('#'+dropdown).show(); 
		$('#'+input).hide();
		$('#'+dropdown).attr("name",name+""); 
		$('#'+input).attr("name",name+"x"); 
	}
	else{
		$('#'+dropdown).hide(); 
		$('#'+input).show();
		$('#'+dropdown).attr("name",name+"x"); 
		$('#'+input).attr("name",name+""); 
	}
}

function selct_district($val)
{
    if($val=='Select State') {
	var andhra = ["Select City"];
   $(function() {
  var options = '';
  for (var i = 0; i < andhra.length; i++) {
      options += '<option value="' + andhra[i] + '">' + andhra[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  
  }
 if($val=='Andhra Pradesh') {
   var andhra = ["Anantapur","Chittoor","East Godavari","Guntur","Krishna","Kurnool","Prakasam","Srikakulam","SriPotti Sri Ramulu Nellore",
                                    "Vishakhapatnam","Vizianagaram","West Godavari","Cudappah"];
   $(function() {
  var options = '';
  for (var i = 0; i < andhra.length; i++) {
      options += '<option value="' + andhra[i] + '">' + andhra[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Arunachal Pradesh') {
    var ap = ["Anjaw","Changlang","Dibang Valley","East Siang","East Kameng","Kurung Kumey","Lohit","Longding","Lower Dibang Valley","Lower Subansiri","Papum Pare",
                                        "Tawang","Tirap","Upper Siang","Upper Subansiri","West Kameng","West Siang"];
   $(function() {
  var options = '';
  for (var i = 0; i < ap.length; i++) {
      options += '<option value="' + ap[i] + '">' + ap[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Assam') {
    var assam = ["Baksa","Barpeta","Bongaigaon","Cachar","Chirang","Darrang","Dhemaji","Dima Hasao","Dhubri","Dibrugarh","Goalpara","Golaghat","Hailakandi","Jorhat",
                                     "Kamrup","Kamrup Metropolitan","Karbi Anglong","Karimganj","Kokrajhar","Lakhimpur","Morigaon","Nagaon","Nalbari","Sivasagar","Sonitpur","Tinsukia","Udalguri"];
   $(function() {
  var options = '';
  for (var i = 0; i < assam.length; i++) {
      options += '<option value="' + assam[i] + '">' + assam[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Bihar') {
    var bihar = ["Araria","Arwal","Aurangabad","Banka","Begusarai","Bhagalpur","Bhojpur","Buxar","Darbhanga","East Champaran","Gaya","Gopalganj","Jamui","Jehanabad","Kaimur",
                                        "Katihar","Khagaria","Kishanganj","Lakhisarai","Madhepura","Madhubani","Munger","Muzaffarpur","Nalanda","Nawada","Patna","Purnia","Rohtas","Saharsa",
                                        "Samastipur","Saran","Sheikhpura","Sheohar","Sitamarhi","Siwan","Supaul","Vaishali","West Champaran"];
   $(function() {
  var options = '';
  for (var i = 0; i < bihar.length; i++) {
      options += '<option value="' + bihar[i] + '">' + bihar[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Chhattisgarh') {
    var Chhattisgarh = ["Bastar","Bijapur","Bilaspur","Dantewada","Dhamtari","Durg","Jashpur","Janjgir-Champa","Korba","Koriya","Kanker","Kabirdham (formerly Kawardha)","Mahasamund",
                                            "Narayanpur","Raigarh","Rajnandgaon","Raipur","Surajpur","Surguja"];
   $(function() {
  var options = '';
  for (var i = 0; i < Chhattisgarh.length; i++) {
      options += '<option value="' + Chhattisgarh[i] + '">' + Chhattisgarh[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Dadra and Nagar Haveli') {
    var dadra = ["Amal","Silvassa"];
   $(function() {
  var options = '';
  for (var i = 0; i < dadra.length; i++) {
      options += '<option value="' + dadra[i] + '">' + dadra[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Daman and Diu') {
    var daman = ["Daman","Diu"];
   $(function() {
  var options = '';
  for (var i = 0; i < daman.length; i++) {
      options += '<option value="' + daman[i] + '">' + daman[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Delhi') {
    var delhi = ["Delhi","New Delhi","North Delhi","Noida","Patparganj","Sonabarsa","Tughlakabad"];
   $(function() {
  var options = '';
  for (var i = 0; i < delhi.length; i++) {
      options += '<option value="' + delhi[i] + '">' + delhi[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Goa') {
    var goa = ["Chapora","Dabolim","Madgaon","Marmugao (Marmagao)","Panaji Port","Panjim","Pellet Plant Jetty/Shiroda","Talpona","Vasco da Gama"];
   $(function() {
  var options = '';
  for (var i = 0; i < goa.length; i++) {
      options += '<option value="' + goa[i] + '">' + goa[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Gujarat') {
    var gujarat = ["Ahmedabad","Amreli district","Anand","Aravalli","Banaskantha","Bharuch","Bhavnagar","Dahod","Dang","Gandhinagar","Jamnagar","Junagadh",
                                        "Kutch","Kheda","Mehsana","Narmada","Navsari","Patan","Panchmahal","Porbandar","Rajkot","Sabarkantha","Surendranagar","Surat","Tapi","Vadodara","Valsad"];
   $(function() {
  var options = '';
  for (var i = 0; i < gujarat.length; i++) {
      options += '<option value="' + gujarat[i] + '">' + gujarat[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Haryana') {
    var haryana = ["Ambala","Bhiwani","Faridabad","Fatehabad","Gurgaon","Hissar","Jhajjar","Jind","Karnal","Kaithal",
                                            "Kurukshetra","Mahendragarh","Mewat","Palwal","Panchkula","Panipat","Rewari","Rohtak","Sirsa","Sonipat","Yamuna Nagar"];
   $(function() {
  var options = '';
  for (var i = 0; i < haryana.length; i++) {
      options += '<option value="' + haryana[i] + '">' + haryana[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  
  if ($val=='Himachal Pradesh') {
    var himachal = ["Baddi","Baitalpur","Chamba","Dharamsala","Hamirpur","Kangra","Kinnaur","Kullu","Lahaul & Spiti","Mandi","Simla","Sirmaur","Solan","Una"];
   $(function() {
  var options = '';
  for (var i = 0; i < himachal.length; i++) {
      options += '<option value="' + himachal[i] + '">' + himachal[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Jammu and Kashmir') {
    var jammu = ["Jammu","Leh","Rajouri","Srinagar"];
   $(function() {
  var options = '';
  for (var i = 0; i < jammu.length; i++) {
      options += '<option value="' + jammu[i] + '">' + jammu[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Jharkhand') {
    var jharkhand = ["Bokaro","Chatra","Deoghar","Dhanbad","Dumka","East Singhbhum","Garhwa","Giridih","Godda","Gumla","Hazaribag","Jamtara","Khunti","Koderma","Latehar","Lohardaga","Pakur","Palamu",
                                            "Ramgarh","Ranchi","Sahibganj","Seraikela Kharsawan","Simdega","West Singhbhum"];
   $(function() {
  var options = '';
  for (var i = 0; i < jharkhand.length; i++) {
      options += '<option value="' + jharkhand[i] + '">' + jharkhand[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Karnataka') {
    var karnataka = ["Bagalkot","Bangalore","Bangalore Urban","Belgaum","Bellary","Bidar","Bijapur","Chamarajnagar", "Chikkamagaluru","Chikkaballapur",
                                           "Chitradurga","Davanagere","Dharwad","Dakshina Kannada","Gadag","Gulbarga","Hassan","Haveri district","Kodagu",
                                           "Kolar","Koppal","Mandya","Mysore","Raichur","Shimoga","Tumkur","Udupi","Uttara Kannada","Ramanagara","Yadgir"];
   $(function() {
  var options = '';
  for (var i = 0; i < karnataka.length; i++) {
      options += '<option value="' + karnataka[i] + '">' + karnataka[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Kerala') {
    var kerala = ["Alappuzha","Ernakulam","Idukki","Kannur","Kasaragod","Kollam","Kottayam","Kozhikode","Malappuram","Palakkad","Pathanamthitta","Thrissur","Thiruvananthapuram","Wayanad"];
   $(function() {
  var options = '';
  for (var i = 0; i < kerala.length; i++) {
      options += '<option value="' + kerala[i] + '">' + kerala[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Madhya Pradesh') {
    var mp = ["Alirajpur","Anuppur","Ashoknagar","Balaghat","Barwani","Betul","Bhilai","Bhind","Bhopal","Burhanpur","Chhatarpur","Chhindwara","Damoh","Dewas","Dhar","Guna","Gwalior","Hoshangabad",
                                    "Indore","Itarsi","Jabalpur","Khajuraho","Khandwa","Khargone","Malanpur","Malanpuri (Gwalior)","Mandla","Mandsaur","Morena","Narsinghpur","Neemuch","Panna","Pithampur","Raipur","Raisen","Ratlam",
                                    "Rewa","Sagar","Satna","Sehore","Seoni","Shahdol","Singrauli","Ujjain"];
   $(function() {
  var options = '';
  for (var i = 0; i < mp.length; i++) {
      options += '<option value="' + mp[i] + '">' + mp[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Maharashtra') {
    var maharashtra = ["Ahmednagar","Akola","Alibag","Amaravati","Arnala","Aurangabad","Aurangabad","Bandra","Bassain","Belapur","Bhiwandi","Bhusaval","Borliai-Mandla","Chandrapur","Dahanu","Daulatabad","Dighi (Pune)","Dombivali","Goa","Jaitapur","Jalgaon",
                                             "Jawaharlal Nehru (Nhava Sheva)","Kalyan","Karanja","Kelwa","Khopoli","Kolhapur","Lonavale","Malegaon","Malwan","Manori",
                                             "Mira Bhayandar","Miraj","Mumbai (ex Bombay)","Murad","Nagapur","Nagpur","Nalasopara","Nanded","Nandgaon","Nasik","Navi Mumbai","Nhave","Osmanabad","Palghar",
                                             "Panvel","Pimpri","Pune","Ratnagiri","Sholapur","Shrirampur","Shriwardhan","Tarapur","Thana","Thane","Trombay","Varsova","Vengurla","Virar","Wada"];
   $(function() {
  var options = '';
  for (var i = 0; i < maharashtra.length; i++) {
      options += '<option value="' + maharashtra[i] + '">' + maharashtra[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
   if ($val=='Manipur') {
    var manipur = ["Bishnupur","Churachandpur","Chandel","Imphal East","Senapati","Tamenglong","Thoubal","Ukhrul","Imphal West"];
   $(function() {
  var options = '';
  for (var i = 0; i < manipur.length; i++) {
      options += '<option value="' + manipur[i] + '">' + manipur[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
   if ($val=='Meghalaya') {
    var meghalaya = ["Baghamara","Balet","Barsora","Bolanganj","Dalu","Dawki","Ghasuapara","Mahendraganj","Moreh","Ryngku","Shella Bazar","Shillong"];
   $(function() {
  var options = '';
  for (var i = 0; i < meghalaya.length; i++) {
      options += '<option value="' + meghalaya[i] + '">' + meghalaya[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
   if ($val=='Mizoram') {
    var mizoram = ["Aizawl","Champhai","Kolasib","Lawngtlai","Lunglei","Mamit","Saiha","Serchhip"];
   $(function() {
  var options = '';
  for (var i = 0; i < mizoram.length; i++) {
      options += '<option value="' + mizoram[i] + '">' + mizoram[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
   if ($val=='Nagaland') {
    var nagaland = ["Dimapur","Kiphire","Kohima","Longleng","Mokokchung","Mon","Peren","Phek","Tuensang","Wokha","Zunheboto"];
   $(function() {
  var options = '';
  for (var i = 0; i < nagaland.length; i++) {
      options += '<option value="' + nagaland[i] + '">' + nagaland[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Orissa') {
    var orissa = ["Bahabal Pur","Bhubaneswar","Chandbali","Gopalpur","Jeypore","Paradip Garh","Puri","Rourkela"];
   $(function() {
  var options = '';
  for (var i = 0; i < orissa.length; i++) {
      options += '<option value="' + orissa[i] + '">' + orissa[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Puducherry') {
    var puducherry = ["Karaikal","Mahe","Pondicherry","Yanam"];
   $(function() {
  var options = '';
  for (var i = 0; i < puducherry.length; i++) {
      options += '<option value="' + puducherry[i] + '">' + puducherry[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Punjab') {
    var punjab = ["Amritsar","Barnala","Bathinda","Firozpur","Faridkot","Fatehgarh Sahib","Fazilka","Gurdaspur","Hoshiarpur","Jalandhar","Kapurthala","Ludhiana","Mansa","Moga","Sri Muktsar Sahib","Pathankot",
                                        "Patiala","Rupnagar","Ajitgarh (Mohali)","Sangrur","Shahid Bhagat Singh Nagar","Tarn Taran"];
   $(function() {
  var options = '';
  for (var i = 0; i < punjab.length; i++) {
      options += '<option value="' + punjab[i] + '">' + punjab[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Rajasthan') {
    var rajasthan = ["Ajmer","Banswara","Barmer","Barmer Rail Station","Basni","Beawar","Bharatpur","Bhilwara","Bhiwadi","Bikaner","Bongaigaon","Boranada, Jodhpur","Chittaurgarh","Fazilka","Ganganagar","Jaipur","Jaipur-Kanakpura",
                                       "Jaipur-Sitapura","Jaisalmer","Jodhpur","Jodhpur-Bhagat Ki Kothi","Jodhpur-Thar","Kardhan","Kota","Munabao Rail Station","Nagaur","Rajsamand","Sawaimadhopur","Shahdol","Shimoga","Tonk","Udaipur"];
   $(function() {
  var options = '';
  for (var i = 0; i < rajasthan.length; i++) {
      options += '<option value="' + rajasthan[i] + '">' + rajasthan[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  if ($val=='Sikkim') {
    var sikkim = ["Chamurci","Gangtok"];
   $(function() {
  var options = '';
  for (var i = 0; i < sikkim.length; i++) {
      options += '<option value="' + sikkim[i] + '">' + sikkim[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  
  if ($val=='Tamil Nadu') {
    var tn = ["Ariyalur","Chennai","Coimbatore","Cuddalore","Dharmapuri","Dindigul","Erode","Kanchipuram","Kanyakumari","Karur","Krishnagiri","Madurai","Mandapam","Nagapattinam","Nilgiris","Namakkal","Perambalur","Pudukkottai","Ramanathapuram","Salem","Sivaganga","Thanjavur","Thiruvallur","Tirupur",
                                   "Tiruchirapalli","Theni","Tirunelveli","Thanjavur","Thoothukudi","Tiruvallur","Tiruvannamalai","Vellore","Villupuram","Viruthunagar"];
   $(function() {
  var options = '';
  for (var i = 0; i < tn.length; i++) {
      options += '<option value="' + tn[i] + '">' + tn[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  
  if ($val=='Telangana') {
    var telangana = ["Adilabad","Hyderabad","Karimnagar","Mahbubnagar","Medak","Nalgonda","Nizamabad","Ranga Reddy","Warangal"];
   $(function() {
  var options = '';
  for (var i = 0; i < telangana.length; i++) {
      options += '<option value="' + telangana[i] + '">' + telangana[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  
  if ($val=='Tripura') {
    var tripura = ["Agartala","Dhalaighat","Kailashahar","Kamalpur","Kanchanpur","Kel Sahar Subdivision","Khowai","Khowaighat","Mahurighat","Old Raghna Bazar","Sabroom","Srimantapur"];
   $(function() {
  var options = '';
  for (var i = 0; i < tripura.length; i++) {
      options += '<option value="' + tripura[i] + '">' + tripura[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  
  if ($val=='Uttar Pradesh') {
    var up = ["Agra","Allahabad","Auraiya","Banbasa","Bareilly","Berhni","Bhadohi","Dadri","Dharchula","Gandhar","Gauriphanta","Ghaziabad","Gorakhpur","Gunji",
                                    "Jarwa","Jhulaghat (Pithoragarh)","Kanpur","Katarniyaghat","Khunwa","Loni","Lucknow","Meerut","Moradabad","Muzaffarnagar","Nepalgunj Road","Pakwara (Moradabad)",
                                    "Pantnagar","Saharanpur","Sonauli","Surajpur","Tikonia","Varanasi"];
   $(function() {
  var options = '';
  for (var i = 0; i < up.length; i++) {
      options += '<option value="' + up[i] + '">' + up[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  
  if ($val=='Uttarakhand') {
    var uttarakhand = ["Almora","Badrinath","Bangla","Barkot","Bazpur","Chamoli","Chopra","Dehra Dun","Dwarahat","Garhwal","Haldwani","Hardwar","Haridwar","Jamal","Jwalapur","Kalsi","Kashipur","Mall",
                                           "Mussoorie","Nahar","Naini","Pantnagar","Pauri","Pithoragarh","Rameshwar","Rishikesh","Rohni","Roorkee","Sama","Saur"];
   $(function() {
  var options = '';
  for (var i = 0; i < uttarakhand.length; i++) {
      options += '<option value="' + uttarakhand[i] + '">' + uttarakhand[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
  
  if ($val=='West Bengal') {
    var wb = ["Alipurduar","Bankura","Bardhaman","Birbhum","Cooch Behar","Dakshin Dinajpur","Darjeeling","Hooghly","Howrah",
                                    "Jalpaiguri","Kolkata","Maldah","Murshidabad","Nadia","North 24 Parganas","Paschim Medinipur","Purba Medinipur","Purulia","South 24 Parganas","Uttar Dinajpur"];
   $(function() {
  var options = '';
  for (var i = 0; i < wb.length; i++) {
      options += '<option value="' + wb[i] + '">' + wb[i] + '</option>';
  }
  $('#secondlist').html(options);
  });
  }
  
}
$(function(){
	 
    $('.select2-dropdown').select2();
	$('.select2-dropdown-full').select2();
	 
});
function setElementValue(ele,val) {
    document.getElementById(ele).value = val;
}
$(document).ajaxComplete(function(){
	$("body").removeClass("is-loading");
});
$(document).ajaxStart(function(){
	$("body").addClass("is-loading");
}); 


$(function () {
	$("#ContentPlace_trmsg .widget-header.toggle-content-widget").click(function(){
		var act = $(this).find(".drop-down-toggle:first").hasClass("fa-minus-square");
		if(act){
			$(this).find(".drop-down-toggle:first").removeClass("fa-minus-square").addClass("fa-plus-square");
			$(this).next( ".widget-content" ).slideUp();
			
		}else{
			$(this).find(".drop-down-toggle:first").removeClass("fa-plus-square").addClass("fa-minus-square");			
			$(this).next( ".widget-content" ).slideDown();
		}		
	});
});
$(function () {
	$("#ContentPlace_trmsg .btn-search").click(function(){
		
		if($(this).closest('.widget-header').next( ".widget-content-search").hasClass('closed')){
			$(this).closest('.widget').find( ".widget-content-summary").removeClass('opened');
			$(this).closest('.widget').find( ".widget-content-summary").addClass('closed');
			$(this).closest('.widget').find( ".widget-content-summary").slideUp();
			
			$(this).closest('.widget-header').next( ".widget-content-search").removeClass('closed');
			$(this).closest('.widget-header').next( ".widget-content-search").addClass('opened');
			$(this).closest('.widget-header').find( ".btn-summary").removeClass('opened');
			$(this).closest('.widget-header').find( ".btn-summary").addClass('closed');
			$(this).addClass('opened');
			$(this).removeClass('closed');
			$(this).closest('.widget-header').next( ".widget-content-search").slideDown();
			if (typeof $(this).attr('data-drawer') !== 'undefined') {
				if($(this).attr('data-drawer') == "search"){
					if (typeof $(this).attr('data-type') !== 'undefined') {
						if (typeof $(this).attr('data-status') !== 'undefined') {
							if (typeof initializeSearchDrawer == 'function') { 
								initializeSearchDrawer($(this)); 
							}
						}	
					}
				}
			}
		}else{
			$(this).removeClass('opened');
			$(this).addClass('closed');
			$(this).closest('.widget-header').next( ".widget-content-search").removeClass('opened');
			$(this).closest('.widget-header').next( ".widget-content-search").addClass('closed');
			$(this).closest('.widget-header').next( ".widget-content-search").slideUp();
			$(this).closest('.widget-header').find( ".btn-summary").removeClass('opened');
			$(this).closest('.widget-header').find( ".btn-summary").addClass('closed');
		}
	});
	$("#ContentPlace_trmsg .btn-summary").click(function(){
		
		if($(this).closest('.widget').find( ".widget-content-summary").hasClass('closed')){
			
			$(this).closest('.widget-header').next( ".widget-content-search").removeClass('opened');
			$(this).closest('.widget-header').next( ".widget-content-search").addClass('closed');
			$(this).closest('.widget-header').next( ".widget-content-search").slideUp();
			$(this).closest('.widget-header').find( ".btn-search").removeClass('opened');
			$(this).closest('.widget-header').find( ".btn-search").addClass('closed');
			
			$(this).closest('.widget').find( ".widget-content-summary").removeClass('closed');
			$(this).closest('.widget').find( ".widget-content-summary").addClass('opened');
			$(this).closest('.widget').find( ".widget-content-summary").slideDown();
			$(this).addClass('opened');
			$(this).removeClass('closed');
			if (typeof $(this).attr('data-query') !== 'undefined') {
					if (typeof initializeSummaryDrawer == 'function') { 
					
						initializeSummaryDrawer($(this)); 
					}
				}
			}
		else{
			$(this).removeClass('opened');
			$(this).addClass('closed');
			$(this).closest('.widget').find( ".widget-content-summary").removeClass('opened');
			$(this).closest('.widget').find( ".widget-content-summary").addClass('closed');
			$(this).closest('.widget').find( ".widget-content-summary").slideUp();
			$(this).closest('.widget-header').find( ".btn-search").removeClass('opened');
			$(this).closest('.widget-header').find( ".btn-search").addClass('closed');
		}
	});
});

jQuery(function($){
	$('[data-footable]').footable({
	"toggleSelector":"tr,td,.footable-toggle,center",
	"cascade": true,
	"breakpoints":{
		"xs": 0, 
		"sm": 480,
		"md": 768, 
		"lg": 1200 
	}});
	$('.drawer').drawer();
	$(".btn-resend-email-verification").click(function(){
		var data = {
			action: 'resendVerificationEmail'
		}
		$.ajax({  
			type: "POST",  
			url: "ajaxcall.php",
			ContentType : 'application/json',
			dataType: 'JSON',
			data: data,
			beforeSend: function() {
				$("body").addClass("is-loading");
			},
			success: function(data){     
				if(data.status == 'OK')
				{ 
					$(".btn-resend-email-verification").removeClass("btn").removeClass("btn-info").addClass("email-verification-mail-sent").html(data.data);
				} 
				else if (data.status == 'ERROR')
				{ 
					$(".btn-resend-email-verification").removeClass("btn").removeClass("btn-info").addClass("email-verification-mail-sent").html(data.data);
				}
				$("body").removeClass("is-loading");
			},
			error: function(data){
				$("body").removeClass("is-loading");
			},
			complete: function(data){
				$("body").removeClass("is-loading");
			}
		
		}); 
	});
			
			
		

});

equalheight = function(container){

var currentTallest = 0,
     currentRowStart = 0,
     rowDivs = new Array(),
     $el,
     topPosition = 0;
 $(container).each(function() {

   $el = $(this);
   $($el).height('auto')
   topPosition = $el.position().top;

   if (currentRowStart != topPosition) {
     for (var currentDiv = 0 ; currentDiv < rowDivs.length ; currentDiv++) {
       rowDivs[currentDiv].height(currentTallest);
     }
     rowDivs.length = 0; // empty the array
     currentRowStart = topPosition;
     currentTallest = $el.height();
     rowDivs.push($el);
   } else {
     rowDivs.push($el);
     currentTallest = (currentTallest < $el.height()) ? ($el.height()) : (currentTallest);
  }
   for (var currentDiv = 0 ; currentDiv < rowDivs.length ; currentDiv++) {
     rowDivs[currentDiv].height(currentTallest);
   }
 });
}

$(window).load(function() {
  equalheight('.equal-height-divs');
});


$(window).resize(function(){
  equalheight('.equal-height-divs');
});

$( document ).ready(function() {
	$('.show_other_tax_1 a').click(function(){
		$('.show_other_tax_1').hide();
		$('.other_tax_1 .hidden_other_tax').hide().slideDown();
	});
	$('.show_other_tax_2 a').click(function(){
		$('.show_other_tax_2').hide();
		$('.other_tax_2 .hidden_other_tax').hide().slideDown();
	});
	if($('input#other_tax_value').val() && $('input#other_tax_value').val() != '0.00'){
		$('.show_other_tax_1').hide();
		$('.other_tax_1 .hidden_other_tax').hide().slideDown();
	}
	if($('input#total_discount_value').val() && $('input#total_discount_value').val() != '0.00'){
		$('.show_other_tax_2').hide();
		$('.other_tax_2 .hidden_other_tax').hide().slideDown();
	}
});

$( document ).ready(function() {
	var intervalId = window.setInterval(function(){
		if($(".submit_for_draft").length > 0){
			$('#submittype').val('draft');
			$('#action').val('autoDraft');
			var form = $('.submit_for_draft');
			var url = 'ajaxcall.php';
			$.ajax({
				type: "POST",
				url: url,
				data: form.serialize(),
				 beforeSend: function() {					
					$('body').addClass('savedarft_loader');
				},
				success: function(data)
				{
					if(data.status == 'ERROR'){						
						$(".gogst_popup-content").html(data.msg);
						$(".gogst_popup-header").html("Error in Completing your request.");
						$('#gogst_popup').popup({
							scrolllock: true,
							transition: 'all 0.3s'
						});
						$('#gogst_popup').popup('show');
					}else
					if(data != null && data.draft_id != undefined && data.draft_id != ""){
						$('#draft_id').val(data.draft_id);	
						$('.discard_btn').show();	
					}
					
				},
				error: function() {
					 $('body').removeClass('savedarft_loader');
				},
				complete: function() {
					$('body').removeClass('savedarft_loader');
				},
			});
		}
	}, 120000);
	$('.discard_btn').click(function(){
		if($('#draft_id').val() != "" && $('.bill_back_btn').attr('href') != ""){
			var data = {
				action: 'discardDraft',
				draft_id: $('#draft_id').val()
			}
			var url = 'ajaxcall.php';
			$.ajax({
				type: "POST",
				url: url,
				data: data,
				success: function(data)
				{					
					window.location.href = $('.bill_back_btn').attr('href');
				}
			});
			
		}
		
	});
});


/* ALT key shortcode js */

function shortkeys_fun(){
	document.addEventListener("keydown", function(event) {
		if(event.altKey){
			$('body').addClass('alt_key_active');
			event.preventDefault();
		}
	});
	document.addEventListener("keyup", function(event) {	
		$('body').removeClass('alt_key_active');
		event.preventDefault();
	});
	document.addEventListener("keydown", function(event) {
		if (event.altKey && event.keyCode >= 65 && event.keyCode <= 90)
		{
			if($('.shortcut_key:contains("'+event.key+'")').closest('a').attr('href') != undefined && $('.shortcut_key:contains("'+event.key+'")').closest('a').attr('href') != ""){
				window.location.href = $('.shortcut_key:contains("'+event.key+'")').closest('a').attr('href');
				event.preventDefault();
			}else{
				if($('.shortcut_key:contains("'+event.key+'")').closest('a').attr('data-toggle') != undefined && $('.shortcut_key:contains("'+event.key+'")').closest('a').attr('data-toggle') == "modal"){
					$($('.shortcut_key:contains("'+event.key+'")').closest('a').attr('data-target')).modal('show');
					event.preventDefault();
				}else if($('.shortcut_key:contains("'+event.key+'")').closest('.btn').attr('class') != undefined){
					$('.shortcut_key:contains("'+event.key+'")').closest('.btn').trigger('click');
					event.preventDefault();
				}
			}
		}
	});
	
	
	/* CTRL key shortcode js */
	document.addEventListener("keydown", function(event) {
		if(event.ctrlKey){
			$('body').addClass('ctrl_key_active');
		}
	});
	document.addEventListener("keyup", function(event) {	
		$('body').removeClass('ctrl_key_active');
	});
	document.addEventListener("keydown", function(event) {
		if (event.ctrlKey && event.keyCode >= 65 && event.keyCode <= 90)
		{
			if($('.shortcut_key_ctrl:contains("'+event.key+'")').closest('a').attr('href') != undefined && $('.shortcut_key_ctrl:contains("'+event.key+'")').closest('a').attr('href') != ""){
				window.location.href = $('.shortcut_key_ctrl:contains("'+event.key+'")').closest('a').attr('href');
				event.preventDefault();
			}else{
				if($('.shortcut_key_ctrl:contains("'+event.key+'")').closest('a').attr('data-toggle') != undefined && $('.shortcut_key_ctrl:contains("'+event.key+'")').closest('a').attr('data-toggle') == "modal"){
					$($('.shortcut_key_ctrl:contains("'+event.key+'")').closest('a').attr('data-target')).modal('show');
					event.preventDefault();
				}else if($('.shortcut_key_ctrl:contains("'+event.key+'")').closest('.btn').attr('class') != undefined){
					$('.shortcut_key_ctrl:contains("'+event.key+'")').closest('.btn').trigger('click');
					event.preventDefault();
				}
			}
		}
	});
}



$( document ).ready(function() {
	$('.import_summary_toggle_btn').on('click',function() {	
		$(this).closest('.widget').find('.widget-content').toggle();
		$(this).closest('.widget').find('.widget-content').toggleClass("showDiv");
		$(this).toggleClass("fa-plus-square fa-minus-square");
	});			                
});



$(document).ready(function(){
	$(document).on("change blur keypress keyup", ".decimal_numeric_only", function(e){				
		var value=$(this).val().replace(/[^0-9.-]*/g, '');
        value=value.replace(/\.{2,}/g, '.');
        value=value.replace(/\.,/g, ',');
        value=value.replace(/\,\./g, ',');
		
        value=value.replace( /^([^.]*\.)(.*)$/, function ( a, b, c ) { return b + c.replace( /\./g, '' ); }); //remove all dots except first one
		$(this).val(value);
	});
});
$(document).ready(function(){
	$(document).on("change blur keypress keyup", ".numeric_only", function(e){				
		var value=$(this).val().replace(/[^0-9]*/g, '');        
		$(this).val(value);
	});
});

$(document).ready(function(){
	$(document).on("change blur keypress keyup", "input[name=gstno]", function(e){
		$(this).val($(this).val().replace(/ /g, ""));
	});
});

(function ($) {
  $.fn.fixTableHeader = function (options) {

    var settings = $.extend({
      fixHeader: true,
      fixFooter: false
    }, options);

    var container = this;
    var table = this.find('table');
    var xHeaders;
    var xFooters;

    if (this.find('table').has('thead').length) {
      if (this.find('table thead').has('th').length) {
        xHeaders = this.find("table thead th");
      }
      else {
        xHeaders = this.find("table thead td");
      }
    }
    else if (this.find('table').has('tbody').length) {

      if (this.find('table tbody').has('th').length) {
        xHeaders = this.find("table tbody th");
      }
      else {
        xHeaders = this.find("table tbody > tr:first-child td");
      }
    }
    else if (this.find('table').has('th').length) {
      xHeaders = this.find("table th");
    }
    else {
      xHeaders = this.find("table > tr:first-child td");
    }

    if (this.find('table').has('tfoot').length) {
      xFooters = this.find("table tfoot td");
    }
    else {
      if (this.find('table').has('tbody').length) {
        xFooters = this.find("table tbody > tr:last-child td");
      }
      else {
        xFooters = this.find("table > tr:last-child td");
      }
    }

    var containerHeight = 0;
    if (hasScrollbar(container)) {
      containerHeight = container.height() - getScrollBarSize();
    }
    else {
      containerHeight = container.height();
    }

    xHeaders.each(function () {
      $(this).addClass(' fth-header');
    });

    xFooters.each(function () {
      $(this).addClass(' fth-footer');
    })

    this.scroll(function () {
      if (settings.fixHeader) {
        xHeaders.each(function () {
          $(this).css('position', 'relative');
          $(this).css('top', container.scrollTop() + 'px');
        });
      }

      if (settings.fixFooter) {
        xFooters.each(function () {
          $(this).css('position', 'relative');
          $(this).css('top', ((containerHeight - table.height() + container.scrollTop())) + 'px');

        })
      }
    })
  };

  function getScrollBarSize() {
    var $outer = $('<div>').css({ visibility: 'hidden', width: 100, overflow: 'scroll' }).appendTo('body'),
        widthWithScroll = $('<div>').css({ width: '100%' }).appendTo($outer).outerWidth();
    $outer.remove();
    return 100 - widthWithScroll;
  };

  function hasScrollbar(node) {
    var el = document.getElementById($(node).attr('id'));
    var overflowX = window.getComputedStyle(el)['overflow-x'];
    return (overflowX === 'scroll' || overflowX === 'auto') && el.scrollWidth > el.clientWidth;
  }
}(jQuery));




function selct_state_option_ship(this_ele,$val,dropdown,input,name)
{
	if($val == 'India') {
		this_ele.closest('.shipping_address_reapiter').find('.'+dropdown).show(); 
		this_ele.closest('.shipping_address_reapiter').find('.'+input).hide();
		this_ele.closest('.shipping_address_reapiter').find('.'+dropdown).attr("name",name+"[]"); 
		this_ele.closest('.shipping_address_reapiter').find('.'+input).attr("name",name+"x"); 
	}
	else{
		this_ele.closest('.shipping_address_reapiter').find('.'+dropdown).hide(); 
		this_ele.closest('.shipping_address_reapiter').find('.'+input).show();
		this_ele.closest('.shipping_address_reapiter').find('.'+dropdown).attr("name",name+"x"); 
		this_ele.closest('.shipping_address_reapiter').find('.'+input).attr("name",name+"[]"); 
	}
}
$(document).on("change", ".listBoxCountry1", function(e){
	$(this).attr("data-value",$(this).val());
	selct_state_option_ship($(this),$(this).val(),"all_state_list","newState1","ship_state");
});
$(document).on("change", ".all_state_list", function(e){
	$(this).attr("data-value",$(this).val());
});
$(document).on("click", ".add_shipping", function(e){		
	var shipping_add = '<div class="shipping_address_reapiter"><div class="shipping_counter">1</div><div class="btn_remove_shipping"><i class="fa fa-trash" aria-hidden="true"></i></div><div class="control-group"><label for="Ship. Name" class="control-label">Ship. Name <span class="star_red">*</span></label><div class="controls"><input type="text" value="" name="ship_name[]" class="span4 ship_name" placeholder="Enter shipping Name"></div> </div> <div class="control-group"><label for="Ship. Phone" class="control-label">Ship. Phone</label><div class="controls"><input type="text" value="" name="ship_phone[]" class="span4 ship_phone"  placeholder="Enter shipping phone No." maxlength="20" ></div> </div> <div class="control-group"><label for="Ship. Address" class="control-label">Ship. Address</label><div class="controls"><textarea name="ship_address[]" class="span4 ship_address" placeholder="Enter shipping address"></textarea></div> </div> <div class="control-group"><label for="ship_pincode" class="control-label">Ship. Pincode</label><div class="controls"><input type="text" value="" name="ship_pincode[]" class="span4 ship_pincode"  placeholder="Enter shipping pincode" maxlength="20" ></div> </div> <div class="control-group"><label for="Ship. State" class="control-label">Ship. State <span class="star_red">*</span></label><div class="controls"><select type="list" data-value="" name="ship_state[]"   class="span4 all_state_list"></select><input type="text" name="ship_statex[]" placeholder="Enter State" value=""   class="span4 hide newState1 "/></div> </div> <div class="control-group"><label for="ship_country" class="control-label">Ship. Country</label><div class="controls"><select data-value="India"  type="list"   name="ship_country[]"   class="span4 listBoxCountry1 ship_country"></select></div> </div> <div class="control-group"><label for="Ship. GSTIN / PAN" class="control-label">Ship. GSTIN / PAN</label><div class="controls"><input type="text" value=""  name="ship_gstno[]" class="span4 ship_gstno" placeholder="Enter shipping GSTIN / PAN" maxlength="20" ></div> </div> <div class="control-group"><label for="Distance for e-way bill (in km)" class="control-label">Distance for e-way bill (in km)</label><div class="controls" style="position:relative;"><input type="text" value=""  name="shipping_distance_eway[]" class="span4 shipping_distance_eway" placeholder="Enter Distance for e-way bill (in km)"    ><div class="btn distance_autofill"  distance_for="shipping"  style="float:right;position: absolute;right: 1px; top: 1px; padding:4px 15px;">Auto Fill</div></div></div></div>';
	$(".shipping_address_section").append(shipping_add);
	
	var options = '';	
	for (var i = 0; i < handlescon.length; i++) {  
		if(handlescon[i] == "Select State" || handlescon[i] == "Select Country")  {	options += '<option value="">' + handlescon[i] + '</option>';  }  else  {	options += '<option value="' + handlescon[i] + '">' + handlescon[i] + '</option>';  }
	}	
	$('.listBoxCountry1').html(options);		
	$(".listBoxCountry1").each(function() {
		if($(this).attr('data-value').length>0)
		{
			if($(this).attr("data-value") != "")
			{
				$(this).val($(this).attr("data-value"));
			}
			
		}
	});
		
		
	var options = '';
	for (var i = 0; i < handles.length; i++) {  
		if(handles[i] == "Select State")  {	
			options += '<option value="">' + handles[i] + '</option>';  
		}  
		else  
		{	
			if(handles[i] == "Dadra and Nagar Haveli" || handles[i] == "Daman and Diu" )
			{
				options += '<option value="' + handles[i] + '">' + handles[i] +handlesCodes[i]+ '**</option>';  
			}
			else
			{
				options += '<option value="' + handles[i] + '">' + handles[i] +handlesCodes[i]+ '</option>';  
			}
			
		}
	} 
	$('.all_state_list').html(options);	
	$(".all_state_list").each(function() {		
		if($(this).attr('data-value').length>0)
		{
			if($(this).attr("data-value") != "")
			{				
				$(this).val($(this).attr("data-value"));
			}
			
		}
		
	});
	shipping_addresses_json_input();
});
$(document).on("click", ".btn_remove_shipping", function(e){
	/* if($('.shipping_address_reapiter').length> 1){ */
		$(this).closest('.shipping_address_reapiter').remove();	
	/* } */
	shipping_addresses_json_input();
});
function shipping_addresses_json_input(){	
	var counter = 1;
	$('.shipping_address_reapiter').each(function() {
		$(this).find('.shipping_counter').html(counter);
		counter = counter + 1;		
	});
	/* if($('.shipping_address_reapiter').length> 1){
		$('.btn_remove_shipping').show();
	}else{
		$('.btn_remove_shipping').hide();
	} */
	$('.listBoxCountry1').trigger('change');
	
}
$(document).ready(function(){	
	shipping_addresses_json_input();
});


$(document).ready(function(){
	$(document).on("change", "#SameShippingAdd", function(){
		if($('#SameShippingAdd').is(":checked")){			
			$('#shipping_address').removeAttr("required");
		}else{
			$('#shipping_address').attr("required",1);
		}
	});
	$(document).on("change", "#shipping_address", function(){
		update_shipping_from_dropdown();
	});
});
function update_shipping_from_dropdown(){
	var shipping_name = "";	
	var ship_address = "";	
	var ship_phone = "";	
	var ship_pincode = "";	
	var ship_gstno = "";	
	var ship_country = "";	
	var ship_state = "";	
	var shipping_distance_eway = "";	
	
	if($('#shipping_address').val() != ""){
		shipping_name = $('#shipping_address option:selected').attr('value');
		$('.shippingName').text(shipping_name);
		$('#shippingName').val(shipping_name);
		
		ship_country = $('#shipping_address option:selected').attr('ship_country');
		ship_pincode = $('#shipping_address option:selected').attr('ship_pincode');
		ship_address = $('#shipping_address option:selected').attr('ship_address');
		ship_state = $('#shipping_address option:selected').attr('ship_state');		
		
		
		if(ship_state != ""){
			ship_address = ship_address + ', ' + ship_state;
		}
		if(ship_country != ""){
			ship_address = ship_address + ', ' + ship_country;
		}
		if(ship_pincode != ""){
			ship_address = ship_address + ' - ' + ship_pincode;
		}
		$('.shippingAddress').text(ship_address);
		$('#shippingAddress').val(ship_address);
		
		ship_phone = $('#shipping_address option:selected').attr('ship_phone');
		$('.shippingPhone').text(ship_phone);
		$('#shippingPhone').val(ship_phone);
		
		
		
		
		ship_gstno = $('#shipping_address option:selected').attr('ship_gstno');
		$('.shippingGSTIN').text(ship_gstno);
		$('#shippingGSTIN').val(ship_gstno);
		
		
		
		
		shipping_distance_eway = $('#shipping_address option:selected').attr('shipping_distance_eway');		
		$('#shipping_distance_eway').val(shipping_distance_eway);
		
		
		
	}
	$('#shippingName').val(shipping_name);
	$('#shippingAddress').val(ship_address);				
	$('#shippingPhone').val(ship_phone);				
	$('#shippingPincode').val(ship_pincode);				
	$('#shippingGSTIN').val(ship_gstno);				
	$('#shippingCountry').val(ship_country);				
	$('#shippingState').val(ship_state);	
	if(shipping_name == ""){
		$('.shippingName').text('-');
	}
	if(ship_address == ""){
		$('.shippingAddress').text('-');
	}
	if(ship_phone == ""){
		$('.shippingPhone').text('-');
	}
	if(ship_pincode == ""){
		$('.shippingPincode').text('-');
	}
	if(ship_gstno == ""){
		$('.shippingGSTIN').text('-');
	}
	if(ship_country == ""){
		$('.shippingCountry').text('-');
	}
	if(ship_state == ""){
		$('.shippingState').text('-');
	}
} 