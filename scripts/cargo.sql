/*
 * CREATE ROLE cargo LOGIN ENCRYPTED PASSWORD 'yourpassword';
 * CREATE DATABASE cargodb OWNER = cargo ENCODING = 'UTF-8';
 *
 */

drop table ico; -- depends icu, iln

drop table if exists iln;

create table iln (
	ilncod		varchar(2) not null default '' primary key,
	ilndes		varchar(80) not null default ''
);
comment on table	iln is 'ISO 639 language code';
comment on column	iln.ilncod is 'Alpha-2 code';
comment on column	iln.ilndes is 'Description';

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

comment on table	icu is 'ISO 639 language code';
comment on column	icu.icucod is 'Alpha-3 code';
comment on column	icu.icudes is 'Description';
comment on column	icu.icudas is 'Digits after decimal separator';

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

comment on table reg is 'Registry';
comment on column reg.regcod is 'Id';
comment on column reg.regdes is 'Description and usage';
comment on column reg.regnum is 'Numeric value';
comment on column reg.regtxt is 'Text value';

/*
 * sequences
 */
drop table if exists seq;

create table seq (
	seqcod		varchar(256) not null default '' primary key,
	seqnxt		bigint not null default 0
);

comment on table seq is 'Identity';
comment on column seq.seqcod is 'Sequence';
comment on column seq.seqnxt is 'Next value to be used';



