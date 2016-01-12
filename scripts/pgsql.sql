/*
 * CREATE ROLE cargo LOGIN ENCRYPTED PASSWORD 'yourpassword';
 * CREATE DATABASE cargodb OWNER = cargo ENCODING = 'UTF-8';
 *
 */

drop table if exists ist;
drop table if exists ico; 

drop table if exists gtz;

create table gtz (
	gtzcod		varchar(40) not null primary key
);
comment on table gtz		is 'Timezone';
comment on column gtz.gtzcod	is 'Code';

insert into gtz select name from pg_timezone_names;

drop table if exists iln;

create table iln (
	ilncod		varchar(2) not null default '' primary key,
	ilndes		varchar(80) not null default ''
);

comment on table iln		is 'ISO 639 language code';
comment on column iln.ilncod	is 'Alpha-2 code';
comment on column iln.ilndes	is 'Description';

insert into iln values('aa','Afar');
insert into iln values('ab','Abkhazian');
insert into iln values('ae','Avestan');
insert into iln values('af','Afrikaans');
insert into iln values('ak','Akan');
insert into iln values('am','Amharic');
insert into iln values('an','Aragonese');
insert into iln values('ar','Arabic');
insert into iln values('as','Assamese');
insert into iln values('av','Avaric');
insert into iln values('ay','Aymara');
insert into iln values('az','Azerbaijani');
insert into iln values('ba','Bashkir');
insert into iln values('be','Belarusian');
insert into iln values('bg','Bulgarian');
insert into iln values('bh','Bihari languages');
insert into iln values('bi','Bislama');
insert into iln values('bm','Bambara');
insert into iln values('bn','Bengali');
insert into iln values('bo','Tibetan');
insert into iln values('br','Breton');
insert into iln values('bs','Bosnian');
insert into iln values('ca','Catalan; Valencian');
insert into iln values('ce','Chechen');
insert into iln values('ch','Chamorro');
insert into iln values('co','Corsican');
insert into iln values('cr','Cree');
insert into iln values('cs','Czech');
insert into iln values('cu','Church Slavic');
insert into iln values('cv','Chuvash');
insert into iln values('cy','Welsh');
insert into iln values('da','Danish');
insert into iln values('de','German');
insert into iln values('dv','Divehi; Dhivehi; Maldivian');
insert into iln values('dz','Dzongkha');
insert into iln values('ee','Ewe');
insert into iln values('el','Greek, Modern (1453-)');
insert into iln values('en','English');
insert into iln values('eo','Esperanto');
insert into iln values('es','Spanish; Castilian');
insert into iln values('et','Estonian');
insert into iln values('eu','Basque');
insert into iln values('fa','Persian');
insert into iln values('ff','Fulah');
insert into iln values('fi','Finnish');
insert into iln values('fj','Fijian');
insert into iln values('fo','Faroese');
insert into iln values('fr','French');
insert into iln values('fy','Western Frisian');
insert into iln values('ga','Irish');
insert into iln values('gd','Gaelic; Scottish Gaelic');
insert into iln values('gl','Galician');
insert into iln values('gn','Guarani');
insert into iln values('gu','Gujarati');
insert into iln values('gv','Manx');
insert into iln values('ha','Hausa');
insert into iln values('he','Hebrew');
insert into iln values('hi','Hindi');
insert into iln values('ho','Hiri Motu');
insert into iln values('hr','Croatian');
insert into iln values('ht','Haitian; Haitian Creole');
insert into iln values('hu','Hungarian');
insert into iln values('hy','Armenian');
insert into iln values('hz','Herero');
insert into iln values('ia','Interlingua (International Auxiliary Language Association)');
insert into iln values('id','Indonesian');
insert into iln values('ie','Interlingue; Occidental');
insert into iln values('ig','Igbo');
insert into iln values('ii','Sichuan Yi; Nuosu');
insert into iln values('ik','Inupiaq');
insert into iln values('io','Ido');
insert into iln values('is','Icelandic');
insert into iln values('it','Italian');
insert into iln values('iu','Inuktitut');
insert into iln values('ja','Japanese');
insert into iln values('jv','Javanese');
insert into iln values('ka','Georgian');
insert into iln values('kg','Kongo');
insert into iln values('ki','Kikuyu; Gikuyu');
insert into iln values('kj','Kuanyama; Kwanyama');
insert into iln values('kk','Kazakh');
insert into iln values('kl','Kalaallisut; Greenlandic');
insert into iln values('km','Central Khmer');
insert into iln values('kn','Kannada');
insert into iln values('ko','Korean');
insert into iln values('kr','Kanuri');
insert into iln values('ks','Kashmiri');
insert into iln values('ku','Kurdish');
insert into iln values('kv','Komi');
insert into iln values('kw','Cornish');
insert into iln values('ky','Kirghiz; Kyrgyz');
insert into iln values('la','Latin');
insert into iln values('lb','Luxembourgish; Letzeburgesch');
insert into iln values('lg','Ganda');
insert into iln values('li','Limburgan; Limburger; Limburgish');
insert into iln values('ln','Lingala');
insert into iln values('lo','Lao');
insert into iln values('lt','Lithuanian');
insert into iln values('lu','Luba-Katanga');
insert into iln values('lv','Latvian');
insert into iln values('mg','Malagasy');
insert into iln values('mh','Marshallese');
insert into iln values('mi','Maori');
insert into iln values('mk','Macedonian');
insert into iln values('ml','Malayalam');
insert into iln values('mn','Mongolian');
insert into iln values('mr','Marathi');
insert into iln values('ms','Malay');
insert into iln values('mt','Maltese');
insert into iln values('my','Burmese');
insert into iln values('na','Nauru');
insert into iln values('nb','Bokmål, Norwegian; Norwegian Bokmål');
insert into iln values('nd','Ndebele, North; North Ndebele');
insert into iln values('ne','Nepali');
insert into iln values('ng','Ndonga');
insert into iln values('nl','Dutch; Flemish');
insert into iln values('nn','Norwegian Nynorsk; Nynorsk, Norwegian');
insert into iln values('no','Norwegian');
insert into iln values('nr','Ndebele, South; South Ndebele');
insert into iln values('nv','Navajo; Navaho');
insert into iln values('ny','Chichewa; Chewa; Nyanja');
insert into iln values('oc','Occitan (post 1500); Provençal');
insert into iln values('oj','Ojibwa');
insert into iln values('om','Oromo');
insert into iln values('or','Oriya');
insert into iln values('os','Ossetian; Ossetic');
insert into iln values('pa','Panjabi; Punjabi');
insert into iln values('pi','Pali');
insert into iln values('pl','Polish');
insert into iln values('ps','Pushto; Pashto');
insert into iln values('pt','Portuguese');
insert into iln values('qu','Quechua');
insert into iln values('rm','Romansh');
insert into iln values('rn','Rundi');
insert into iln values('ro','Romanian; Moldavian; Moldovan');
insert into iln values('ru','Russian');
insert into iln values('rw','Kinyarwanda');
insert into iln values('sa','Sanskrit');
insert into iln values('sc','Sardinian');
insert into iln values('sd','Sindhi');
insert into iln values('se','Northern Sami');
insert into iln values('sg','Sango');
insert into iln values('si','Sinhala; Sinhalese');
insert into iln values('sk','Slovak');
insert into iln values('sl','Slovenian');
insert into iln values('sm','Samoan');
insert into iln values('sn','Shona');
insert into iln values('so','Somali');
insert into iln values('sq','Albanian');
insert into iln values('sr','Serbian');
insert into iln values('ss','Swati');
insert into iln values('st','Sotho, Southern');
insert into iln values('su','Sundanese');
insert into iln values('sv','Swedish');
insert into iln values('sw','Swahili');
insert into iln values('ta','Tamil');
insert into iln values('te','Telugu');
insert into iln values('tg','Tajik');
insert into iln values('th','Thai');
insert into iln values('ti','Tigrinya');
insert into iln values('tk','Turkmen');
insert into iln values('tl','Tagalog');
insert into iln values('tn','Tswana');
insert into iln values('to','Tonga (Tonga Islands)');
insert into iln values('tr','Turkish');
insert into iln values('ts','Tsonga');
insert into iln values('tt','Tatar');
insert into iln values('tw','Twi');
insert into iln values('ty','Tahitian');
insert into iln values('ug','Uighur; Uyghur');
insert into iln values('uk','Ukrainian');
insert into iln values('ur','Urdu');
insert into iln values('uz','Uzbek');
insert into iln values('ve','Venda');
insert into iln values('vi','Vietnamese');
insert into iln values('vo','Volapük');
insert into iln values('wa','Walloon');
insert into iln values('wo','Wolof');
insert into iln values('xh','Xhosa');
insert into iln values('yi','Yiddish');
insert into iln values('yo','Yoruba');
insert into iln values('za','Zhuang; Chuang');
insert into iln values('zh','Chinese');
insert into iln values('zu','Zulu');

drop table if exists icu;

create table icu (
	icucod		varchar(3) not null default '' primary key,
	icudes		varchar(80) not null default '',
	icudas		smallint not null default 0
);

comment on table icu		is 'ISO 639 language code';
comment on column icu.icucod	is 'Alpha-3 code';
comment on column icu.icudes	is 'Description';
comment on column icu.icudas	is 'Digits after decimal separator';

insert into icu values('ADP','Andorran Peseta',0);
insert into icu values('AED','UAE Dirham',2);
insert into icu values('AFA','Afghani',0);
insert into icu values('AFN','Afghani',2);
insert into icu values('ALK','Old Lek',0);
insert into icu values('ALL','Lek',2);
insert into icu values('AMD','Armenian Dram',2);
insert into icu values('ANG','Netherlands Antillean Guilder',2);
insert into icu values('AOA','Kwanza',2);
insert into icu values('AOK','Kwanza',0);
insert into icu values('AON','New Kwanza',0);
insert into icu values('AOR','Kwanza Reajustado',0);
insert into icu values('ARA','Austral',0);
insert into icu values('ARP','Peso Argentino',0);
insert into icu values('ARS','Argentine Peso',2);
insert into icu values('ARY','Peso',0);
insert into icu values('ATS','Schilling',0);
insert into icu values('AUD','Australian Dollar',2);
insert into icu values('AWG','Aruban Florin',2);
insert into icu values('AYM','Azerbaijan Manat',0);
insert into icu values('AZM','Azerbaijanian Manat',0);
insert into icu values('AZN','Azerbaijanian Manat',2);
insert into icu values('BAD','Dinar',0);
insert into icu values('BAM','Convertible Mark',2);
insert into icu values('BBD','Barbados Dollar',2);
insert into icu values('BDT','Taka',2);
insert into icu values('BEC','Convertible Franc',0);
insert into icu values('BEF','Belgian Franc ',0);
insert into icu values('BEL','Financial Franc',0);
insert into icu values('BGJ','Lev A/52',0);
insert into icu values('BGK','Lev A/62',0);
insert into icu values('BGL','Lev',0);
insert into icu values('BGN','Bulgarian Lev',2);
insert into icu values('BHD','Bahraini Dinar',3);
insert into icu values('BIF','Burundi Franc',0);
insert into icu values('BMD','Bermudian Dollar',2);
insert into icu values('BND','Brunei Dollar',2);
insert into icu values('BOB','Boliviano',2);
insert into icu values('BOP','Peso boliviano',0);
insert into icu values('BOV','Mvdol',2);
insert into icu values('BRB','Cruzeiro',0);
insert into icu values('BRC','Cruzado',0);
insert into icu values('BRE','Cruzeiro',0);
insert into icu values('BRL','Brazilian Real',2);
insert into icu values('BRN','New Cruzado',0);
insert into icu values('BRR','Cruzeiro Real',0);
insert into icu values('BSD','Bahamian Dollar',2);
insert into icu values('BTN','Ngultrum',2);
insert into icu values('BWP','Pula',2);
insert into icu values('BYB','Belarussian Ruble',0);
insert into icu values('BYR','Belarussian Ruble',0);
insert into icu values('BZD','Belize Dollar',2);
insert into icu values('CAD','Canadian Dollar',2);
insert into icu values('CDF','Congolese Franc',2);
insert into icu values('CHC','WIR Franc (for electronic)',0);
insert into icu values('CHE','WIR Euro',2);
insert into icu values('CHF','Swiss Franc',2);
insert into icu values('CHW','WIR Franc',2);
insert into icu values('CLF','Unidades de fomento',0);
insert into icu values('CLP','Chilean Peso',0);
insert into icu values('CNX','Peoples Bank Dollar',0);
insert into icu values('CNY','Yuan Renminbi',2);
insert into icu values('COP','Colombian Peso',2);
insert into icu values('COU','Unidad de Valor Real',2);
insert into icu values('CRC','Costa Rican Colon',2);
insert into icu values('CSD','Serbian Dinar',0);
insert into icu values('CSJ','Krona A/53',0);
insert into icu values('CSK','Koruna',0);
insert into icu values('CUC','Peso Convertible',2);
insert into icu values('CUP','Cuban Peso',2);
insert into icu values('CVE','Cape Verde Escudo',2);
insert into icu values('CYP','Cyprus Pound',0);
insert into icu values('CZK','Czech Koruna',2);
insert into icu values('DDM','Mark der DDR',0);
insert into icu values('DEM','Deutsche Mark',0);
insert into icu values('DJF','Djibouti Franc',0);
insert into icu values('DKK','Danish Krone',2);
insert into icu values('DOP','Dominican Peso',2);
insert into icu values('DZD','Algerian Dinar',2);
insert into icu values('ECS','Sucre',0);
insert into icu values('EEK ','Kroon',0);
insert into icu values('EGP','Egyptian Pound',2);
insert into icu values('EQE','Ekwele',0);
insert into icu values('ERN','Nakfa',2);
insert into icu values('ESP','Spanish Peseta',0);
insert into icu values('ETB','Ethiopian Birr',2);
insert into icu values('EUR','Euro',2);
insert into icu values('FIM','Markka',0);
insert into icu values('FJD','Fiji Dollar',2);
insert into icu values('FKP','Falkland Islands Pound',2);
insert into icu values('FRF','French Franc',0);
insert into icu values('GBP','Pound Sterling',2);
insert into icu values('GEK','Georgian Coupon',0);
insert into icu values('GEL','Lari',2);
insert into icu values('GHC','Cedi',0);
insert into icu values('GHP','Ghana Cedi ',0);
insert into icu values('GHS','Ghana Cedi',2);
insert into icu values('GIP','Gibraltar Pound',2);
insert into icu values('GMD','Dalasi',2);
insert into icu values('GNE','Syli',0);
insert into icu values('GNF','Guinea Franc',0);
insert into icu values('GNS','Syli',0);
insert into icu values('GQE','Ekwele',0);
insert into icu values('GRD','Drachma',0);
insert into icu values('GTQ','Quetzal',2);
insert into icu values('GWE','Guinea Escudo',0);
insert into icu values('GWP','Guinea-Bissau Peso',0);
insert into icu values('GYD','Guyana Dollar',2);
insert into icu values('HKD','Hong Kong Dollar',2);
insert into icu values('HNL','Lempira',2);
insert into icu values('HRD','Croatian Dinar',0);
insert into icu values('HRK','Croatian Kuna',2);
insert into icu values('HTG','Gourde',2);
insert into icu values('HUF','Forint',2);
insert into icu values('IDR','Rupiah',2);
insert into icu values('IEP','Irish Pound',0);
insert into icu values('ILP','Pound',0);
insert into icu values('ILR','Old Shekel',0);
insert into icu values('ILS','New Israeli Sheqel',2);
insert into icu values('INR','Indian Rupee',2);
insert into icu values('IQD','Iraqi Dinar',3);
insert into icu values('IRR','Iranian Rial',2);
insert into icu values('ISJ','Old Krona',0);
insert into icu values('ISK','Iceland Krona',0);
insert into icu values('ITL','Italian Lira',0);
insert into icu values('JMD','Jamaican Dollar',2);
insert into icu values('JOD','Jordanian Dinar',3);
insert into icu values('JPY','Yen',0);
insert into icu values('KES','Kenyan Shilling',2);
insert into icu values('KGS','Som',2);
insert into icu values('KHR','Riel',2);
insert into icu values('KMF','Comoro Franc',0);
insert into icu values('KPW','North Korean Won',2);
insert into icu values('KRW','Won',0);
insert into icu values('KWD','Kuwaiti Dinar',3);
insert into icu values('KYD','Cayman Islands Dollar',2);
insert into icu values('KZT','Tenge',2);
insert into icu values('LAJ','Kip Pot Pol',0);
insert into icu values('LAK','Kip',2);
insert into icu values('LBP','Lebanese Pound',2);
insert into icu values('LKR','Sri Lanka Rupee',2);
insert into icu values('LRD','Liberian Dollar',2);
insert into icu values('LSL','Loti',2);
insert into icu values('LSM','Maloti',0);
insert into icu values('LTL','Lithuanian Litas',2);
insert into icu values('LTT','Talonas',0);
insert into icu values('LUC','Luxembourg Convertible Franc',0);
insert into icu values('LUF','Luxembourg Franc',0);
insert into icu values('LUL','Luxembourg Financial Franc',0);
insert into icu values('LVL','Latvian Lats',2);
insert into icu values('LVR','Latvian Ruble',0);
insert into icu values('LYD','Libyan Dinar',3);
insert into icu values('MAD','Moroccan Dirham',2);
insert into icu values('MAF','Mali Franc',0);
insert into icu values('MDL','Moldovan Leu',2);
insert into icu values('MGA','Malagasy Ariary',2);
insert into icu values('MGF','Malagasy Franc',0);
insert into icu values('MKD','Denar',2);
insert into icu values('MLF','Mali Franc',0);
insert into icu values('MMK','Kyat',2);
insert into icu values('MNT','Tugrik',2);
insert into icu values('MOP','Pataca',2);
insert into icu values('MRO','Ouguiya',2);
insert into icu values('MTL','Maltese Lira',0);
insert into icu values('MTP','Maltese Pound',0);
insert into icu values('MUR','Mauritius Rupee',2);
insert into icu values('MVQ','Maldive Rupee',0);
insert into icu values('MVR','Rufiyaa',2);
insert into icu values('MWK','Kwacha',2);
insert into icu values('MXN','Mexican Peso',2);
insert into icu values('MXP','Mexican Peso',0);
insert into icu values('MXV','Mexican Unidad de Inversion (UDI)',2);
insert into icu values('MYR','Malaysian Ringgit',2);
insert into icu values('MZE','Mozambique Escudo',0);
insert into icu values('MZM','Mozambique Metical',0);
insert into icu values('MZN','Mozambique Metical',2);
insert into icu values('NAD','Namibia Dollar',2);
insert into icu values('NGN','Naira',2);
insert into icu values('NIC','Cordoba',0);
insert into icu values('NIO','Cordoba Oro',2);
insert into icu values('NLG','Netherlands Guilder',0);
insert into icu values('NOK','Norwegian Krone',2);
insert into icu values('NPR','Nepalese Rupee',2);
insert into icu values('NZD','New Zealand Dollar',2);
insert into icu values('OMR','Rial Omani',3);
insert into icu values('PAB','Balboa',2);
insert into icu values('PEH','Sol',0);
insert into icu values('PEI','Inti',0);
insert into icu values('PEN','Nuevo Sol',2);
insert into icu values('PES','Sol',0);
insert into icu values('PGK','Kina',2);
insert into icu values('PHP','Philippine Peso',2);
insert into icu values('PKR','Pakistan Rupee',2);
insert into icu values('PLN','Zloty',2);
insert into icu values('PLZ','Zloty',0);
insert into icu values('PTE','Portuguese Escudo',0);
insert into icu values('PYG','Guarani',0);
insert into icu values('QAR','Qatari Rial',2);
insert into icu values('RHD','Rhodesian Dollar',0);
insert into icu values('ROK','Leu A/52',0);
insert into icu values('ROL','Old Leu',0);
insert into icu values('RON','New Romanian Leu',2);
insert into icu values('RSD','Serbian Dinar',2);
insert into icu values('RUB','Russian Ruble',2);
insert into icu values('RUR','Russian Ruble',0);
insert into icu values('RWF','Rwanda Franc',0);
insert into icu values('SAR','Saudi Riyal',2);
insert into icu values('SBD','Solomon Islands Dollar',2);
insert into icu values('SCR','Seychelles Rupee',2);
insert into icu values('SDD','Sudanese Dinar',0);
insert into icu values('SDG','Sudanese Pound',2);
insert into icu values('SDP','Sudanese Pound',0);
insert into icu values('SEK','Swedish Krona',2);
insert into icu values('SGD','Singapore Dollar',2);
insert into icu values('SHP','Saint Helena Pound',2);
insert into icu values('SIT','Tolar',0);
insert into icu values('SKK','Slovak Koruna',0);
insert into icu values('SLL','Leone',2);
insert into icu values('SOS','Somali Shilling',2);
insert into icu values('SRD','Surinam Dollar',2);
insert into icu values('SRG','Surinam Guilder',0);
insert into icu values('SSP','South Sudanese Pound',2);
insert into icu values('STD','Dobra',2);
insert into icu values('SUR','Rouble',0);
insert into icu values('SVC','El Salvador Colon',2);
insert into icu values('SYP','Syrian Pound',2);
insert into icu values('SZL','Lilangeni',2);
insert into icu values('THB','Baht',2);
insert into icu values('TJR','Tajik Ruble',0);
insert into icu values('TJS','Somoni',2);
insert into icu values('TMM','Turkmenistan Manat',0);
insert into icu values('TMT','Turkmenistan New Manat',2);
insert into icu values('TND','Tunisian Dinar',3);
insert into icu values('TOP','Pa’anga',2);
insert into icu values('TPE','Timor Escudo',0);
insert into icu values('TRL','Old Turkish Lira',0);
insert into icu values('TRY','Turkish Lira',2);
insert into icu values('TTD','Trinidad and Tobago Dollar',2);
insert into icu values('TWD','New Taiwan Dollar',2);
insert into icu values('TZS','Tanzanian Shilling',2);
insert into icu values('UAH','Hryvnia',2);
insert into icu values('UAK','Karbovanet',0);
insert into icu values('UGS','Uganda Shilling',0);
insert into icu values('UGW','Old Shilling',0);
insert into icu values('UGX','Uganda Shilling',2);
insert into icu values('USD','US Dollar',2);
insert into icu values('UYI','Uruguay Peso en Unidades Indexadas (URUIURUI)',0);
insert into icu values('UYN','Old Uruguay Peso',0);
insert into icu values('UYP','Uruguayan Peso',0);
insert into icu values('UYU','Peso Uruguayo',2);
insert into icu values('UZS','Uzbekistan Sum',2);
insert into icu values('VEB','Bolivar',0);
insert into icu values('VEF','Bolivar Fuerte',2);
insert into icu values('VNC','Old Dong',0);
insert into icu values('VND','Dong',0);
insert into icu values('VUV','Vatu',0);
insert into icu values('WST','Tala',2);
insert into icu values('YDD','Yemeni Dinar',0);
insert into icu values('YER','Yemeni Rial',2);
insert into icu values('YUD','New Yugoslavian Dinar',0);
insert into icu values('YUM','New Dinar',0);
insert into icu values('YUN','Yugoslavian Dinar',0);
insert into icu values('ZAR','Rand',2);
insert into icu values('ZMK','Zambian Kwacha',2);
insert into icu values('ZRN','New Zaire',0);
insert into icu values('ZRZ','Zaire',0);
insert into icu values('ZWC','Rhodesian Dollar',0);



create table ico (
	icocod		varchar(2) not null default '' primary key,
	icoal3		varchar(3) not null default '' unique,
	iconum		integer not null default 0 unique,
	icodes		varchar(80) not null default '',
	icoicucod	varchar(3) references icu,
	icoilncod	varchar(2) references iln
);

comment on table ico 		is 'ISO 3166 country code';
comment on column ico.icocod	is 'Alpha-2 code';
comment on column ico.icoal3	is 'Alpha-3 code';
comment on column ico.iconum	is 'Numeric code';
comment on column ico.icodes 	is 'Description';
comment on column ico.icoicucod	is 'Currency';
comment on column ico.icoilncod	is 'Language';

create table ist (
	istcod		varchar(10) not null default '' primary key,
	istdes		varchar(80) not null default '',
	isticocod	varchar(2) not null references ico
);

comment on table ist 		is 'ISO 3166-2 subdivision code';
comment on column ist.istcod	is 'Code';
comment on column ist.istdes	is 'Description';
comment on column ist.isticocod	is 'Country code';

/*
 * registry
 */
 
drop table if exists reg;

create table reg (
	regcod varchar(256) not null default '' primary key,
	regdes text not null default '',
	regnum numeric not null default '0',
	regtxt text not null default ''
);

comment on table reg 		is 'Registry';
comment on column reg.regcod	is 'Id';
comment on column reg.regdes	is 'Description and usage';
comment on column reg.regnum	is 'Numeric value';
comment on column reg.regtxt	is 'Text value';

insert into reg values ('cargo.system.language', 'List of supported languages. The first one is the standard.', 0, 'en,es');
insert into reg values ('cargo.system.currency', 'System currency', 0, 'EUR');

/*
 * sequences
 */
drop table if exists seq;

create table seq (
	seqcod		varchar(256) not null default '' primary key,
	seqnxt		bigint not null default 0
);

comment on table seq		is 'Identity';
comment on column seq.seqcod	is 'Sequence';
comment on column seq.seqnxt	is 'Next value to be used';



