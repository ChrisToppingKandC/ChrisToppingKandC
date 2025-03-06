CREATE OR REPLACE VIEW odw_curated_db.vw_nsip_s51_advice

    AS

SELECT DISTINCT

AD.NSIPAdviceID										AS [adviceId],
AD.AdviceReference									AS [adviceReference],
AD.CaseReference									AS [caseReference],
AD.Section51Advice									AS [title],
AD.EnquirerFirstName & ' ' & AD.EnquirerLastName	AS [from]


FROM odw_harmonised_db.casework_nsip_advice_dim 	AS AD
