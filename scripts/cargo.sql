/*
 * CREATE ROLE cargo LOGIN ENCRYPTED PASSWORD 'yourpassword';
 * CREATE DATABASE cargodb OWNER = cargo ENCODING = 'UTF-8';
 *
 */

drop table if exists identity;

create table identity (
	entity varchar(20) not null default '' primary key,
	next_value bigint not null default 0
);

comment on table identity is 'Identities';
comment on column identity.entity is 'Entity';
comment on column identity.next_value is 'Next value';

drop table if exists registry;

create table registry (
	id varchar(256) not null default '' primary key,
	description text not null default '',
	numeric_value numeric not null default '0',
	text_value text not null default ''
);

comment on table registry is 'Registry';
comment on column registry.id is 'Id';
comment on column registry.description is 'Description and usage';
comment on column registry.numeric_value is 'Numeric value';
comment on column registry.text_value is 'Text value';


