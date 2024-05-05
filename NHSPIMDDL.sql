USE NHS_PIM;

-- CREATE TABLE STATEMENTS
CREATE TABLE `authorized_rep` (
  `rep_id` varchar(32) NOT NULL,
  `rep_name` varchar(32) NOT NULL,
  `contact_number` char(11) NOT NULL,
  `email` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`rep_id`)
) ;

CREATE TABLE `gmdn` (
  `gmdn_code` varchar(32) NOT NULL,
  `gmdn_term_name` varchar(32) NOT NULL,
  `gmdn_term_definition` text,
  PRIMARY KEY (`gmdn_code`)
) ;

CREATE TABLE `risk_class` (
  `class_name` varchar(32) NOT NULL,
  `class_description` text,
  `regulatory_requirements` text,
  PRIMARY KEY (`class_name`)
) ;

CREATE TABLE `nhs_product_classification` (
  `eclass_code` varchar(32) NOT NULL,
  `description` text NOT NULL,
  PRIMARY KEY (`eclass_code`)
) ;

CREATE TABLE `manufacturer` (
  `manufacturer_gln` char(13) NOT NULL,
  `manufacturer_name` varchar(32) NOT NULL,
  `manufacturer_address` text NOT NULL,
  `company_registration_no` varchar(32) NOT NULL,
  `customer_service_phone` char(11) DEFAULT NULL,
  `customer_service_email` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`manufacturer_gln`)
) ;

CREATE TABLE `nhs_provider` (
  `provider_gln` char(13) NOT NULL,
  `provider_name` text NOT NULL,
  `provider_address` text NOT NULL,
  `provider_registration_no` varchar(32) NOT NULL,
  PRIMARY KEY (`provider_gln`)
) ;

CREATE TABLE `supplier` (
  `supplier_gln` char(13) NOT NULL,
  `supplier_name` varchar(32) NOT NULL,
  `supplier_address` text NOT NULL,
  `company_registration_no` varchar(32) NOT NULL,
  `customer_service_phone` char(11) DEFAULT NULL,
  `customer_service_email` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`supplier_gln`)
) ;

CREATE TABLE `item_model` (
  `gmn` char(25) NOT NULL,
  `model_name` varchar(32) NOT NULL,
  `device_type` varchar(32) NOT NULL,
  `market_availability_date` date DEFAULT NULL,
  `lifecycle_status` varchar(32) NOT NULL,
  `last_status_update` date DEFAULT NULL,
  PRIMARY KEY (`gmn`)
) ;

CREATE TABLE `manufacturer_catalog` (
  `manufacturer_reference_no` varchar(32) NOT NULL,
  `product_name` varchar(32) NOT NULL,
  `product_model` varchar(32) NOT NULL,
  `product_category` varchar(32) DEFAULT NULL,
  `market_availability_date` date DEFAULT NULL,
  `lifecycle_status` varchar(32) NOT NULL,
  `last_status_update` date DEFAULT NULL,
  `manufacturer_manufacturer_gln` char(13) NOT NULL,
  `authorized_rep_rep_id` varchar(32) NOT NULL,
  PRIMARY KEY (`manufacturer_reference_no`),
  KEY `authorized_rep_fk` (`authorized_rep_rep_id`),
  KEY `manufacturer_fk` (`manufacturer_manufacturer_gln`),
  CONSTRAINT `authorized_rep_fk` FOREIGN KEY (`authorized_rep_rep_id`) REFERENCES `authorized_rep` (`rep_id`),
  CONSTRAINT `manufacturer_fk` FOREIGN KEY (`manufacturer_manufacturer_gln`) REFERENCES `manufacturer` (`manufacturer_gln`)
) ;

CREATE TABLE `medical_device` (
  `gtin` char(14) NOT NULL,
  `brand_name` varchar(32) NOT NULL,
  `unit_of_use` varchar(32) DEFAULT NULL,
  `quantity_of_uou` int DEFAULT NULL,
  `item_length` double DEFAULT NULL,
  `item_height` double DEFAULT NULL,
  `item_width` double DEFAULT NULL,
  `item_weight` double DEFAULT NULL,
  `item_volume` double DEFAULT NULL,
  `unit_of_dimension` char(2) DEFAULT NULL,
  `product_description` text,
  `storage_handling` text,
  `single_use` varchar(3) NOT NULL,
  `restricted_no_of_use` int DEFAULT NULL,
  `sterile` varchar(3) NOT NULL,
  `sterilize_before_use` varchar(3) NOT NULL,
  `sterilization_method` text,
  `item_contains_latex` varchar(3) DEFAULT NULL,
  `item_contains_dehp` varchar(3) DEFAULT NULL,
  `item_mri_compatible` varchar(3) DEFAULT NULL,
  `nhs_eclass_code` varchar(32) NOT NULL,
  `gmn` char(25) NOT NULL,
  `gmdn_code` varchar(32) NOT NULL,
  `manufacturer_reference_no` varchar(32) DEFAULT NULL,
  `risk_class_name` varchar(32) NOT NULL
  PRIMARY KEY (`gtin`),
  KEY `medical_device_gmdn_fk` (`gmdn_code`),
  KEY `medical_device_item_model_fk` (`gmn`),
  KEY `medical_device_nhs_product_classification_fk` (`nhs_eclass_code`),
  KEY `medical_device_manufacturer_ref_fk` (`manufacturer_reference_no`),
  KEY `medical_device_risk_class_fk` (`risk_class_name`),
  CONSTRAINT `medical_device_gmdn_fk` FOREIGN KEY (`gmdn_code`) REFERENCES `gmdn` (`gmdn_code`),
  CONSTRAINT `medical_device_item_model_fk` FOREIGN KEY (`gmn`) REFERENCES `item_model` (`gmn`),
  CONSTRAINT `medical_device_manufacturer_ref_fk` FOREIGN KEY (`manufacturer_reference_no`) REFERENCES `manufacturer_catalog` (`manufacturer_reference_no`),
  CONSTRAINT `medical_device_nhs_product_classification_fk` FOREIGN KEY (`nhs_eclass_code`) REFERENCES `nhs_product_classification` (`eclass_code`),
  CONSTRAINT `medical_device_risk_class_fk` FOREIGN KEY ( `risk_class_name` ) REFERENCES risk_class (`class_name`)
) ;
    

CREATE TABLE `trade_item` (
  `UDI` varchar(32) NOT NULL,
  `gtin` char(14) NOT NULL,
  `serial_number` varchar(32) DEFAULT NULL,
  `batch_number` varchar(32) DEFAULT NULL,
  `manufacturing_date` date DEFAULT NULL,
  `expiry_date` date DEFAULT NULL,
  `udi_pi` varchar(32) NOT NULL,
  `unit_of_issue` varchar(32) DEFAULT NULL,
  `unit_of_use_udi` char(14) NOT NULL,
  `supplier_gln` char(13) NOT NULL,
  `nhs_provider_gln` char(13) NOT NULL,
  PRIMARY KEY (`UDI`),
  KEY `trade_item_medical_device_fk` (`gtin`),
  KEY `trade_item_nhs_provider_fk` (`nhs_provider_gln`),
  KEY `trade_item_supplier_fk` (`supplier_gln`),
  CONSTRAINT `trade_item_medical_device_fk` FOREIGN KEY (`gtin`) REFERENCES `medical_device` (`gtin`),
  CONSTRAINT `trade_item_nhs_provider_fk` FOREIGN KEY (`nhs_provider_gln`) REFERENCES `nhs_provider` (`provider_gln`),
  CONSTRAINT `trade_item_supplier_fk` FOREIGN KEY (`supplier_gln`) REFERENCES `supplier` (`supplier_gln`)
) ;

SHOW TABLES;

