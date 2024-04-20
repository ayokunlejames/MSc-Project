USE NHS_PIM;
CREATE TABLE authorized_rep (
    rep_id         VARCHAR(32) NOT NULL,
    rep_name       VARCHAR(32) NOT NULL,
    contact_number CHAR(11) NOT NULL,
    email          VARCHAR(32)
);

ALTER TABLE authorized_rep ADD CONSTRAINT authorized_rep_pk PRIMARY KEY ( rep_id );

CREATE TABLE gmdn (
    gmdn_code            VARCHAR(32) NOT NULL,
    gmdn_term_name       VARCHAR(32) NOT NULL,
    gmdn_term_definition TEXT
);

ALTER TABLE gmdn ADD CONSTRAINT gmdn_pk PRIMARY KEY (gmdn_code);

CREATE TABLE item_model (
    gmn                      CHAR(25) NOT NULL,
    model_name               VARCHAR(32) NOT NULL,
    device_type              VARCHAR(32) NOT NULL,
    market_availability_date DATE,
    lifecycle_status         VARCHAR(32) NOT NULL,
    last_status_update       DATE,
    risk_class_class_name    VARCHAR(32) NOT NULL
);

ALTER TABLE item_model ADD CONSTRAINT item_model_pk PRIMARY KEY ( gmn );

CREATE TABLE manufacturer (
    manufacturer_gln        CHAR(13) NOT NULL,
    manufacturer_name       VARCHAR(32) NOT NULL,
    manufacturer_address    TEXT NOT NULL,
    company_registration_no VARCHAR(32) NOT NULL,
    customer_service_phone  CHAR(11),
    customer_service_email  VARCHAR(32)
);

ALTER TABLE manufacturer ADD CONSTRAINT manufacturer_pk PRIMARY KEY ( manufacturer_gln );

CREATE TABLE manufacturer_catalog (
    manufacturer_product_code     VARCHAR(32) NOT NULL,
    product_name                  VARCHAR(32) NOT NULL,
    product_model                 VARCHAR(32) NOT NULL,
    product_category              VARCHAR(32),
    market_availability_date      DATE,
    lifecycle_status              VARCHAR(32) NOT NULL,
    last_status_update            DATE,
    manufacturer_manufacturer_gln CHAR(13) NOT NULL,
    authorized_rep_rep_id         VARCHAR(32) NOT NULL,
    risk_class_class_name         VARCHAR(32) NOT NULL
);

ALTER TABLE manufacturer_catalog ADD CONSTRAINT manufacturer_catalog_pk PRIMARY KEY (manufacturer_product_code);

CREATE TABLE nhs_product_classification (
    eclass_code VARCHAR(32) NOT NULL,
    description TEXT NOT NULL
);

ALTER TABLE nhs_product_classification ADD CONSTRAINT nhs_product_classification_pk PRIMARY KEY (eclass_code);

CREATE TABLE nhs_provider (
    provider_gln             CHAR(13) NOT NULL,
    provider_name            VARCHAR(32) NOT NULL,
    provider_address         TEXT NOT NULL,
    provider_registration_no VARCHAR(32) NOT NULL
);

ALTER TABLE nhs_provider ADD CONSTRAINT nhs_provider_pk PRIMARY KEY (provider_gln);

CREATE TABLE risk_class (
    class_name              VARCHAR(32) NOT NULL,
    class_description       TEXT,
    regulatory_requirements TEXT
);

ALTER TABLE risk_class ADD CONSTRAINT risk_class_pk PRIMARY KEY (class_name);

CREATE TABLE supplier (
    supplier_gln            CHAR(13) NOT NULL,
    supplier_name           VARCHAR(32) NOT NULL,
    supplier_address        TEXT NOT NULL,
    company_registration_no VARCHAR(32) NOT NULL,
    customer_service_phone  CHAR(11),
    customer_service_email  VARCHAR(32)
);

ALTER TABLE supplier ADD CONSTRAINT supplier_pk PRIMARY KEY (supplier_gln);

CREATE TABLE trade_item (
    gtin                      CHAR(14) NOT NULL,
    brand_name                VARCHAR(32) NOT NULL,
    serial_number             VARCHAR(32),
    batch_number              VARCHAR(32),
    manufacturing_date        DATE,
    expiry_date               DATE,
    udi_pi                    VARCHAR(32),
    unit_of_issue             VARCHAR(32),
    unit_of_use               VARCHAR(32),
    quantity_of_uou           INTEGER,
    unit_of_use_udi           CHAR(14) NOT NULL,
    item_length_cm            CHAR,
    item_height_cm            CHAR,
    item_width_cm             CHAR,
    item_weight_gram          CHAR,
    item_volume_ccm           CHAR,
    unit_of_dimension         CHAR(2),
    product_description       TEXT,
    storage_handling          TEXT,
    single_use                CHAR(1) NOT NULL,
    restricted_no_of_use      INTEGER,
    sterile                   VARCHAR(32) NOT NULL,
    sterilize_before_use      VARCHAR(32) NOT NULL,
    sterilization_method      TEXT,
    item_contains_latex       VARCHAR(32),
    item_contains_dehp        VARCHAR(32),
    item_mri_compatible       VARCHAR(32),
    supplier_supplier_gln     CHAR(13) NOT NULL,
    item_model_gmn            CHAR(25) NOT NULL,
    gmdn_gmdn_code            VARCHAR(32) NOT NULL,
    manufacturer_catalog_mpc  VARCHAR(32) NOT NULL,
    nhs_provider_provider_gln CHAR(13) NOT NULL,
    nhs_eclass_code           VARCHAR(32) NOT NULL
);

ALTER TABLE trade_item ADD CONSTRAINT trade_item_pk PRIMARY KEY (gtin);

ALTER TABLE manufacturer_catalog
    ADD CONSTRAINT authorized_rep_fk FOREIGN KEY ( authorized_rep_rep_id )
        REFERENCES authorized_rep (rep_id);

ALTER TABLE trade_item
    ADD CONSTRAINT gtin_eclass_fk FOREIGN KEY (nhs_eclass_code)
        REFERENCES nhs_product_classification (eclass_code);

ALTER TABLE trade_item
    ADD CONSTRAINT gtin_gmdn_fk FOREIGN KEY (gmdn_gmdn_code)
        REFERENCES gmdn ( gmdn_code );

ALTER TABLE trade_item
    ADD CONSTRAINT gtin_gmn_fk FOREIGN KEY (item_model_gmn)
        REFERENCES item_model  (gmn);

ALTER TABLE trade_item
    ADD CONSTRAINT gtin_mpc_fk FOREIGN KEY (manufacturer_catalog_mpc)
        REFERENCES manufacturer_catalog (manufacturer_product_code);

ALTER TABLE trade_item
    ADD CONSTRAINT gtin_nhs_provider_fk FOREIGN KEY (nhs_provider_provider_gln)
        REFERENCES nhs_provider (provider_gln);

ALTER TABLE item_model
    ADD CONSTRAINT item_model_risk_class_fk FOREIGN KEY (risk_class_class_name)
        REFERENCES risk_class (class_name);

ALTER TABLE manufacturer_catalog
    ADD CONSTRAINT manufacturer_fk FOREIGN KEY (manufacturer_manufacturer_gln)
        REFERENCES manufacturer (manufacturer_gln);

ALTER TABLE manufacturer_catalog
    ADD CONSTRAINT risk_class_fk FOREIGN KEY (risk_class_class_name)
        REFERENCES risk_class (class_name);

ALTER TABLE trade_item
    ADD CONSTRAINT trade_item_supplier_fk FOREIGN KEY (supplier_supplier_gln)
        REFERENCES supplier (supplier_gln);
